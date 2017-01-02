from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class DashboardClass(LoginRequiredMixin, View):
	login_url = 'login'

	def get(self, request, *args, **kwargs):
		return render( request, 'index.html', {})

#def _index(	request):
#	return	render(	request,	'index.html',	{})
