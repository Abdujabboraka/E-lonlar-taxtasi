from django.contrib import admin
from .models import Category, Announcement, Comment, Like, Attachment, Notification, Profile
# Register your models here.

admin.site.register(Category)
admin.site.register(Announcement)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Attachment)
admin.site.register(Notification)
admin.site.register(Profile)
