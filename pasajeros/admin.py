from django.contrib import admin
from .models import Perfil, Cuentas, Movimientos
from django.utils.html import format_html

# Register your models here.
class CuentasAdmin(admin.ModelAdmin):
	list_display = ('user', 'no_cuenta', 'saldo')

class PerfilesAdmin(admin.ModelAdmin):
	list_display = ('user', 'direccion', 'estado', 'image_photo')

	def image_photo(self, obj):
		url = obj.foto.url
		return format_html("<img class='img-circle' src='/"+url+"' width=100>")


admin.site.register(Perfil, PerfilesAdmin)
admin.site.register(Cuentas, CuentasAdmin)
admin.site.register(Movimientos)