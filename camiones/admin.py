from django.contrib import admin
from .models import Rutas, Rutas_favoritas, Catalogo_rutas, Corridas
from django.utils.html import format_html

# Register your models here.
class Catalogo_rutasAdmin(admin.ModelAdmin):
	list_display = ('ruta',)

class Rutas_favoritasAdmin(admin.ModelAdmin):
	list_display = ('user','ruta')

class RutasAdmin(admin.ModelAdmin):
	list_display = ('no_camion','ruta')

admin.site.register(Corridas)
admin.site.register(Rutas, RutasAdmin)
admin.site.register(Rutas_favoritas, Rutas_favoritasAdmin)
admin.site.register(Catalogo_rutas, Catalogo_rutasAdmin)