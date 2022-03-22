import email
from tkinter import W
from traceback import format_stack
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput, EmailInput
import re
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

class CustomAuthForm(UserCreationForm):

    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Usuario'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Contraseña'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Repita contraseña'}))
    email = forms.EmailField( widget=EmailInput(attrs={'class':'validate','placeholder': 'Email'}))
    first_name = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Nombre'}))
    last_name = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Apellidos'}))

    class Meta(UserCreationForm.Meta):
        fields = ("username", "email", "last_name", "first_name",) 

    def clean_email(self):
        data = self.cleaned_data['email']
        domain = data.split('@')[1]
        domain_list = ["ieselrincon.es", "alumno.ieselrincon.es",]
        if domain not in domain_list:
            raise forms.ValidationError('Debes pertenecer al centro.')
        return data
        
    def save(self, commit=True):
        user = super(CustomAuthForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
            

        