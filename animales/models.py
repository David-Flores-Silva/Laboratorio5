from django.db import models

# Create your models here.
class Animal(models.models):
    nombre = models.CharField(max_length=100)
    numuero_patas = models.IntegerField()
    