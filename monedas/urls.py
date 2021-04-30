from django.urls import path, include
from rest_framework import routers

from monedas import views

router = routers.DefaultRouter()
router.register(r'', views.MonedasViewSet)
router.register(r'materiales', views.MaterialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
