import getpass

usuario=str(getpass.getuser())


print("el usuario es "+usuario)

largo=10
saludo="Hola"
acumulado=""

for i in range(largo):
    acumulado=acumulado+saludo+","

acumulado.rstrip(acumulado[-1])

imprimir=acumulado+" Texto acumulado de prueba"+'\n\n'\
    +"segunda linea de prueba"

print(imprimir)

