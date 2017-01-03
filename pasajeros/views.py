from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from .models import Cuentas, Perfil
from .forms import EditAjustesCuentaForm, EditPasswordForm, EditPerfilForm

# Create your views here.
class AjustesCuentaClass(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
	login_url = 'login'
	model = Cuentas
	template_name = 'pasajeros/ajustes_cuenta.html'
	success_url = reverse_lazy('dashboard:dashboard')
	form_class = EditAjustesCuentaForm
	success_message = "Tu cuenta ha sido actualizada exitosamente."

	def get_object(self, queryset = None):
		return self.get_cuenta_instance()

	def get_cuenta_instance(self):
		try:
			return self.request.user.cuentas
		except:
			return Cuentas(user = self.request.user)

class EditPerfilClass(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
	login_url = 'login'
	model = Perfil
	template_name = 'pasajeros/edit_perfil.html'
	success_url = reverse_lazy('dashboard:dashboard')
	form_class = EditPerfilForm
	success_message = "Tu usuarios ha sido actualizado exitosamente."

	def get_object(self, queryset = None):
		return self.get_perfil_instance()

	def get_perfil_instance(self):
		try:
			return self.request.user.perfil
		except:
			return Perfil(user = self.request.user)

"""
Functions
"""
@login_required(login_url = 'login')
def edit_password(request):
	form = EditPasswordForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			current_password = form.cleaned_data['password']
			new_password = form.cleaned_data['new_password']

			if authenticate(username = request.user.username, password = current_password):
				request.user.set_password(  new_password )
				request.user.save()

				update_session_auth_hash( request, request.user )
				messages.success(request, 'Password actualizado correctamente')
			else:
				messages.error(request, 'No es posible actualizar el password')

	context = {'form' : form }
	return render(request, 'pasajeros/edit_password.html', context)
