from selenium import webdriver
from selenium.webdriver.chrome.service import service
#acciones de teclado
from selenium.webdriver.common.keys import Keys
#permite utilizar los localizadores de elementos
from selenium.webdriver.common.by import By
#permite esperar de forma explícita hasta que ciertas condiciones se cumplan
from selenium.webdriver.support.ui import WebDriverWait
#proporciona diferentes condiciones enlazada a WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import os
from selenium.common.exceptions import NoSuchElementException
import time
from Encrypt_Decrypt import *
import buscarsql as buscar
import database as db_module
import subprocess
conexion = db_module.conntDB()

dir_path = os.path.dirname(os.path.realpath(__file__))
chrome_driver_path = os.path.join(dir_path, 'chromedriver.exe')
chrome_driver_path_service = Service(chrome_driver_path)
driver = webdriver.Chrome(service= chrome_driver_path_service)


control=buscar.control().upper()
if control =="TRUE":
    link=buscar.link()
    driver.get(link)

    buscador = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
    p=buscar.palabra()
    
    buscador.send_keys(p)
    buscador.send_keys(Keys.RETURN)

    time.sleep(5)
    wikipedia=driver.find_element(By.PARTIAL_LINK_TEXT, "wikipedia")
    wikipedia.send_keys(Keys.RETURN)
    time.sleep(5)
    palabra =p.upper()
    #print(palabra)

    if palabra =="SELENIUM":
        
        def boot_auto_recuperable():
            # Intentos máximos para recuperarse si ocurre un error
            max_intentos = 3

            intento_actual = 1
            while intento_actual <= max_intentos:
                try:
                    
                    Titles = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "firstHeading")))
                    Intros = driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/p[1]')
                    Historias = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[2]')))
                    xpaths = [
                        '//*[@id="mw-content-text"]/div[1]/p[3]',
                        '//*[@id="mw-content-text"]/div[1]/p[4]',
                        '//*[@id="mw-content-text"]/div[1]/p[5]',
                        '//*[@id="mw-content-text"]/div[1]/p[6]',
                        '//*[@id="mw-content-text"]/div[1]/ul[1]',
                    ]
                    #limpiar texto
                    texto_titles = Titles.text
                    texto_intros = Intros.text
                    texto_historias = Historias.text

                    Title = Encrypt(texto_titles.replace("'", "&#39;"))
                    Intro = texto_intros.replace("'", "&#39;")
                    Historia= texto_historias.replace("'", "&#39;")

                    componentes = [driver.find_element(By.XPATH, xpath).text for xpath in xpaths]

                    # Imprimir el contenido 
                    #print(f"{Title}\n\n{Intro}\n\n{Historia}\n\n")

                    for componente in componentes:
                        texto_datos = componente
                        Datos = texto_datos.replace("'", "&#39;")
                        #print(Datos)
                        


                    if conexion:
                        try:
                            # Obtener el cursor a partir de la conexión
                            cursor = conexion.cursor()
                            

                            # Datos a insertar 
                            WIKI_TITLE = {Title}
                            WIKI_INTRO = {Intro}
                            WIKI_HISTORY = {Historia}
                            WIKI_COMPONENTS = {Datos}

                        
                            consulta = "INSERT INTO tbl_datoswiki (WIKI_CTITLE, WIKI_CINTRO, WIKI_CHISTORY, WIKI_CCOMPONENTS) VALUES (%s, %s, %s, %s)"
                            datos_wiki = (WIKI_TITLE, WIKI_INTRO, WIKI_HISTORY, WIKI_COMPONENTS)

                            # Ejecuta la consulta 
                            cursor.execute(consulta, datos_wiki)

                            # Confirma los cambios en la base de datos
                            conexion.commit()

                            print("Datos insertados correctamente en la tabla tbl_datoswiki.")

                        except db_module.pymysql.Error as error:
                            # Si ocurre algún error, deshacemos los cambios
                            conexion.rollback()
                            print(f"Error al insertar datos en la tabla: {error}")
                            
                            
                        finally:
                            # Cerrar el cursor y la conexión cuando ya no se necesiten
                            cursor.close()
                            conexion.close()  
                    
                    
                    
                    break

                except NoSuchElementException as e:
                    # En caso de que no se encuentre el elemento, muestra el error y espera un tiempo antes de intentar nuevamente
                    print(f"Error: No se encontró el elemento. Intento {intento_actual}/{max_intentos}")
                    print(f"Mensaje de error: {e} aqui termina el error")
                    
                    mensaje_error = str(e)
                    lineas = mensaje_error.splitlines()
                    primer_linea = '\n'.join(lineas[:1])
                    x=db_module.ControlERROR(primer_linea)
                    
                    intento_actual += 1
                    time.sleep(5)  # Espera 5 segundos antes de intentar nuevamente

            # Cerrar el navegador al finalizar
            driver.quit()

            # Si se agotan los intentos y no se encuentra el elemento, mostrar un mensaje de error final
            if intento_actual > max_intentos:
                print("No se pudo encontrar el elemento después de varios intentos. El script ha terminado.")
                
        if __name__ == "__main__":
            boot_auto_recuperable()

        #conexion.close() 
    else:
        print("no se guardará nada en la base de datos")
        #conexion.close() 
        
elif control =="FALSE":
    print("NO SE ACTIVARÁ EL BOOT")
    #conexion.close() 



    