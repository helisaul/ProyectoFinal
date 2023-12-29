from django import forms
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    pass


class RegisterForm(UserCreationForm):

    telefono = forms.CharField(max_length=15, required=True, help_text='Número de teléfono')
    CUI = forms.CharField(max_length=15, required=True, help_text='Número de DPI')
    
    class Meta:
        model = User
        fields = ['first_name','last_name','CUI','telefono','username','email','password1','password2']

