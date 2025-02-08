from django.db import models

from django.contrib.auth.models import AbstractUser

from django.core.exceptions import ValidationError

# Create your models here.


def valideCin(value):
    if len(value) != 8:
        
        raise ValidationError ("Cin must has 8 characters")


def valideEmail(value):
    
    if value.endswith('@esprit.tn')==False:
        
        raise ValidationError (f"Your email  {value} must end with @esprit.tn")




class Person(AbstractUser):
    cin = models.CharField(max_length=8 , primary_key=True , validators=[valideCin])
    email = models.EmailField( validators=[valideEmail])
    username=models.CharField(max_length=30 ,unique=True)
    
    USERNAME_FIELD="username"
    
    
    class Meta:
        verbose_name="Person"
    