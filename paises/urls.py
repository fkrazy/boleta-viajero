from django.urls import path, include
from rest_framework import routers

from paises import views

router = routers.DefaultRouter()
router.register(r'', views.PaisesViewSet)
router.register(r'aduanas', views.AduanasViewSet)
router.register(r'republicas', views.RepublicasViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
