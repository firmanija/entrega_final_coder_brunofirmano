# GAMEFLIX 🎮

Proyecto final desarrollado con **Django**.
GAMEFLIX es una plataforma web inspirada en los **videoclubes clásicos de los años 90**, donde los usuarios pueden explorar videojuegos disponibles, ver planes de suscripción y registrar alquileres.

El objetivo del proyecto es demostrar el uso de Django para construir una aplicación web completa con modelos, vistas, templates, autenticación y CRUD.

---

# Funcionalidades principales

### Catálogo de videojuegos

Los usuarios pueden visualizar una lista de videojuegos disponibles en la plataforma.

También incluye un **formulario de búsqueda por título** para filtrar juegos.

---

### Gestión de planes

El sistema permite crear y administrar **planes de suscripción**, donde cada plan puede tener diferentes precios.

Ejemplo:

* Plan Básico
* Plan Premium
* Plan Ilimitado

---

### Gestión de alquileres

Permite registrar alquileres de videojuegos asociando:

* Usuario
* Juego
* Fecha de alquiler

---

### Autenticación de usuarios

El sistema incluye:

* Login
* Logout
* Registro de usuario

Utilizando el sistema de autenticación integrado de Django.

---

### Panel de administración

Se utiliza el **admin de Django** para gestionar:

* Juegos
* Planes
* Alquileres
* Usuarios

Usuario de prueba:

```
usuario: admin
contraseña: 123
```

---

# Modelos del proyecto

El sistema incluye **3 modelos principales**:

### Game

Representa los videojuegos disponibles.

Campos principales:

* title
* platform
* genre
* price_per_rental
* is_active

---

### Plan

Representa los planes de suscripción del sistema.

Campos principales:

* name
* monthly_price

---

### Rental

Representa el alquiler de un videojuego por parte de un usuario.

Campos principales:

* user
* game
* rental_date

---

# Estructura del proyecto

```
entrega_final_coder_brunofirmano/
│
├── GAMEFLIX/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
│
├── templates/
│   ├── base.html
│   ├── about.html
│   ├── registration/
│   │   ├── login.html
│   │   └── register.html
│   └── GAMEFLIX/
│       ├── game_list.html
│       ├── plan_list.html
│       ├── rental_list.html
│       ├── form.html
│       └── confirm_delete.html
│
├── manage.py
├── requirements.txt
└── db.sqlite3
```

---

# Instalación y ejecución

1. Clonar el repositorio

```
git clone https://github.com/firmanija/entrega_final_coder_brunofirmano.git
```

2. Entrar al proyecto

```
cd entrega_final_coder_brunofirmano
```

3. Crear entorno virtual

```
python -m venv .venv
```

4. Activar entorno virtual

Windows:

```
.venv\Scripts\activate
```

5. Instalar dependencias

```
pip install -r requirements.txt
```

6. Aplicar migraciones

```
python manage.py migrate
```

7. Ejecutar el servidor

```
python manage.py runserver
```

8. Abrir el navegador en

```
http://127.0.0.1:8000
```

---

# Tecnologías utilizadas

* Python
* Django
* SQLite
* HTML (Django Templates)
* Git
* GitHub

---

# Autor

Proyecto realizado por **Bruno Firmano** como entrega final del curso.

Inspirado en los clásicos **videoclubes de los años 90**, donde elegir un juego para el fin de semana era parte de la experiencia.
