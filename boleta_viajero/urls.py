"""boleta_viajero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from bearer_auth.views import ObtainToken
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from common.urls import urlpatterns as common_urls
from bitacora.urls import urlpatterns as bitacora_urls
from paises.urls import urlpatterns as paises_urls
from monedas.urls import urlpatterns as monedas_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('common/', include(common_urls)),
    path('auth/token', ObtainToken.as_view()),
    path('api/bitacoras/', include(bitacora_urls)),
    path('api/paises/', include(paises_urls)),
    path('api/monedas/', include(monedas_urls))
]
