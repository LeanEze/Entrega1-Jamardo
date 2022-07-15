from django.db import models
from unittest.util import _MAX_LENGTH


class cerdo(models.Model):
    nombre = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.genero} {self.raza} {self.edad} años"

class gato(models.Model):
    nombre = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.genero}, {self.raza}, {self.edad} años"

class perro(models.Model):
    nombre = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
    edad = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}, {self.genero}, {self.raza}, {self.edad}años"