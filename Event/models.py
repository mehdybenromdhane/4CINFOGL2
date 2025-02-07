from django.db import models

# Create your models here.

from Person.models import Person

category_list = (('Musique','Musique'), 
                 ('Sport','Sport'),
                 ('Cinema','Cinema')
                 )
class Event(models.Model):
    title= models.CharField(max_length=20)
    description= models.TextField()
    category=models.CharField(choices=category_list , max_length=20)
    state= models.BooleanField(default=True)
    nbr_participants= models.IntegerField(default=0)
    evt_date= models.DateTimeField()
    creation_date= models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)
    
    organisateur = models.ForeignKey(Person,on_delete=models.CASCADE)
    
    participant = models.ManyToManyField(Person , through="Participants" , related_name="participant")
    
    
class Participants(models.Model):
    
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    particiaption_date=models.DateField(auto_now_add=True)