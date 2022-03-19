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

class Index(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

class Menu(TemplateView):
    template_name = "menu.html"

class LoginViewC(LoginView):
    template_name= 'base/login.html'
    redirect_autheticated_user=True
    def get_success_url(self):
        return reverse_lazy('home')
