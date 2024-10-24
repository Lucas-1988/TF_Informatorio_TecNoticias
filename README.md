🤖 TecNoticias - Blog de Noticias  
Este es un blog de noticias dedicado a ciberseguridad, creado con **Django**.

**INFORMATORIO - 1° COHORTE 2024 - ETAPA 2 | COMISIÓN 6 - GRUPO 7:
INTEGRANTES:**

* Leonczyk, Lucas

* Czajka, Brian Alexander

* Jara,  Alejandro David

* Drocezesky , Clara Denise

* Mandziuk., Rosana Marcela


Profesor: Vargas, Diego

Mentor: Hiebl, Darian

---

**Índice**  
- [Descripción](#Descripción)  
- [Funcionalidades](#Funcionalidades)
- [Diseño de interfaz](#Diseño-de-interfaz) 
- [Instalación](#Instalación)  
- [Uso](#Uso)  
- [Capturas de Pantalla](#Capturas-de-Pantalla)  
- [Tecnologías](#Tecnologías)  
- [Requisitos](#Contacto)   

---

**Descripción**  
El blog permite que los usuarios lean, publiquen y comenten sobre noticias sobre ciberseguridad. Además, los usuarios autenticados con permisos de **staff** pueden crear, modificar y eliminar publicaciones.  

---

**Funcionalidades**  
- Registro e inicio de sesión de usuarios. 
- Roles de usuario: Administrador, Colaborador y Registrado.  
- Creación, edición y eliminación de publicaciones para usuarios con permisos de staff  
- Sistema de comentarios en las publicaciones.
- Interfaz utilizando HTML, CSS.
- Mappeo de URLs para la navegación interna.
- Integración con redes sociales

---

**Instalación**  
Sigue estos pasos para instalar y ejecutar el proyecto en tu máquina local:

1. **Clonar el repositorio:**
   ```bash
   git clone <URL-del-repositorio>
   cd <nombre-del-repositorio>
   ```

2. **Crear y activar un entorno virtual:**
   ```bash
   python -m venv entorno
   cd/entorno/Scripts/activate  
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar migraciones:**
   ```bash
   python manage.py migrate
   ```

5. **Ejecutar el servidor:**
   ```bash
   python manage.py runserver
   ```

---

**Uso**  
1. Accede a `https://tecnoticias.pythonanywhere.com/` en tu navegador.  
2. Regístrate e inicia sesión para agregar comentarios.  
3. Los administradores o usuarios con permisos de staff podrán gestionar las publicaciones.  

---

**Capturas de la interfaz**  
- ![Página principal](/blog/media/media/tecnoticias.home.png)
- ![Noticia individual](/blog/media/media/tecnoticias.noticia_individual.png)
- ![Inicio de sesión](/blog/media/media/tecnoticias_login.png)
- ![Registro](/blog/media/media/tecnoticias_registro_.png)
- ![Contacto](blog/media/media/tecnoticias_contacto_.png)

---

**Tecnologías**  
- **Django (Backend)** 
- **Python (Lógica del servidor)** 
- **HTML/CSS/JavaScript (Frontend)** 
- **SQLite (Base de datos)** 
- **PythonAnywhere** 
- **Control de versiones:** Git
- **Figma (Diseño de interfaz)**

---

**Requisitos**  
- **asgiref==3.8.1** 
- **Python 3.12.4** 
- **Django 5.1.1** 
- **pillow==10.4.0** 
- **sqlparse==0.5.1**
- **tzdata==2024.1**
