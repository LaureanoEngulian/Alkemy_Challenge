import pandas as pd
from datetime import datetime
from logger_base import log

dt = datetime.now()

def normalizar_datos():
    try:
        # NORMALIZAR DATOS BIBLIOTECAS
        df_bibliotecas = pd.read_csv('bibliotecas_populares/' + str(dt.year) + '-' + str(dt.month) + '/bibliotecas_populares-' +
                                     str(dt.day) + '-' + str(dt.month) + '-' + str(dt.year) + '.csv', sep=',', quotechar='"',
                                     encoding='utf-8')

        df_bibliotecas1 = df_bibliotecas[['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Categoría',
                                          'Provincia', 'Localidad', 'Nombre', 'Domicilio', 'CP', 'Teléfono', 'Mail', 'Web',
                                          'Fuente']]

        df_bibliotecas1.rename({'Cod_Loc': 'cod_localidad', 'IdProvincia': 'id_provincia', 'IdDepartamento': 'id_departamento',
                                'Categoría': 'categoría',
                                'Provincia': 'provincia', 'Localidad': 'localidad', 'Nombre': 'nombre',
                                'Domicilio': 'domicilio', 'CP': 'código postal', 'Teléfono': 'número de teléfono',
                                'Mail': 'mail', 'Web': 'web',
                                'Fuente': 'fuente'}, axis='columns', inplace=True)

        # NORMALIZAR DATOS SALAS DE CINE
        df_salas_de_cine = pd.read_csv(
            'salas_de_cine/' + str(dt.year) + '-' + str(dt.month) + '/salas_de_cine-' + str(dt.day) + '-' + str(
                dt.month) + '-' + str(dt.year) + '.csv', sep=',', quotechar='"', encoding='utf-8')

        df_salas_de_cine1 = df_salas_de_cine[['Cod_Loc', 'IdProvincia', 'IdDepartamento',
                                              'Categoría', 'Provincia', 'Localidad', 'Nombre',
                                              'Dirección', 'CP', 'Teléfono', 'Mail', 'Web',
                                              'Fuente']]
        df_salas_de_cine1.rename(
            {'Cod_Loc': 'cod_localidad', 'IdProvincia': 'id_provincia', 'IdDepartamento': 'id_departamento',
             'Categoría': 'categoría', 'Provincia': 'provincia', 'Localidad': 'localidad', 'Nombre': 'nombre',
             'Dirección': 'domicilio', 'CP': 'código postal', 'Teléfono': 'número de teléfono', 'Mail': 'mail',
             'Web': 'web', 'Fuente': 'fuente'}, axis='columns', inplace=True)

        # NORMALIZAR DATOS MUSEOS
        df_museos = pd.read_csv(
            'museos/' + str(dt.year) + '-' + str(dt.month) + '/museos-' + str(dt.day) + '-' + str(dt.month) + '-' + str(
                dt.year) + '.csv',
            sep=',', quotechar='"', index_col=[0], encoding='ISO-8859-1')

        df_museos1 = df_museos[['provincia_id', 'localidad_id', 'provincia', 'localidad',
                                'nombre', 'direccion', 'codigo_postal', 'telefono', 'mail', 'web', 'fuente']]

        df_museos1 = df_museos1.assign(categoría='Museos')
        df_museos1.rename({'localidad_id': 'cod_localidad',
                           'provincia_id': 'id_provincia',
                           'provincia': 'provincia',
                           'localidad': 'localidad',
                           'nombre': 'nombre',
                           'direccion': 'domicilio',
                           'codigo_postal': 'código postal',
                           'telefono': 'número de teléfono',
                           'mail': 'mail',
                           'web': 'web',
                           'fuente': 'fuente'}, axis='columns', inplace=True)

        # CREACION BASE DE DATOS CINES
        df_salas_de_cine2 = df_salas_de_cine[['Provincia', 'Pantallas', 'Butacas', 'espacio_INCAA']]
        df_salas_de_cine2.rename(
            {'Provincia': 'provincia', 'Pantallas': 'pantallas', 'Butacas': 'butacas', 'espacio_INCAA': 'espacios INCAA'},
            axis='columns', inplace=True)
        df_salas_de_cine2.to_csv('df_cines.csv', sep=',', index=False, encoding='utf-8')

        # CREACION BASE DE DATOS CONJUNTA
        df_conjunto = pd.concat([df_bibliotecas1, df_salas_de_cine1, df_museos1])
        df_conjunto = df_conjunto.assign(fecha_mod=dt)
        df_conjunto.to_csv('df_conjunto.csv', sep=',', quotechar='"', index=False, encoding='utf-8')
        log.info('Los datos se procesaron correctamente')
    except Exception as e:
        log.error('Error al procesar los archivos fuente')

if __name__ == '__main__':
    normalizar_datos()