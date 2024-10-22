from django.db.transaction import commit
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Announcement, Comment, Like, Category, Profile
from .forms import AnnouncementForm, CommentForm, RegisterForm, ProfileForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages

# profile edit form
def user_profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        form = RegisterForm(request.POST, instance=user)

        if profile_form.is_valid() and form.is_valid():
            form.save()  # Save the User form
            profile_instance = profile_form.save(commit=False)
            profile_instance.user = user
            profile_instance.save()  # Save the Profile form
            messages.success(request, 'Profile updated successfully!')
            return redirect('user_profile')
        else:
            messages.error(request, 'Profile update failed!')
    else:
        profile_form = ProfileForm(instance=profile)
        form = RegisterForm(instance=user)

    user_ads = Announcement.objects.filter(author=user)
    context = {
        'user': user,
        'profile': profile,
        'profile_form': profile_form,
        'form': form,
        'user_ads': user_ads,
    }

    return render(request, 'user_profile/profile.html', context)


def search(request):
    query = request.GET.get('q')  # Get the search query from the URL
    if query:
        # Search for announcements where the title or content contains the query
        results = Announcement.objects.filter(
            title__icontains=query
        ) | Announcement.objects.filter(content__icontains=query)
    else:
        results = Announcement.objects.none()  # Return no results if no query is entered

    return render(request, 'search_result.html', {'results': results, 'query': query})
# View to list all announcements
def announcement_list(request):
    announcements = Announcement.objects.filter(is_active=True).order_by('-date_created')
    categories = Category.objects.all()
    return render(request, 'announcements/announcement_list.html', {'announcements': announcements, 'categories': categories})

# View to display a single announcement
def announcement_detail(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)
    likes_count = announcement.likes_count()
    ads = Announcement.objects.filter(category = announcement.category)
    comments = announcement.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.announcement = announcement
            comment.user = request.user
            comment.save()
            return redirect('announcement_detail', announcement_id=announcement.id)
    else:
        comment_form = CommentForm()

    return render(request, 'announcements/announcement_detail.html', {
        'announcement': announcement,
        'comments': comments,
        'comment_form': comment_form,
        'ads': ads,
        'likes_count': likes_count,
    })



@login_required(login_url='login')
def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, request.FILES)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.author = request.user

            announcement.save()
            messages.success(request, "Announcement created successfully!")  # Optional success message
            return redirect('announcement_list')
    else:
        form = AnnouncementForm()

    return render(request, 'announcements/create_announcement.html', {'form': form})


# View to like an announcement
@login_required
def like_announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)
    like, created = Like.objects.get_or_create(announcement=announcement, user=request.user)
    if not created:
        like.delete()
    return redirect('announcement_detail', announcement_id=announcement.id)


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Muvaffaqiyatli Login')
            return redirect('announcement_list')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


# View for user logout
def user_logout(request):
    logout(request)
    messages.success(request, 'Muvafaqqiyatli Log out')
    return redirect('announcement_list')  # Redirect to the announcement list after logout


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            messages.success(request, 'Muvaffaqiyatli registratsiyadan o\'tdingiz!')
            return redirect('announcement_list')  # Redirect after registration
    else:
        form = RegisterForm()
        profile_form = ProfileForm()

    return render(request, 'register.html', {'form': form, 'profile_form': profile_form})


def select_category(request, category_id):
    announcements = Announcement.objects.filter(category_id=category_id, is_active=True).order_by('-date_created')
    return render(request, 'announcements/announcement_list.html', {'announcements': announcements})


def sponsor(request):
    return render(request, 'Sponsor/chimyon-patir.html')