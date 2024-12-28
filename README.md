<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/MatiasMichaux98/BlogDjango/blob/master/static/img/busqueda.png" alt="Busqueda" width="200" height="200" />
  <img src="https://github.com/MatiasMichaux98/BlogDjango/blob/master/static/img/detail.png" alt="Detalle" width="200" height="200" />
  <img src="https://github.com/MatiasMichaux98/BlogDjango/blob/master/static/img/home.png" alt="Home" width="200" height="200" />
  <img src="https://github.com/MatiasMichaux98/BlogDjango/blob/master/static/img/perfil.png" alt="Perfil" width="200" height="200" />
</div>


🖥️ Proyecto Django + PostgreSQL 

Antes de comenzar, asegúrate de tener instalados los siguientes componentes:

[Python >=3.9.x]
PostgreSQL (instalarlo y configurarlo en tu pc )
Instalación clona el repositorio en tu máquina: git clone https://github.com/tu_usuario/tu_proyecto.git

Configurar el entorno virtual para Django

Crear entorno virtual
pip install virtualenv
luego usa venv\Scripts\activate para activar el entorno
Instala las dependencias de Django:
pip install -r requirements.txt
Configurar la base de datos PostgreSQL
Crea el archivo .env en el directorio principal con los datos de tu base de datos PostgreSQL:

DB_NAME=nombre_basedatos
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
Luego crea la base de datos en PostgreSQL:

CREATE DATABASE nombre_basedatos;
Aplicar migraciones
luego en consola dentro del entorno virtual pone los siguientes comandos

python manage.py makemigrations
python manage.py migrate
