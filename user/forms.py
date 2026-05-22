from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    ROLE_CHOICES = [
         ("attendant", "Parking Attendant"),
         ("tyre_manager", "Tyre Manager"),
         ("battery_manager", "Battery Manager"),
         ("admin", "System Admin"),
     ]
    role = forms.ChoiceField(choices=ROLE_CHOICES)
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2', 'role'
        ]