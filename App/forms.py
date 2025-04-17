from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class SignupForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=UserProfile.USER_TYPES, required=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password1', 'password2', 'user_type']
