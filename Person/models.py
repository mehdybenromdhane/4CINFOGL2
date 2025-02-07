from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class Person(AbstractUser):
    cin = models.CharField(max_length=8 , primary_key=True)
    email = models.EmailField()
    username=models.CharField(max_length=30 ,unique=True)
    
    USERNAME_FIELD="username"
    
    
    class Meta:
        verbose_name="Person"
    