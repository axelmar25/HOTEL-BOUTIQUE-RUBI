from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('habitaciones/', views.habitaciones, name='habitaciones'),
    path('habitaciones/<int:pk>/', views.detalle_habitacion, name='detalle_habitacion'),
    path('contacto/', views.contacto, name='contacto'),
]
