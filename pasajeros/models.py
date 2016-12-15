from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Perfil(models.Model):
	class Meta:
		verbose_name_plural = 'Perfiles'

	id = models.AutoField(primary_key = True)
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	direccion = models.CharField(max_length = 200)
	ciudad = models.CharField(max_length = 140, default = 'Aguascalientes')
	estado = models.CharField(max_length = 140, default ='Aguascalientes')
	cp = models.IntegerField(default = 20200)
	edad = models.IntegerField()
	telefono = models.CharField(max_length = 10)
	foto = models.ImageField(upload_to = 'static/assets/images/user_photos', blank = True)

	def __str__(self):
		return self.user.username

class Cuentas(models.Model):
	class Meta:
		verbose_name_plural = 'Cuentas'
	
	id = models.AutoField(primary_key = True)
	user = models.OneToOneField(User)
	no_cuenta = models.CharField(max_length = 50)
	saldo = models.FloatField()

	def __str__(self):
		return self.user.username

class Movimientos(models.Model):
	class Meta:
		verbose_name_plural = 'Movimientos'

	MOVIMIENTOS = (
			('1', 'Ingreso'),
			('2', 'Descuento'),
			('3', 'Abono')
		)

	id = models.AutoField(primary_key = True)
	user = models.OneToOneField(User)
	tipo_movimiento = models.CharField(max_length = 140, choices=MOVIMIENTOS)
	saldo_anterior = models.DecimalField(max_digits = 10, decimal_places = 2)
	saldo_despues = models.DecimalField( max_digits = 10, decimal_places = 2)
	saldo_movimiento = models.DecimalField(max_digits = 10, decimal_places = 2)
	fecha = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.user.username




