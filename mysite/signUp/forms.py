from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    myteam = forms.CharField(max_length=254, help_text='Create team.')
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2')

class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(label=("Email Or Username"), max_length=254)