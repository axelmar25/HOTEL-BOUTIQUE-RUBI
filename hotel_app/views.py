from django.shortcuts import render, get_object_or_404
from .models import Habitacion, Servicio, ConfiguracionHotel


def get_config():
    config, _ = ConfiguracionHotel.objects.get_or_create(pk=1, defaults={
        'nombre_hotel': 'Hotel Real Palace',
        'slogan': 'Donde el lujo se encuentra con el confort',
        'telefono': '+52 (442) 000-0000',
        'whatsapp': '524420000000',
        'email': 'info@hotelrealpalace.mx',
        'direccion': 'Querétaro, México',
        'descripcion_principal': 'Bienvenido a una experiencia única de descanso y confort.'
    })
    return config


def inicio(request):
    habitaciones = Habitacion.objects.filter(disponible=True)[:6]
    servicios = Servicio.objects.all()
    config = get_config()
    return render(request, 'hotel_app/inicio.html', {
        'habitaciones': habitaciones,
        'servicios': servicios,
        'config': config,
    })


def habitaciones(request):
    tipo = request.GET.get('tipo', '')
    todas = Habitacion.objects.filter(disponible=True)
    if tipo:
        todas = todas.filter(tipo=tipo)
    config = get_config()
    return render(request, 'hotel_app/habitaciones.html', {
        'habitaciones': todas,
        'tipo_seleccionado': tipo,
        'config': config,
    })


def detalle_habitacion(request, pk):
    habitacion = get_object_or_404(Habitacion, pk=pk, disponible=True)
    relacionadas = Habitacion.objects.filter(disponible=True).exclude(pk=pk)[:3]
    config = get_config()
    return render(request, 'hotel_app/detalle_habitacion.html', {
        'habitacion': habitacion,
        'relacionadas': relacionadas,
        'config': config,
    })


def contacto(request):
    config = get_config()
    return render(request, 'hotel_app/contacto.html', {'config': config})
