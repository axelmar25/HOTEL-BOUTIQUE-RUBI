# 🏨 Hotel Real Palace — Catálogo Digital Django

Sitio web tipo catálogo digital para hotel, construido con Django.

---

## 📁 Estructura del proyecto

```
hotel_catalogo/
├── hotel_catalogo/          # Configuración principal de Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── hotel_app/               # App principal
│   ├── models.py            # Habitaciones, Servicios, Configuración
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       └── hotel_app/
│           ├── base.html        # Layout base (navbar + footer)
│           ├── inicio.html      # Página principal con hero y grid
│           ├── habitaciones.html # Catálogo con filtros
│           ├── detalle_habitacion.html # Detalle + sidebar reserva
│           └── contacto.html    # Página de contacto
├── seed_data.py             # Script para cargar datos de ejemplo
├── manage.py
└── requirements.txt
```

---

## ⚙️ Instalación paso a paso en VS Code

### 1. Abrir en VS Code
```bash
cd hotel_catalogo
code .
```

### 2. Crear entorno virtual
```bash
# En la terminal de VS Code (Ctrl+`)
python -m venv venv

# Activar (Windows)
venv\Scripts\activate

# Activar (Mac/Linux)
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Crear la base de datos
```bash
python manage.py makemigrations hotel_app
python manage.py migrate
```

### 5. Cargar datos de ejemplo
```bash
python seed_data.py
```

### 6. Crear superusuario para el admin
```bash
python manage.py createsuperuser
# Sigue las instrucciones (usuario, email, contraseña)
```

### 7. Ejecutar el servidor
```bash
python manage.py runserver
```

### 8. Abrir en el navegador
- **Sitio web:** http://127.0.0.1:8000/
- **Panel admin:** http://127.0.0.1:8000/admin/

---

## 🎨 Personalización

### Cambiar nombre/datos del hotel
Ve a **Admin → Configuración del Hotel** y edita:
- Nombre del hotel
- Teléfono y WhatsApp
- Email y dirección
- Slogan

### Agregar habitaciones con fotos
1. Ve a **Admin → Habitaciones → Agregar**
2. Llena el formulario
3. Sube la imagen principal
4. Agrega características (amenidades)
5. Agrega imágenes a la galería

### Número de WhatsApp
En **Configuración del Hotel**, el campo "WhatsApp" debe ser el número completo con código de país pero SIN el símbolo `+`:
- México: `5214421234567` (52 + código de área + número)

### Agregar servicios
Ve a **Admin → Servicios** y agrega los que ofrece tu hotel.

---

## 🌟 Páginas incluidas

| Página | URL | Descripción |
|--------|-----|-------------|
| Inicio | `/` | Hero, grid de habitaciones, servicios |
| Habitaciones | `/habitaciones/` | Catálogo con filtros por tipo |
| Detalle | `/habitaciones/<id>/` | Ficha completa + precios + WhatsApp |
| Contacto | `/contacto/` | Canales de comunicación |
| Admin | `/admin/` | Panel de gestión completo |

---

## 📱 Características del diseño

- ✅ Diseño oscuro y elegante (tema gold/negro)
- ✅ Totalmente responsive (móvil, tablet, desktop)
- ✅ Botón flotante de WhatsApp
- ✅ Galería de imágenes por habitación
- ✅ Filtros por tipo de habitación
- ✅ Panel admin para gestionar todo
- ✅ Animaciones suaves en hover
- ✅ Fuentes premium (Playfair Display + Lato)

---

## 🔧 Extensiones recomendadas para VS Code

- **Python** (Microsoft)
- **Django** (Baptiste Darthenay)
- **SQLite Viewer** (Florian Klampfer)
- **Pylance** (Microsoft)
