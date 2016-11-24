from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Animal(models.Model):
	"""docstring for Animal"""
	nombre = models.CharField(max_length=50)
	edad = models.IntegerField()
	fecha_ingreso = models.DateField()

	def __str__(self):
		return '{}'.format(self.nombre)

class Cliente(models.Model):
	documento = models.IntegerField()
	nombre = models.CharField(max_length=100)
	fecha_nacimiento = models.DateField()

	def __str__(self):
		return '{}'.format(self.nombre)

class Adopcion(models.Model):
	cliente = models.ForeignKey(Cliente, null=True,blank=True, on_delete=models.CASCADE)
	animal = models.ForeignKey(Animal, null=True,blank=True, on_delete=models.CASCADE)
	fecha = models.DateField()
