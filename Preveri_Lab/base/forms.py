from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput, EmailInput

class CustomAuthForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Usuario'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Contraseña'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Repita contraseña'}))
    email = forms.CharField(widget=EmailInput(attrs={'class':'validate','placeholder': 'Email'}))
    first_name = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Nombre'}))
    last_name = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Apellidos'}))

    class Meta(UserCreationForm.Meta):
        fields = ("username", "email", "last_name", "first_name")

    
