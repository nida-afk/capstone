from django.db import models

# Create your models here.
class Jun(models.Model):
    name = models.CharField(max_length= 100)

    def __str__(self):
        return  f"{self.name}"

class Name(models.Model):
    i = models.CharField(max_length= 100)
    def __str__(self):
        return f"{self.i}"

class Fly(models.Model):
    bird = models.CharField(max_length= 100)
    forest = models.ForeignKey(Jun, on_delete= models.CASCADE,  related_name= "forest")
    name = models.ManyToManyField(Name,  related_name= "bird")
    def __str__(self):
        return f"{self.bird} lives in {self.forest} his name is { self.name.all()}"
