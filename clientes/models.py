from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Concesionarios(models.Model):
	class Meta:
		verbose_name_plural = 'Concesionarios'

	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 100)
	rfc = models.CharField(max_length = 15)
	direccion = models.CharField(max_length = 200)
	telefono = models.CharField(max_length = 10)
	ciudad = models.CharField(max_length = 140, default = 'Aguascalientes')
	estado = models.CharField(max_length = 140, default ='Aguascalientes')
	latitud =  models.CharField(max_length = 25)
	longitud =  models.CharField(max_length = 25)

	def __str__(self):
		return self.nombre
		
class TipoTrabajador(models.Model):
	class Meta:
		verbose_name_plural = 'Tipo de trabajadores'

	id = models.AutoField(primary_key = True)
	tipo = models.CharField(max_length = 100)

	def __str__(self):
		return self.tipo

class Trabajador(models.Model):
	class Meta:
		verbose_name_plural = 'Trabajadores'

	id = models.AutoField(primary_key = True)
	user = models.ForeignKey(User,	on_delete = models.CASCADE)
	tipo = models.ForeignKey(TipoTrabajador,	on_delete = models.CASCADE)
	concesionario = models.ForeignKey(	Concesionarios,	on_delete = models.CASCADE)
	curp = models.CharField(max_length = 30)
	rfc = models.CharField(max_length = 15)
	fecha_de_nacimiento = models.DateTimeField(default = timezone.now)
	fecha_de_ingreso = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.user.first_name + ' ' + self.user.last_name

class Conductores(models.Model):
	class Meta:
		verbose_name_plural = 'Conductores'

	id = models.AutoField(primary_key = True)
	trabajador = models.ForeignKey(	Trabajador,	on_delete = models.CASCADE)
	licencia_de_conducir = models.CharField(max_length = 100)

	def __str__(self):
		return self.trabajador.user.first_name + ' ' + self.trabajador.user.last_name