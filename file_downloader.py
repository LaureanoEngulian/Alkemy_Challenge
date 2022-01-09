import requests
import csv
import os, shutil
from datetime import datetime
from config import *
from logger_base import log

dt = datetime.now()


def download_file(url, filename):
    ''' Downloads file from the url and save it as filename '''
    response = requests.get(url)
    # Check if the response is ok (200)
    if response.status_code == 200:
        # Open file and write the content
        with open(filename, 'wb') as file:
            # A chunk of 128 bytes
            for chunk in response:
                file.write(chunk)


def obtener_archivos_fuente():
    try:
        #OBTENEMOS ARCHIVO DE BIBLIOTECAS POPULARES
        categoria_r = 'bibliotecas_populares'
        path_r = categoria_r + '/' + str(dt.year) + '-' + str(dt.month)
        # VERIFICAMOS QUE EXISTA EL DIRECTORIO
        if not os.path.exists(path_r):
            os.makedirs(path_r)
        #DESCARGAMOS EL ARCHIVO CSV
        filename = path_r + '/' + categoria_r + '-' + str(dt.day) + '-' + str(dt.month) + '-' + str(dt.year) + '.csv'
        url = CSV_BIBLIOTECAS
        download_file(url, filename)

        #OBTENEMOS ARCHIVO DE MUSEOS
        categoria_r = 'museos'
        path_r = categoria_r + '/' + str(dt.year) + '-' + str(dt.month)
        # VERIFICAMOS QUE EXISTA EL DIRECTORIO
        if not os.path.exists(path_r):
            os.makedirs(path_r)
        # DESCARGAMOS EL ARCHIVO CSV
        filename = path_r + '/' + categoria_r + '-' + str(dt.day) + '-' + str(dt.month) + '-' + str(dt.year) + '.csv'
        url = CSV_MUSEOS
        download_file(url, filename)

        # OBTENEMOS ARCHIVO DE SALAS DE CINE
        categoria_r = 'salas_de_cine'
        path_r = categoria_r + '/' + str(dt.year) + '-' + str(dt.month)
        # VERIFICAMOS QUE EXISTA EL DIRECTORIO
        if not os.path.exists(path_r):
            os.makedirs(path_r)
        # DESCARGAMOS EL ARCHIVO CSV
        filename = path_r + '/' + categoria_r + '-' + str(dt.day) + '-' + str(dt.month) + '-' + str(dt.year) + '.csv'
        url = CSV_SALAS_CINE
        download_file(url, filename)
        log.info('Se decargaron los archivos fuente')
    except Exception as e:
        log.error(('Error en la descara de archivos fuente'))




if __name__ == '__main__':
    try:
        obtener_archivos_fuente()
    except Exception as e:
        print(f'Error: {e}')
