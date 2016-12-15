from django.contrib import admin
from .models import Rutas, Rutas_favoritas, Catalogo_rutas
from django.utils.html import format_html

# Register your models here.
class RutasAdmin(admin.ModelAdmin):
	list_display = ('ruta',)

class Rutas_favoritasAdmin(admin.ModelAdmin):
	list_display = ('user',	'ruta')

class Catalogo_rutasAdmin(admin.ModelAdmin):
	list_display = ('ruta',	'no_camion')

admin.site.register(Rutas, RutasAdmin)
admin.site.register(Rutas_favoritas, Rutas_favoritasAdmin)
admin.site.register(Catalogo_rutas, Catalogo_rutasAdmin)