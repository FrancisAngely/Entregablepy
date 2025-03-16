from django.db import models
from datetime import date
import uuid

from django.forms import ValidationError
from django.urls import reverse


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
    password = models.CharField(max_length=128)  # Vuelve a hacer que el campo sea obligatorio
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

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['primer_nombre', 'apellido'], name='unique_estudiante')
        ]

    def get_absolute_url(self):
        return reverse('estudiante-detalle', kwargs={'pk': self.pk}) 
    def __str__(self):
        return f'{self.primer_nombre} {self.apellido}'


class Modulo(models.Model):
    nombre = models.CharField(max_length=200)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

def validar_nota(value):
    if value < 0 or value > 10:
        raise ValidationError('La nota debe estar entre 0 y 10.')
    
class Nota(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2, validators=[validar_nota])  # Validación a nivel de BD
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Nota de {self.estudiante} en {self.modulo}'

    def get_absolute_url(self):
        return reverse('nota-detalle', args=[str(self.id)])  # Redirige al detalle de la nota