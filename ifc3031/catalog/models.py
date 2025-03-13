from django.db import models
from datetime import date
import uuid

class Rol(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    correo = models.EmailField(unique=True)
    primer_nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.correo


class Estudiante(models.Model):
    primer_nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.primer_nombre} {self.apellido}'


class Modulo(models.Model):
    nombre = models.CharField(max_length=200)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Nota(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Nota de {self.estudiante} en {self.modulo}'
