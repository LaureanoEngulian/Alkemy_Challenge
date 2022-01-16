from decouple import config
#LINK DE DESCARGA DE ARCHIVOS FUENTE
CSV_BIBLIOTECAS = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'
CSV_MUSEOS = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos.csv'
CSV_SALAS_CINE = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'

#CONFIGURACIÓN DE LA CONEXIÓN A LA BASE DE DATOS
class Conexion:
    _USERNAME = config('_USERNAME')
    PASSWORD = config('PASSWORD')
    DB_HOST = config('DB_HOST')
    DB_PORT = config('DB_PORT')
    DB_NAME = config('DB_NAME')