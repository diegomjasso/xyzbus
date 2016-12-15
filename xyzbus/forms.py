#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

"""
	Constants
"""
ERROR_MESSAGE_USER = {'required' : 'El username es requerido', 'unique' : 'El username ya se encuentra registrado', 'invalid': 'El username es incorrecto' }
ERROR_MESSAGE_PASSWORD = {'required' : 'El password es requerido'}
ERROR_MESSAGE_EMAIL = {'required' : 'El email es requerido', 'invalid': 'Ingrese un correo valido'}

"""
	Classes
"""
class CreateUserForm(forms.ModelForm):
	username = forms.CharField( max_length = 20,  error_messages =  ERROR_MESSAGE_USER  )
	password = forms.CharField( max_length = 20, widget = forms.PasswordInput(), error_messages =  ERROR_MESSAGE_PASSWORD  )
	email = forms.CharField( error_messages =  ERROR_MESSAGE_EMAIL  )

	def __init__(self, *args, **kwargs):
		super(CreateUserForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update( {'id': 'username_create', 'placeholder' : 'username' } )
		self.fields['password'].widget.attrs.update( {'id': 'password_create' , 'placeholder' : 'password' } )
		self.fields['email'].widget.attrs.update( {'id': 'email_create', 'placeholder' : 'email'} )

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email=email).count():
			raise forms.ValidationError('El email debe de ser unico.')
		return email

	class Meta:
		model = User
		fields = ('username', 'password', 'email')

class LoginUserForm(forms.Form):
	username = forms.CharField( max_length = 20)
	password = forms.CharField( max_length = 20, widget = forms.PasswordInput() )

	def __init__(self, *args, **kwargs):
		super(LoginUserForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update( {'id': 'username_login', 'class': '', 'placeholder' : 'username' } )
		self.fields['password'].widget.attrs.update( {'id': 'password_login', 'class': '', 'placeholder' : 'password' } )
