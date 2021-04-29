from django.urls import path, include
from rest_framework import routers

from bitacora import views

router = routers.DefaultRouter()
router.register(r'', views.BitacoraViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
