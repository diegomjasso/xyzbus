#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

class LoginUserForm(forms.Form):
	username = forms.CharField( max_length = 20)
	password = forms.CharField( max_length = 20, widget = forms.PasswordInput() )

	def __init__(self, *args, **kwargs):
		super(LoginUserForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update( {'id': 'username_login', 'class': '', 'placeholder' : 'username' } )
		self.fields['password'].widget.attrs.update( {'id': 'password_login', 'class': '', 'placeholder' : 'password' } )
