from sqlalchemy import create_engine
from sqlalchemy.types import Integer, String, DateTime
import pandas as pd
from config import Conexion
from logger_base import log

# CONEXIÓN CON POSTGRES Y SQLALCHEMY
engine = create_engine(
    f'postgresql+psycopg2://{Conexion.USERNAME}:{Conexion.PASSWORD}@{Conexion.DB_HOST}:{Conexion.DB_PORT}/{Conexion.DB_NAME}')

def crear_conexion():
    # ENVÍO Y ACTUALIZACIÓN DE LA BASE DE DATOS
    try:
        # BASE DE DATOS CUNJUNTA
        df = pd.read_csv('df_conjunto.csv')
        df.to_sql('bd_integrada', con=engine, if_exists='replace', index=False, dtype={
            'cod_localidad': String,
            'id_provincia': String,
            'id_departamento': String,
            'categoría': String,
            'provincia': String,
            'localidad': String,
            'nombre': String,
            'domicilio': String,
            'código postal': String,
            'número de teléfono': String,
            'mail': String,
            'web': String,
            'fuente': String,
            'fecha_mod': DateTime
        })
        # BASE DE DATOS CINES
        df_cine = pd.read_csv('df_cines.csv')
        df_cine.to_sql('bd_cines', con=engine, if_exists='replace', index=False, dtype={
            'provincia': String,
            'pantallas': Integer,
            'butacas': Integer,
            'espacios INCAA': String
        })
        log.info('Se actualizó la base de datos correctamente')
    except Exception as e:
        print(e)
        log.error('No se pudo actualizar la base de datos')

#CONSULTAS A LA BASE DE DATOS CON SQLALCHEMY
def Consulta1():
    print('Cantidad de registros totales por categoría:')
    con = engine.connect()
    rs = con.execute("SELECT categoría, COUNT(*) as total FROM bd_integrada GROUP BY categoría")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
    print(df)
    con.close()

def Consulta2():
    print('Cantidad de registros totales por fuente:')
    con = engine.connect()
    rs = con.execute("SELECT fuente, COUNT(*) as total FROM bd_integrada GROUP BY fuente")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
    print(df)
    con.close()

def Consulta3():
    print('Cantidad de registros por provincia y categoría:')
    con = engine.connect()
    rs = con.execute("SELECT provincia, categoría, COUNT(*) as total FROM bd_integrada GROUP BY provincia, categoría order by provincia")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
    pd.set_option('display.max_rows', None,'display.max_columns', None,'display.width', None,'display.max_colwidth', -1)
    print(df)
    con.close()

def Consulta4():
    print('Cantidad de pantallas de cine por provincia:')
    con = engine.connect()
    rs = con.execute("SELECT provincia, SUM (pantallas) as total_pantallas FROM bd_cines GROUP BY provincia order by provincia")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
    print(df)
    con.close()

def Consulta5():
    print('Cantidad de butacas de cine por provincia:')
    con = engine.connect()
    rs = con.execute("SELECT provincia, SUM (butacas) as total_butacas FROM bd_cines GROUP BY provincia order by provincia")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
    print(df)
    con.close()

def Consulta6():
    print('Cantidad de Espacios INCAA por provincia:')
    con = engine.connect()
    rs = con.execute("select provincia , count('espacios INCAA') as total_esp_INCAA from bd_cines where \"espacios INCAA\"!='0' group by provincia, \"espacios INCAA\" order by provincia")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
    print(df)
    con.close()


if __name__ == '__main__':
    crear_conexion()
