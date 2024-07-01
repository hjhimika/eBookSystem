from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from admin_app.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['fullname', 'email',  'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')