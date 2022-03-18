from django.urls import path, include

from django.contrib.auth.views import LogoutView, LoginView
from .views import Index, LoginViewC
'''
Here comes the PATH+VIEW(HTML)+NAME of the APP

'''
urlpatterns = [
        
        path('login/', LoginViewC.as_view(), name="login"),

        path('', Index.as_view(template_name='base/index.html'), name="home"),
        
        path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
]

