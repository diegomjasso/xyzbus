from django.conf.urls import include, url
from .views import edit_password, EditPerfilClass

app_name = 'pasajeros'

urlpatterns = [
	url(r'^edit_password/$', edit_password, name='edit_password'),
	url(r'^edit_perfil/$', EditPerfilClass.as_view(), name='edit_perfil'),
]
