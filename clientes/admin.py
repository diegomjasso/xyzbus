from django.contrib import admin
from .models import Concesionarios,	TipoTrabajador,	Trabajador,	Conductores
from django.utils.html import format_html

# Register your models here.
class ConcesionariosAdmin(admin.ModelAdmin):
	list_display = ('nombre','rfc','direccion')

class TipoTrabajadorAdmin(admin.ModelAdmin):
	list_display = ('tipo',)

class TrabajadorAdmin(admin.ModelAdmin):
	list_display = ('name', 'curp',	'rfc')

	def name(self, obj):
		return obj.user.first_name+' '+obj.user.last_name

class ConductoresAdmin(admin.ModelAdmin):
	list_display = ('trabajador','licencia_de_conducir')

admin.site.register(	Concesionarios,ConcesionariosAdmin)
admin.site.register(	TipoTrabajador,TipoTrabajadorAdmin)
admin.site.register(	Trabajador,TrabajadorAdmin)
admin.site.register(	Conductores,ConductoresAdmin)