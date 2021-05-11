# Librerías
import pandas as pd
import datetime
import time
import math
import getpass
from datetime import date
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from os import path

# Constantes
usuario=getpass.getuser()
telefono_local="3166651382"
noEncontrados=" "


# Opciones de navegacion
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument("user-data-dir=C:\\Users\\"+str(usuario)+"\\AppData\\Local\\Google\\Chrome\\User Data")

driver_path = path.abspath("driver\\chromedriver.exe")

# Leer el archivo de citas
data = pd.read_csv('citas.csv', delimiter='|', encoding='latin-1')
data_dict = data.to_dict('list')
# Listado de campos
documento = data_dict['num_doc_usr']
phone_no = data_dict['celular']
apellido1 = data_dict['apellido1']
apellido2 = data_dict['apellido2']
nombre1 = data_dict['nombre1']
nombre2 = data_dict['nombre2']
dia_cita = data_dict['fec_cita']
hora_cita = data_dict['hora_cita']
especialidad = data_dict['especialidad']
profesional = data_dict['profesional']
combo = zip(documento,phone_no,apellido1,apellido2,nombre1,nombre2,dia_cita,hora_cita,especialidad,profesional)

# Variables
conteo=0
driver = webdriver.Chrome(driver_path, chrome_options=options)
inicial = datetime.datetime.now()
parsedMessage = ''
for documento,phone_no,apellido1,apellido2,nombre1,nombre2,dia_cita,hora_cita,especialidad,profesional in combo:
    parsedMessage= "Estimado usuario "+nombre1+" "+nombre2+" "+apellido1+" "+apellido2+", "\
        +"La E.S.E. Centro hospital Luis Antonio Montero, le recuerda la oportuna asistencia a su cita "\
        +" de "+especialidad+" "\
        +"El dia "+str(dia_cita)+" a las "+str(hora_cita)+", "\
        +"con el Doctor(a) "+profesional+", "\
        +"En caso de no poder asistir recuerde cancelar con 24 horas de anticipacion."
    time.sleep(2)
    driver.get('https://web.whatsapp.com/send?phone=+57'+str(phone_no))  

    try:
        WebDriverWait(driver, 20)\
            .until(EC.element_to_be_clickable((By.XPATH,
                                            '/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]')))\
            .send_keys(parsedMessage)

        WebDriverWait(driver, 20)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                'button._1E0Oz'.replace(' ', '.'))))\
                .click()
        time.sleep(3)
        conteo += 1
    except TimeoutException: 
        noEncontrados=noEncontrados+str(phone_no)+","  
        print("Numero no encontrado")
final = datetime.datetime.now()
diferencia = final - inicial
segundos = diferencia.seconds
minutos= math.floor(segundos/60)
segundosMin=segundos-(minutos*60)
resultado="Se enviaron "+str(conteo)+" Mensajes en "+str(minutos)+" Minutos con "+str(segundosMin)+" Segundos, "+'\n'\
    "Los siguientes Telefonos no se encontraron "+noEncontrados.rstrip(noEncontrados[-1])   
driver.get('https://web.whatsapp.com/send?phone=+57'+str(telefono_local))
time.sleep(3)
WebDriverWait(driver, 20)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]')))\
    .send_keys(resultado)

WebDriverWait(driver, 20)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        'button._1E0Oz'.replace(' ', '.'))))\
        .click()
time.sleep(3)
driver.quit()
print(resultado)