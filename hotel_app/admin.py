from django.contrib import admin
from .models import Habitacion, CaracteristicaHabitacion, ImagenHabitacion, Servicio, ConfiguracionHotel


class CaracteristicaInline(admin.TabularInline):
    model = CaracteristicaHabitacion
    extra = 3


class ImagenInline(admin.TabularInline):
    model = ImagenHabitacion
    extra = 2


@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo', 'precio_noche', 'disponible', 'orden']
    list_editable = ['disponible', 'orden']
    list_filter = ['tipo', 'disponible']
    inlines = [CaracteristicaInline, ImagenInline]


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'orden']
    list_editable = ['orden']


@admin.register(ConfiguracionHotel)
class ConfiguracionAdmin(admin.ModelAdmin):
    pass
