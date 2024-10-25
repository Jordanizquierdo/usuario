from django.db import models

# Create your models here.

class User(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    numero = models.CharField(max_length=10)
    correo = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
