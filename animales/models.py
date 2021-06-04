from django.db import models

# Create your models here.
class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    numero_patas = models.IntegerField()

    carnivoro = models.BooleanField()
    herbivoro = models.BooleanField()
