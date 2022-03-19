from django.urls import path, include

from django.contrib.auth.views import LogoutView, LoginView
from .views import LoginViewC, Home, SignUp
'''
Here comes the PATH+VIEW(HTML)+NAME of the APP

'''
urlpatterns = [
        
        path('login/', LoginViewC.as_view(), name="login"),

        path('', Home.as_view(template_name='base/home.html'), name="home"),

        path('signup/', SignUp.as_view(template_name='base/register.html'), name="register"),
        
        path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
]

