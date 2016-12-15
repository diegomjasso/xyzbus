from django.db import models

# Django Imports.
from django.db import models
from django.contrib.auth.models import User
from django.utils	import timezone

# Create your models here.
class Rutas(models.Model):
	class Meta:
		verbose_name_plural = 'Rutas'

	id = models.AutoField(primary_key = True)
	ruta = models.CharField(max_length = 50)
	#no_paradas = models.IntegerField()

	def __str__(self):
		return self.ruta

class Rutas_favoritas(models.Model):
	class Meta:
		verbose_name_plural = 'Rutas Favoritas'

	id = models.AutoField(primary_key = True)
	user = models.ForeignKey(User,	on_delete = models.CASCADE)
	ruta = models.ForeignKey(Rutas,	on_delete = models.CASCADE)

	def __str__(self):
		return self.user.username

class Catalogo_rutas(models.Model):
	class Meta:
		verbose_name_plural = 'Catálogo de Rutas'

	id = models.AutoField(primary_key = True)
	ruta = models.ForeignKey(Rutas,	on_delete = models.CASCADE)
	no_camion = models.IntegerField()

	def __str__(self):
		return self.ruta.ruta
		