# Librerías
import pandas as pd
import pyautogui as pg
import datetime
import time
import math
from datetime import date
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# Usuario de sistema
usuario="ACER"
telefono_local="3166651382"

# Opciones de navegacion
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument("user-data-dir=C:\\Users\\"+usuario+"\\AppData\\Local\\Google\\Chrome\\User Data")

driver_path = 'D:\\python\\seleniumChrome\\driver\\chromedriver.exe'
data=pd.read_csv('datos.csv')
data_dict = data.to_dict('list')
phone_no = data_dict['celular']
parsedMessage = data_dict['mensaje']
combo = zip(phone_no,parsedMessage)
first = True
conteo=0
driver = webdriver.Chrome(driver_path, chrome_options=options)
inicial = datetime.datetime.now()
for phone_no,parsedMessage in combo:
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
        print("Numero no encontrado")
final = datetime.datetime.now()
diferencia = final - inicial
segundos = diferencia.seconds
minutos= math.floor(segundos/60)
segundosMin=segundos-(minutos*60)
resultado="Se enviaron "+str(conteo)+" Mensajes en "+str(minutos)+" Minutos con "+str(segundosMin)+" Segundos"   
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