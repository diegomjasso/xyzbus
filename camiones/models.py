# Django Imports.
from django.db import models
from django.contrib.auth.models import User
from clientes.models import Conductores
from django.utils	import timezone

# Create your models here.
class Catalogo_rutas(models.Model):
	class Meta:
		verbose_name_plural = 'Catálogo de Rutas'

	id = models.AutoField(primary_key = True)
	ruta = models.CharField(max_length = 50)

	def __str__(self):
		return self.ruta

class Rutas(models.Model):
	class Meta:
		verbose_name_plural = 'Rutas'

	id = models.AutoField(primary_key = True)
	ruta = models.ForeignKey(Catalogo_rutas,on_delete = models.CASCADE)
	no_camion = models.IntegerField()
	conductor =	models.ForeignKey(Conductores,on_delete = models.CASCADE)

	def __str__(self):
		return ruta.ruta

class Rutas_favoritas(models.Model):
	class Meta:
		verbose_name_plural = 'Rutas Favoritas'

	id = models.AutoField(primary_key = True)
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	ruta = models.ForeignKey(Catalogo_rutas,on_delete = models.CASCADE)

	def __str__(self):
		return self.user.first_name + ' ' + self.user.last_name
		