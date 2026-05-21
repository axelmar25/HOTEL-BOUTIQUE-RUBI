from django.db import models

class Habitacion(models.Model):
    TIPO_CHOICES = [
        ('sencilla', 'Sencilla'),
        ('doble', 'Doble'),
        ('suite', 'Suite'),
        ('jacuzzi', 'Jacuzzi'),
        ('presidencial', 'Presidencial'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='sencilla')
    descripcion = models.TextField()
    precio_hora = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    precio_noche = models.DecimalField(max_digits=8, decimal_places=2)
    capacidad = models.IntegerField(default=2)
    disponible = models.BooleanField(default=True)
    imagen_principal = models.ImageField(upload_to='habitaciones/', null=True, blank=True)
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden', 'nombre']
        verbose_name = 'Habitación'
        verbose_name_plural = 'Habitaciones'

    def __str__(self):
        return self.nombre


class CaracteristicaHabitacion(models.Model):
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, related_name='caracteristicas')
    nombre = models.CharField(max_length=100)
    icono = models.CharField(max_length=50, default='✓')

    def __str__(self):
        return f"{self.habitacion.nombre} - {self.nombre}"


class ImagenHabitacion(models.Model):
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='habitaciones/galeria/')
    descripcion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Imagen de {self.habitacion.nombre}"


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    icono = models.CharField(max_length=10, default='★')
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return self.nombre


class ConfiguracionHotel(models.Model):
    nombre_hotel = models.CharField(max_length=200, default='Hotel Real Palace')
    slogan = models.CharField(max_length=300, blank=True)
    telefono = models.CharField(max_length=30, blank=True)
    whatsapp = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    direccion = models.TextField(blank=True)
    descripcion_principal = models.TextField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    logo = models.ImageField(upload_to='config/', null=True, blank=True)

    class Meta:
        verbose_name = 'Configuración del Hotel'
        verbose_name_plural = 'Configuración del Hotel'

    def __str__(self):
        return self.nombre_hotel
