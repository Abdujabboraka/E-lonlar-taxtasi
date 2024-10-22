from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    address = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(blank=True,null=True, upload_to='user_avatar')
    phone = models.CharField(max_length=13)
    telegram_id = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category/', blank=True, null=True)

    def __str__(self):
        return self.name




class Announcement(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="elonlar/", blank=True, null=True)
    content = models.TextField(max_length=555 ,null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    telegram_id = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    deadline = models.DateField(null=True, blank=True)


    def save(self, *args, **kwargs):
        if self.telegram_id and "@" in self.telegram_id:
            self.telegram_id = self.telegram_id[1:]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.likes.count()


class Like(models.Model):
    REACTION_CHOICES = [
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    ]

    announcement = models.ForeignKey(Announcement, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reaction_type = models.CharField(max_length=10, choices=REACTION_CHOICES)

    class Meta:
        unique_together = ('announcement', 'user')


# Comment model
class Comment(models.Model):
    announcement = models.ForeignKey(Announcement, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.announcement.title}'



# Attachment model
class Attachment(models.Model):
    announcement = models.ForeignKey(Announcement, related_name='attachments', on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Attachment for {self.announcement.title}'


# Notification model
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification for {self.user.username} about {self.announcement.title}'
