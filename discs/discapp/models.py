from django.db import models
from django.urls import reverse

class DiscsData(models.Model):
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    image = models.CharField(max_length=20, null=True)
    
    def get_absolute_url(self): # new
        return ('/home')
    
    def __str__(self):
        return self.name
    