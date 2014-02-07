from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from codewithbp.apps.customuser.models import CustomUser

class LoginForm(AuthenticationForm):
