import conexion_db
import data_process
import file_downloader
from logger_base import log

def deploy():
    log.info('Se inicia la ejecución')
    file_downloader.obtener_archivos_fuente()
    data_process.normalizar_datos()
    conexion_db.crear_conexion()
    opcion = None
    while opcion != 7:
        print('Elija su consulta sobre la base de datos:')
        print()
        print('1. Cantidad de registros totales por categoría')
        print('2. Cantidad de registros totales por fuente')
        print('3. Cantidad de registros totales po provincia y categoría')
        print('4. Cantidad de pantallas de cine por provincia')
        print('5. Cantidad de butacas de cine por provincia')
        print('6. Cantidad de Espacios INCAA por provincia')
        print('7. Salir')
        print()
        opcion = int(input('Escribe tu opción(1-7): '))
        if opcion == 1:
            print()
            conexion_db.Consulta1()
            print()
            log.info('Consulta: Cantidad de registros totales por categoría')
        elif opcion == 2:
            print()
            conexion_db.Consulta2()
            print()
            log.info('Consulta: Cantidad de registros totales por fuente')
        elif opcion == 3:
            print()
            conexion_db.Consulta3()
            print()
            log.info('Consulta: Cantidad de registros totales po provincia y categoría')
        elif opcion == 4:
            print()
            conexion_db.Consulta4()
            print()
            log.info('Consulta: Cantidad de pantallas de cine por provincia')
        elif opcion == 5:
            print()
            conexion_db.Consulta5()
            print()
            log.info('Consulta: Cantidad de butacas de cine por provincia')
        elif opcion == 6:
            print()
            conexion_db.Consulta6()
            print()
            log.info('Consulta: Cantidad de Espacios INCAA por provincia')
        else:
            print()
            print('Salimos de la consulta')
            log.info('Finaliza la ejecución')

if __name__ == '__main__':
    try:
        deploy()
        log.info('Se inicia la ejecición')
    except Exception as e:
        print(e)
        log.error('Error al ejecutar el programa')