# models.py


from django.db import models
from django.contrib.auth.models import User




class Song(models.Model):
    track_id = models.CharField(max_length=100, unique=True)
    watchlist = models.ManyToManyField(User, blank=True,null = True,  related_name='watchlist')

