from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """Custom user registration form."""
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'date_of_birth', 'password1', 'password2')
