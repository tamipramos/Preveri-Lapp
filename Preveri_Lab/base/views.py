#GENERAL MODULES
from re import template
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
###

#LOCAL MODULES
import re
from .forms import CustomAuthForm
from .models import Task
###

class Home(LoginRequiredMixin, TemplateView):
    #model = MODELO
    #fields = ['table entries']                                     #shows only the fields in the DB table
    #def form_valid(self, form):
    #form.instance.user = self.request.user                         #returning only data from the current user
    #return super(FORM_NAME, self).form_valid(form)
    #def get_context_data(self, **kwargs):                          #returns the value of context 
        #context=super().get_context_data(**kwargs)                 
        #context['color']= 'red'                                    #In this case it is returning 'red'
        #return context                                             #The specification will be called as a variable it self.
                                                                    # {{color}} = 'red'
                                                                    #As an extended option we can also filter the content shown
    #def get_context_data(self, **kwargs):                  
        #context=super().get_context_data(**kwargs)                 #Now we are showing a context depending of the user session ID
        #context['tasks']= context['tasks'].filter(user=self.request.user)
        #context['count']= context['tasks'].filter(completed=False).count() #we are passing the filter to the variable "Count saying"
        #                                                                   #tasks that are not "completed" wont be shown and counting the amount of them.
        #return context

    template_name = 'base/home.html'

class RegisterViewC(FormView):
    template_name = "base/register.html"
    form_class = CustomAuthForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
           login(self.request, user)
        return super(RegisterViewC, self).form_valid(form)

class LoginViewC(LoginView):
    template_name= 'base/login.html'
    redirect_autheticated_user=True
    def get_success_url(self):
        return reverse_lazy('home')

