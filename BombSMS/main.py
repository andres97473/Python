import pyautogui as pg
import time
import webbrowser as web
phone_no= "3166651382"
parsedMessage= "Esto es un sms de prueba 6"
web.open('https://web.whatsapp.com/send?phone=+57'+phone_no+'&text='+parsedMessage)
time.sleep(8)
for i in range(5):
    pg.write('We')
    pg.press('enter')
    print('Mensaje #'+str(i+1)+' enviado')
    pass
pg.alert('Bomba de mensajes finalizada')
