# GAMEFLIX 🎮

### Plataforma de alquiler de videojuegos — Proyecto Django

Bienvenido a **GAMEFLIX**.

Este proyecto busca recrear la experiencia de los clásicos **videoclubes de los años 90**, donde uno podía recorrer estanterías llenas de juegos y elegir qué alquilar para el fin de semana.
Inspirado en esa nostalgia, **GAMEFLIX** propone una versión web simple de un sistema de alquiler de videojuegos.

El proyecto fue desarrollado como **entrega final del curso de Django**, cumpliendo con los requisitos de creación de modelos, CRUD, autenticación de usuarios y sistema de búsqueda.

---

# Funcionalidades

El sistema incluye:

* Catálogo de videojuegos
* Búsqueda de juegos por título
* Sistema de planes de alquiler
* Registro de alquileres
* Sistema de autenticación (Login / Logout / Register)
* Panel de administración de Django
* CRUD completo para los modelos principales
* Uso de **herencia de plantillas (base.html)**

---

# Modelos del proyecto

El sistema está compuesto por tres modelos principales:

### Game

Representa un videojuego disponible para alquilar.

Campos principales:

* título
* plataforma
* género
* precio por alquiler
* estado activo

---

### Plan

Representa los distintos planes de suscripción disponibles.

Campos principales:

* nombre del plan
* precio mensual
* estado activo

---

### Rental

Representa un alquiler realizado por un usuario.

Campos principales:

* usuario
* videojuego
* plan
* tipo de alquiler
* fecha de inicio
* fecha de devolución
* estado del alquiler

---

# Secciones principales de la web

| Sección           | URL                   |
| ----------------- | --------------------- |
| Listado de juegos | `/`                   |
| Planes            | `/plans/`             |
| Alquileres        | `/rentals/`           |
| Login             | `/accounts/login/`    |
| Registro          | `/accounts/register/` |
| Panel admin       | `/admin/`             |
| About             | `/about/`             |

---

# Búsqueda de videojuegos

La página principal incluye un formulario que permite **buscar videojuegos por título**.

Ejemplo:

`/?q=mario`

---

# Acceso al panel de administración

Ruta:

`/admin/`

Usuario de prueba:

Usuario
`admin`

Contraseña
`123`

---

# Cómo ejecutar el proyecto

1. Crear entorno virtual

```
python -m venv .venv
```

2. Activar entorno virtual

Windows:

```
.venv\Scripts\activate
```

3. Instalar dependencias

```
pip install django
```

4. Ejecutar migraciones

```
python manage.py migrate
```

5. Iniciar servidor

```
python manage.py runserver
```

Abrir en el navegador:

```
http://127.0.0.1:8000
```

---

# Autor

**Bruno Firmano**

Proyecto realizado como práctica final de Django, inspirado en los videoclubes clásicos de los años 90.
