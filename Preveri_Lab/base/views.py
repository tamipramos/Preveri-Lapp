#GENERAL MODULES
from re import template
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
###

#GENERICS
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
###

#LOGIN - LOGOUT - REGISTER
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
###

#LOCAL MODULES
from .models import Task
###

class Index(TemplateView):
    template_name = 'index.html'

class Menu(TemplateView):
    template_name = "menu.html"

class LoginViewC(LoginView):
    template_name= 'base/login.html'
    redirect_autheticated_user=True
    def get_success_url(self):
        return reverse_lazy('home')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully!!!')
                    return render(request, 'home')
        else:
            fm = AuthenticationForm()
        return render(request,'base/index.html',{'form':fm})
    else:
        return render(request, 'home')