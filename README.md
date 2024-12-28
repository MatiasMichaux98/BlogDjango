<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/MatiasMichaux98/BlogDjango/blob/master/static/img/busqueda.png" alt="Busqueda" width="200" height="200" />
  <img src="https://github.com/MatiasMichaux98/BlogDjango/blob/master/static/img/detail.png" alt="Detalle" width="200" height="200" />
  <img src="https://github.com/MatiasMichaux98/BlogDjango/blob/master/static/img/home.png" alt="Home" width="200" height="200" />
  <img src="https://github.com/MatiasMichaux98/BlogDjango/blob/master/static/img/perfil.png" alt="Perfil" width="200" height="200" />
</div>


# 🖥️ Proyecto Django + PostgreSQL <br>

Antes de comenzar, asegúrate de tener instalados los siguientes componentes: <br>

[Python >=3.9.x] <br>
PostgreSQL (instalarlo y configurarlo en tu pc ) <br>
Instalación clona el repositorio en tu máquina: git clone https://github.com/tu_usuario/tu_proyecto.git <br>

# Configurar el entorno virtual para Django
Crear entorno virtual <br>
pip install virtualenv <br>
luego usa venv\Scripts\activate para activar el entorno <br> 
Instala las dependencias de Django: <br>
pip install -r requirements.txt <br>
# Configurar la base de datos PostgreSQL
Crea el archivo .env en el directorio principal con los datos de tu base de datos PostgreSQL:

DB_NAME=nombre_basedatos <br>
DB_USER=tu_usuario<br>
DB_PASSWORD=tu_contraseña <br>
DB_HOST=localhost <br>
DB_PORT=5432 <br>
# Luego crea la base de datos en PostgreSQL:

CREATE DATABASE nombre_basedatos; <br>
Aplicar migraciones <br>
# luego en consola dentro del entorno virtual pone los siguientes comandos <br>

python manage.py makemigrations <br>
python manage.py migrate <br>
