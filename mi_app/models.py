from django.db import models
from unittest.util import _MAX_LENGTH

class cerdo(models.Model):
    nombre = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
    edad = models.IntegerField

class gato(models.Model):
    nombre = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
    edad = models.IntegerField

class perro(models.Model):
    nombre = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
    edad = models.IntegerField