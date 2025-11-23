# CloudContacts

Aplicación web para registrar y listar contactos en la nube, desarrollada con Flask y MySQL. La aplicación es completamente responsiva gracias a TailwindCSS y está preparada para producción con Gunicorn y Systemd.

---

## Índice

1. [Arquitectura](#arquitectura)
2. [Estructura de carpetas](#estructura-de-carpetas)
3. [Requisitos](#requisitos)
4. [Configuración de entorno](#configuración-de-entorno)
5. [Instalación y ejecución](#instalación-y-ejecución)
6. [Seguridad de credenciales](#seguridad-de-credenciales)
7. [Grupos de seguridad en AWS](#grupos-de-seguridad-en-aws)
8. [Comandos útiles](#comandos-útiles)
9. [Licencia](#licencia)

---

## Arquitectura

- **EC2-WEB**: instancia que ejecuta la aplicación Flask con Gunicorn.
- **EC2-DB**: instancia que aloja la base de datos MySQL.
- La aplicación se conecta a MySQL usando la IP privada de la EC2-DB.
- Se utiliza una IP elástica para la EC2-WEB, de modo que la aplicación sea accesible de forma constante desde Internet.

CloudContacts/
│
├─ app.py # Archivo principal de Flask
├─ requirements.txt # Dependencias de Python
├─ .gitignore # Ignora venv, .env y archivos sensibles
├─ .env.example # Variables de entorno de ejemplo
├─ templates/
│ ├─ index.html # Formulario de registro
│ └─ contacts.html # Lista de contactos
└─ static/ # Archivos estáticos (CSS, JS, imágenes)

## Requisitos

- Python 3.10+
- pip
- MySQL 8+
- Gunicorn
- TailwindCSS (CDN incluido en HTML)
- AWS EC2 con Linux (Ubuntu recomendado)

---

## Configuración de entorno

1. Copia el archivo de ejemplo `.env.example` a `.env`:

```bash
cp .env.example .env

Edita .env con tus credenciales de MySQL y la IP privada de tu EC2-DB:

DB_HOST=172.31.xx.xx   # IP privada EC2-DB
DB_USER=usuario_mysql
DB_PASS=contraseña
DB_NAME=cloudcontacts

Crear y activar el entorno virtual:

python3 -m venv venv
source venv/bin/activate


Instalar dependencias:

pip install -r requirements.txt


Ejecutar la aplicación localmente (desarrollo):

python app.py


Para producción, usar Gunicorn y Systemd:

sudo systemctl daemon-reload
sudo systemctl enable cloudcontacts
sudo systemctl start cloudcontacts
sudo systemctl status cloudcontacts

Grupos de seguridad en AWS

EC2-WEB

Puerto 22 (SSH) abierto a tu IP

Puerto 80 (HTTP) abierto a Internet

Puerto 8000 abierto a Internet

EC2-DB

Puerto 3306 (MySQL) solo accesible desde la EC2-WEB (regla de origen: IP privada EC2-WEB)

## Instalación y ejecución

1. Clonar el repositorio:

```bash
git clone https://github.com/aynara-NolazcoYs/CloudContacts.git
cd CloudContacts
Crear y activar el entorno virtual:

bash
Copiar código
python3 -m venv venv
source venv/bin/activate
Instalar dependencias:

bash
Copiar código
pip install -r requirements.txt
Configurar variables de entorno
Copiar el archivo de ejemplo .env.example a .env y llenar los datos correspondientes (IP privada de la EC2-DB, usuario y contraseña de MySQL).

bash
Copiar código
cp .env.example .env
nano .env
Ejecutar la aplicación

Modo desarrollo (opcional, solo para pruebas locales en la EC2-WEB):

bash
Copiar código
python app.py
Producción 

La aplicación se servirá automáticamente en la IP elástica pública asignada a la EC2-WEB
http://98.89.102.120:8000/
