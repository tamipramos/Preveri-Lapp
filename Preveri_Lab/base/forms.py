from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput, EmailInput
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from Preveri_Lab.settings import RECAPTCHA_PUBLIC_KEY, RECAPTCHA_PRIVATE_KEY

class CustomAuthForm(UserCreationForm):

    username = forms.CharField(label="Usuario", widget=TextInput(attrs={'class':'validate','placeholder': 'Usuario'}))
    password1 = forms.CharField(label="Contraseña", widget=PasswordInput(attrs={'placeholder':'Contraseña'}))
    password2 = forms.CharField(label="Contraseña", widget=PasswordInput(attrs={'placeholder':'Repita la contraseña'}))
    email = forms.EmailField(label="Email", widget=EmailInput(attrs={'class':'validate','placeholder': 'Email'}))
    first_name = forms.CharField(label="Nombre", widget=TextInput(attrs={'class':'validate','placeholder': 'Nombre'}))
    last_name = forms.CharField(label="Apellidos", widget=TextInput(attrs={'class':'validate','placeholder': 'Apellidos'}))
    captcha = ReCaptchaField(label="Captcha", widget=ReCaptchaV2Checkbox)

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





    
