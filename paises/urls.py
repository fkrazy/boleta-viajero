from django.urls import path, include
from rest_framework import routers

from paises import views

router = routers.DefaultRouter()
router.register(r'', views.PaisesViewSet.as_view())
router.register(r'aduanas', views.AduanasViewSet.as_view())
router.register(r'republicas', views.RepublicasViewSet.as_view())

urlpatterns = [
    path('', include(router.urls)),
]
