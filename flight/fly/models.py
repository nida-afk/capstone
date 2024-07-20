from django.db import models

# Create your models here.
class Fly(models.Model):
    bird = models.CharField(max_length= 100)
    
