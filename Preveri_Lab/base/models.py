from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.core.exceptions import ValidationError
# Create your models here.


class Register(models.Model):
    username=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    password=models.CharField(max_length=200, null=True, blank=True)
    email=models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.username 

    class Meta:
        ordering=['username']


