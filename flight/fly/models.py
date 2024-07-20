from django.db import models

# Create your models here.
class Jun(models.Model):
    name = models.CharField(max_length= 100)

    def __str__(self):
        return  f"{self.name}"

class Fly(models.Model):
    bird = models.CharField(max_length= 100)
    forest = models.ForeignKey(Jun, on_delete= models.CASCADE,  related_name= "forest")

    def __str__(self):
        return f"{self.bird} lives in {self.forest}"
