import mysql.connector
import pymysql
import database as db_module
conexion = db_module.conntDB()

def palabra():
    try:
        with conexion.cursor() as cursor:
            # Consulta SQL para obtener todos los registros de la tabla
            url = "SELECT url_palabra FROM tbl_url WHERE PKurl_id = %s;"
            cursor.execute(url,(1))

            # Obtener los resultados de la consulta
            resultados = cursor.fetchall()
            
            
            
            # Hacer algo con los datos obtenidos
            for resultado in resultados:
                a=resultado['url_palabra']
                #print(resultado)
                #print(a)
        return a
        conexion.close() 

    except Exception as e:
        err = db_module.ControlERROR(e)
        print('Error al obtener datos:', e)
        
def link():
    try:
        with conexion.cursor() as cursor:
            # Consulta SQL para obtener todos los registros de la tabla
            url = "SELECT url_link FROM tbl_url WHERE PKurl_id = %s;"
            cursor.execute(url,(1))

            # Obtener los resultados de la consulta
            resultados = cursor.fetchall()
            
            
            
            # Hacer algo con los datos obtenidos
            for resultado in resultados:
                l=resultado['url_link']
                #print(resultado)
                #print(l)
        return l
        conexion.close() 

    except Exception as e:
        err = db_module.ControlERROR(e)
        print('Error al obtener datos:', e)
        
def control():
    try:
        with conexion.cursor() as cursor:
            # Consulta SQL para obtener todos los registros de la tabla
            url = "SELECT url_control FROM tbl_url WHERE PKurl_id = %s;"
            cursor.execute(url,(1))

            # Obtener los resultados de la consulta
            resultados = cursor.fetchall()
            
            
            
            # Hacer algo con los datos obtenidos
            for resultado in resultados:
                c=resultado['url_control']
                #print(resultado)
                #print(c)
        return c
        conexion.close() 

    except Exception as e:
        err = db_module.ControlERROR(e)
        print('Error al obtener datos:', e)