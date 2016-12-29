"""xyzbus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Exampl-es:
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
from jet.dashboard.dashboard_modules import google_analytics_views
from django.conf import settings
from django.conf.urls import url,	include
from django.conf.urls.static import static
from django.contrib import admin
from .views import CreateUserClass, error_404, home, LoginClass, logout

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^$', home, name='home'),
    url(r'^dashboard/',	include('dashboard.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^new_user/$', CreateUserClass.as_view(), name = 'new_user'),
    url(r'^login/$', LoginClass.as_view(), name = 'login'),
    url(r'^logout/$', logout, name = 'logout'),
    url(r'^api/', include('xyzbus.urls_api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

handler404 = error_404

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
