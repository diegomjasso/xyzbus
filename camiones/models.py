# Django Imports.
from django.db import models
from django.contrib.auth.models import User
from clientes.models import Conductores
from django.utils	import timezone
from geoposition.fields import GeopositionField

# Create your models here.
class Catalogo_rutas(models.Model):
	class Meta:
		verbose_name_plural = 'Catálogo de Rutas'

	id = models.AutoField(primary_key = True)
	ruta = models.CharField(max_length = 50)
	punto_inicio = GeopositionField(blank=True)
	punto_final = GeopositionField(blank=True)

	def __str__(self):
		return self.ruta

class Coordenadas_rutas(models.Model):
	class Meta:
		verbose_name_plural = 'Coordenadas de las Rutas'

	TYPE_SENTIDO = (
			(1, 'Ida'),
			(2, 'Vuelta')
		)

	id = models.AutoField(primary_key = True)
	ruta = models.ForeignKey(Catalogo_rutas,on_delete = models.CASCADE)
	coordenadas = GeopositionField(blank=True)
	order = models.IntegerField()
	sentido = models.IntegerField(default = 1,choices = TYPE_SENTIDO)

	def __str__(self):
		return str(self.coordenadas)


class Rutas(models.Model):
	class Meta:
		verbose_name_plural = 'Rutas'

	id = models.AutoField(primary_key = True)
	ruta = models.ForeignKey(Catalogo_rutas,on_delete = models.CASCADE)
	no_camion = models.IntegerField()
	conductor =	models.ForeignKey(Conductores,on_delete = models.CASCADE)

	def __str__(self):
		return str(self.ruta)


class Rutas_favoritas(models.Model):
	class Meta:
		verbose_name_plural = 'Rutas Favoritas'

	id = models.AutoField(primary_key = True)
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	ruta = models.ForeignKey(Catalogo_rutas,on_delete = models.CASCADE)

	def __str__(self):
		return self.user.first_name + ' ' + self.user.last_name

class Corridas(models.Model):
	class Meta:
		verbose_name_plural = 'Corridas'

	TYPE_SENTIDO = (
			(1, 'Ida'),
			(2, 'Vuelta')
		)

	TYPE_STATUS = (
			(1,	'En proceso'),
			(2,	'Finalizada'),
			(3, 'En pausa'),
			(4, 'Cancelado')
		)

	id = models.AutoField(primary_key = True)
	ruta = models.ForeignKey(Rutas, on_delete = models.CASCADE)
	fecha_inicio = models.DateTimeField(default = timezone.now)
	fecha_final = models.DateTimeField(null = True, blank = True)
	status = models.IntegerField(default = 1,choices = TYPE_STATUS)
	sentido = models.IntegerField(default = 1,choices = TYPE_SENTIDO)

	def __str__(self):
		return str(self.ruta) + ' - ' + str(self.sentido) + ' - ' + str(self.status)

class Coordenadas_corridas(models.Model):
	class Meta:
		verbose_name_plural = 'Coordenadas de Corridas'

	id = models.AutoField(primary_key = True)
	corrida = models.ForeignKey(Corridas, on_delete = models.CASCADE)
	coordenadas = GeopositionField()

	def __str__(self):
		return str(self.coordenadas)