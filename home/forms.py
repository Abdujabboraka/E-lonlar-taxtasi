from django import forms
from .models import Announcement, Comment, Profile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'category', 'image', 'price', 'address', 'telegram_id', 'phone']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nomi'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "E'lon xaqida"}),
            'image': forms.ClearableFileInput(),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Narx: '}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Manzil:'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqam:'}),
            'telegram_id':  forms.TextInput(attrs={'class': 'form-control','placeholder': " '@' ni Yozmang! '@user' ❌   'user' ✅ "}),

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 2}),
        }


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parol:'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parolni qayta kitish:'}))

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username:'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismi:'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familiya:'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parol'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parolni qayta kitish'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone', 'telegram_id', 'photo']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Manzil'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqam'}),
            'telegram_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': " '@' ni Yozmang! '@user' ❌   'user' ✅ "}),
            'photo': forms.ClearableFileInput(),
        }

        help_texts = {
            'photo': 'JPG, PNG, GIF formatlarda rasmlar qo\'shilish mumkin. Rasmning rangi 1MB dan ko\'p emas.'
        }


