from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# inherit from the usercreationform and adds an email field to it
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Gives nested configurations.
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Adding an email field to registerationg page

