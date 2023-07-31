import mysql.connector
import pymysql
from Encrypt_Decrypt import *


IPServidor=('41785A3245774C6D41775232446D4C3441784C335A6D7030')
UsuarioServidor=('416D563245774D54416D443D')
ContrasenaServidor=('4177523244474C6B416D56325A475A355A6D483D')
BaseDatosServidor=('417744325A77706A41484C335A6D4C3141785A3241474D53416D44324147706D416D443D')
def conntDB():
    try:    
        connectionMySQL = pymysql.connect(
            host=DeCrypt(IPServidor),
            user=DeCrypt(UsuarioServidor),
            password=DeCrypt(ContrasenaServidor), 
            db=DeCrypt(BaseDatosServidor), 
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        connectionMySQL.autocommit(True)    
        return connectionMySQL
    except Exception as e:
        print('Sin conexión a la base de datos', e)
        return None  # Devolver None en caso de error para manejarlo fuera de la función

   
def ControlERROR(e):
    connectionMySQL = conntDB()
    try:
        with connectionMySQL.cursor() as cursor:
            # Limpiamos la cadena
            cadena1 = str(e).replace('"','*')
            cadena2 = cadena1.replace("'","*")
            sql2 = "INSERT INTO " + str(DeCrypt(BaseDatosServidor)) + \
                ".tbl_rlog_detalle (LOG_ERROR_LOG, LOG_NAME_BOT) VALUES ('" + str(cadena2) + "', '" + str("ejem") + "');"
            cursor.execute(sql2)
            connectionMySQL.close()
    except:
        print('Error ControlERROR')
        connectionMySQL.close()

