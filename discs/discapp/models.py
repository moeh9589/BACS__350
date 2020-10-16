from django.db import models

class Discs(models.Model):
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    image = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.name
    