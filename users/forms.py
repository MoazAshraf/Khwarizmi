from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserSignupForm(UserCreationForm):
    email = forms.EmailField()  # we add this to make the email required since the default User has blank=True for the email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(required=False, max_length=256, widget=forms.Textarea)

    class Meta:
        model = Profile
        fields = ['display_name', 'bio', 'image']