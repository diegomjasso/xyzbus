#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from .models import Cuentas, Perfil

"""
Constants
"""
ERROR_MESSAGE_USER = {'required' : 'El username es requerido', 'unique' : 'El username ya se encuentra registrado', 'invalid': 'El username es incorrecto' }
ERROR_MESSAGE_PASSWORD = {'required' : 'El password es requerido'} 
ERROR_MESSAGE_EMAIL = {'required' : 'El email es requerido', 'invalid': 'Ingrese un correo valido'}

"""
Functions
"""

def must_be_gt(value_password):
	if len(value_password) < 2:
		raise forms.ValidationError('El password debe contener por lo menos 5 caracteres.')

"""
Classes
"""
class EditAjustesCuentaForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(EditAjustesCuentaForm, self).__init__(*args, **kwargs)
		self.fields['tipo_tarjeta'].widget.attrs.update( {'class': 'ui selection dropdown', } )

	class Meta:
		model = Cuentas
		exclude = ['user']

class EditPerfilForm(forms.ModelForm):
	class Meta:
		model = Perfil
		exclude = ['user']

class EditPasswordForm(forms.Form):
	password = forms.CharField( max_length = 20, widget = forms.PasswordInput() )
	new_password = forms.CharField(max_length = 20,label = "Nueva password", widget = forms.PasswordInput(), validators = [must_be_gt]  )
	repeat_password = forms.CharField(max_length = 20,label = "Repetir nueva password", widget = forms.PasswordInput(),  validators = [must_be_gt])

	def clean(self):
		clean_data = super(EditPasswordForm,self).clean()
		password1 = clean_data.get('new_password')
		password2 = clean_data.get('repeat_password')

		if password1 != password2:
			raise forms.ValidationError('Los password no son los mismos')

			