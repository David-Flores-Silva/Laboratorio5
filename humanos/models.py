from django.db import models

# Create your models here.
class Humano(models.Model):
    nombre = models.CharField()
    sexo = models.CharField()