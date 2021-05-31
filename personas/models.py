from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = IntegerField()
    