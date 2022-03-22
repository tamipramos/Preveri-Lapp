from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.core.exceptions import ValidationError
# Create your models here.



class Task(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title=models.CharField(max_length=200, null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
    class Meta:
        ordering=['completed']

class Register(models.Model):
    username=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    password=models.CharField(max_length=200, null=True, blank=True)
    email=models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.username 

    class Meta:
        ordering=['username']

class UserManagement(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not username or email:
            raise ValueError('Los usuarios deben tener un nombre y una contraseña')

