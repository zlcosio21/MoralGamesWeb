from django.urls import path, include
from carrito import views
from django.conf import settings

urlpatterns = [

    path('carrito/<str:videojuego>/', views.carrito, name="carrito"),
        
]