from django.db import models
from django.db.models.fields import BooleanField, IntegerField

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = IntegerField()
    donador = BooleanField()
    correo = models.EmailField()