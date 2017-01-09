from django.contrib import admin
from .models import Rutas, Rutas_favoritas, Catalogo_rutas, Corridas, Coordenadas_rutas, Coordenadas_corridas
from django.utils.html import format_html

# Register your models here.
class Catalogo_rutasAdmin(admin.ModelAdmin):
	list_display = ('ruta',)

class Rutas_favoritasAdmin(admin.ModelAdmin):
	list_display = ('user','ruta')

class RutasAdmin(admin.ModelAdmin):
	list_display = ('no_camion','ruta')

class CoordenadasRutasAdmin(admin.ModelAdmin):
	list_display = ('ruta','coordenadas','order','sentido')

class CorridasAdmin(admin.ModelAdmin):
	list_display = ('ruta', 'fecha_inicio', 'fecha_final', 'status', 'sentido')

class CoordenadasCorridasAdmin(admin.ModelAdmin):
	list_display = ('corrida', 'coordenadas')

admin.site.register(Rutas, RutasAdmin)
admin.site.register(Rutas_favoritas, Rutas_favoritasAdmin)
admin.site.register(Catalogo_rutas, Catalogo_rutasAdmin)
admin.site.register(Coordenadas_rutas, CoordenadasRutasAdmin)
admin.site.register(Corridas, CorridasAdmin)
admin.site.register(Coordenadas_corridas, CoordenadasCorridasAdmin)