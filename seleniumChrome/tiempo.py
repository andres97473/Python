import datetime
import time
import math
from datetime import date

inicial = datetime.datetime.now()

time.sleep(70)

final = datetime.datetime.now()

diferencia = final - inicial
segundos = diferencia.seconds
minutos= math.floor(segundos/60)
segundosMin=segundos-(minutos*60)

print(inicial.strftime("%H:%M:%S"))
print(final.strftime("%H:%M:%S"))
print(minutos," Minutos con ",segundosMin, " Segundos")


