"""xyzbus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url,	include
from django.conf.urls.static import static
from django.contrib import admin
from .views import CreateUserClass, error_404, home, LoginClass, logout


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^dashboard/',	include('dashboard.urls')),
    url(r'^admin/',	admin.site.urls),
    url(r'^new_user/$', CreateUserClass.as_view(), name = 'new_user'),
    url(r'^login/$', LoginClass.as_view(), name = 'login'),
    url(r'^logout/$', logout, name = 'logout'),

]

handler404 = error_404

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
