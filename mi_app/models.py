from django.db import models
from unittest.util import _MAX_LENGTH


class Cerdo(models.Model): # Nombre de los modelos deben comenzar con mayuscula
    nombre = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.genero} {self.raza} {self.edad} años"

class Gato(models.Model): # Nombre de los modelos deben comenzar con mayuscula
    nombre = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.genero}, {self.raza}, {self.edad} años"

class Perro(models.Model): # Nombre de los modelos deben comenzar con mayuscula
    nombre = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
    edad = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}, {self.genero}, {self.raza}, {self.edad} años"