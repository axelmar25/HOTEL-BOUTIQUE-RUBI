"""
Script para cargar datos de ejemplo.
Ejecutar con: python manage.py shell < seed_data.py
O mejor: python seed_data.py (con el entorno activo y desde la raíz del proyecto)
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_catalogo.settings')
django.setup()

from hotel_app.models import Habitacion, CaracteristicaHabitacion, Servicio, ConfiguracionHotel

print("🏨 Cargando datos de ejemplo...")

# Configuración del hotel
config, _ = ConfiguracionHotel.objects.get_or_create(pk=1)
config.nombre_hotel = "Hotel Real Palace"
config.slogan = "Donde el lujo se encuentra con el confort"
config.telefono = "+52 (442) 123-4567"
config.whatsapp = "524421234567"
config.email = "reservas@hotelrealpalace.mx"
config.direccion = "Blvd. Bernardo Quintana 123, Querétaro, México"
config.descripcion_principal = "Hotel Real Palace ofrece habitaciones de lujo con privacidad garantizada, atención 24 horas y las mejores amenidades para hacer de tu estancia una experiencia inolvidable."
config.save()
print("✅ Configuración guardada")

# Servicios
servicios = [
    ("🔒", "Privacidad Total", "Acceso discreto y privado a cada habitación. Tu visita es completamente confidencial."),
    ("🌙", "Disponible 24/7", "Abierto las 24 horas del día, los 7 días de la semana, incluyendo días festivos."),
    ("❄️", "Aire Acondicionado", "Clima individual en cada habitación para tu máxima comodidad."),
    ("📺", "Smart TV", "Televisión de pantalla grande con canales de cable y streaming."),
    ("🚿", "Baño de Lujo", "Amenidades premium en cada baño. Toallas y artículos de tocador incluidos."),
    ("🍽️", "Room Service", "Servicio a habitaciones disponible para snacks, bebidas y más."),
    ("🅿️", "Estacionamiento", "Estacionamiento privado y seguro sin costo adicional."),
    ("💳", "Múltiples pagos", "Aceptamos efectivo, tarjeta de débito y crédito."),
]

Servicio.objects.all().delete()
for i, (icono, nombre, desc) in enumerate(servicios):
    Servicio.objects.create(icono=icono, nombre=nombre, descripcion=desc, orden=i)

print(f"✅ {len(servicios)} servicios creados")

# Habitaciones
habitaciones_data = [
    {
        "nombre": "Habitación Sencilla Estándar",
        "tipo": "sencilla",
        "descripcion": "Una habitación confortable y acogedora, perfecta para una estancia relajante. Cuenta con cama matrimonial, baño completo y todas las amenidades necesarias para tu comodidad.",
        "precio_hora": 180,
        "precio_noche": 650,
        "capacidad": 2,
        "caracteristicas": [
            ("🛏️", "Cama matrimonial"),
            ("❄️", "Aire acondicionado"),
            ("📺", "TV 40\""),
            ("🚿", "Regadera"),
            ("🔒", "Cerradura electrónica"),
            ("💡", "Iluminación ambiente"),
        ]
    },
    {
        "nombre": "Habitación Doble Ejecutiva",
        "tipo": "doble",
        "descripcion": "Espaciosa habitación doble con diseño contemporáneo. Ideal para parejas que buscan mayor comodidad. Incluye amenidades premium y un ambiente sofisticado.",
        "precio_hora": 250,
        "precio_noche": 850,
        "capacidad": 2,
        "caracteristicas": [
            ("🛏️", "Cama king size"),
            ("❄️", "Clima individual"),
            ("📺", "Smart TV 50\""),
            ("🛁", "Tina de baño"),
            ("🔒", "Acceso privado"),
            ("🪞", "Espejo de cuerpo completo"),
        ]
    },
    {
        "nombre": "Suite de Lujo",
        "tipo": "suite",
        "descripcion": "Nuestra Suite de Lujo ofrece un nivel superior de comodidad y elegancia. Amplio espacio con sala de estar separada, decoración premium y vistas privilegiadas.",
        "precio_hora": 380,
        "precio_noche": 1200,
        "capacidad": 2,
        "caracteristicas": [
            ("🛏️", "Cama super king"),
            ("🛋️", "Sala de estar"),
            ("❄️", "Climatización premium"),
            ("📺", "Smart TV 65\""),
            ("🛁", "Tina de hidromasaje"),
            ("🍾", "Botella de vino cortesía"),
        ]
    },
    {
        "nombre": "Suite con Jacuzzi",
        "tipo": "jacuzzi",
        "descripcion": "Experiencia única con jacuzzi privado dentro de la habitación. La combinación perfecta de romance y relax. Ideal para celebraciones especiales y momentos inolvidables.",
        "precio_hora": 420,
        "precio_noche": 1450,
        "capacidad": 2,
        "caracteristicas": [
            ("🛏️", "Cama king size"),
            ("🛁", "Jacuzzi privado"),
            ("❄️", "Clima doble zona"),
            ("📺", "Smart TV 55\""),
            ("🕯️", "Decoración romántica"),
            ("🫧", "Sales de baño incluidas"),
        ]
    },
    {
        "nombre": "Suite Presidencial",
        "tipo": "presidencial",
        "descripcion": "La experiencia más exclusiva de nuestro hotel. La Suite Presidencial ofrece el máximo nivel de lujo con jacuzzi, sala privada, decoración de diseñador y servicio personalizado.",
        "precio_hora": None,
        "precio_noche": 2200,
        "capacidad": 2,
        "caracteristicas": [
            ("👑", "Decoración presidencial"),
            ("🛁", "Jacuzzi + tina romana"),
            ("🛋️", "Sala privada"),
            ("📺", "Dos Smart TV"),
            ("🍾", "Champagne cortesía"),
            ("🌹", "Decoración romántica"),
            ("🍽️", "Room service exclusivo"),
            ("🔒", "Máxima privacidad"),
        ]
    },
    {
        "nombre": "Junior Suite Romántica",
        "tipo": "suite",
        "descripcion": "Diseñada especialmente para parejas que buscan una experiencia romántica. Ambiente cálido con iluminación especial, pétalos de rosa y detalles únicos que hacen la diferencia.",
        "precio_hora": 320,
        "precio_noche": 980,
        "capacidad": 2,
        "caracteristicas": [
            ("🛏️", "Cama king con dosel"),
            ("🌹", "Pétalos de rosa"),
            ("🕯️", "Velas aromáticas"),
            ("❄️", "Clima individual"),
            ("📺", "Smart TV 50\""),
            ("🍫", "Chocolates incluidos"),
        ]
    },
]

Habitacion.objects.all().delete()
for i, data in enumerate(habitaciones_data):
    caract = data.pop("caracteristicas")
    data["orden"] = i
    hab = Habitacion.objects.create(**data)
    for icono, nombre in caract:
        CaracteristicaHabitacion.objects.create(habitacion=hab, nombre=nombre, icono=icono)

print(f"✅ {len(habitaciones_data)} habitaciones creadas")
print()
print("🎉 ¡Datos cargados exitosamente!")
print()
print("Accede al admin en: http://127.0.0.1:8000/admin/")
print("Usuario admin: admin / password (créalo con: python manage.py createsuperuser)")
