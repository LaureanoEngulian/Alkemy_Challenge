# Alkemy_Challenge

IMPORTANTE. LEER PARA CONFIGURAR CORRECTAMENTE EL PROYECTO

## Instalación

Usar el administrador de paquetes [pip](https://pip.pypa.io/en/stable/) para instalar las librerías necesarias.

```bash
pip install pandas #Pandas
pip install sqlalchemy #Sqlalchemy
pip install psycopg2 #Postgresql

```
## Configuración URL
Dentro del archivo config.py realizar la configuración de las URL de descarga de los archivos csv.

```bash
CSV_BIBLIOTECAS = 'URL de Bibliotecas'
CSV_MUSEOS = 'URL de Museos'
CSV_SALAS_CINE = 'URL de Salas de Cine'

```
## Configuración ENV
Dentro del archivo env.example realizar la configuración del acceso a la base de datos y modificar el nombre del archivo a .env
```bash
_USERNAME = 'usuario'
PASSWORD = 'contraseña'
DB_HOST = 'host'
DB_PORT = 'puerto'
DB_NAME = 'nombre de la base de datos'
```


## Uso
Ejecutar el archivo alkemy_challenge.py. Se deplegará el menú de consultas.
