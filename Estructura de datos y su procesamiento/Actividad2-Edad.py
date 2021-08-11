'''
Codificar un script de Python que solicite la fecha de nacimiento de una persona
y nos regrese su edad aproximada mediante restar el año actual al año de nacimiento reportado
'''

import datetime

SEPARADOR = ("*" * 20)

# Preguntar al usuario fecha de nacimiento
fechaNacimiento = input("Ingrese su fecha de nacimiento (dd/mm/yyyy): ")
fechaNacimiento = datetime.datetime.strptime(fechaNacimiento, "%d/%m/%Y").date()
print("Confirmación de nacimiento: "+ fechaNacimiento.strftime("%d") + " de " + fechaNacimiento.strftime("%B del %Y"))

fechaActual = datetime.datetime.today().date()
print("Confirmación de fecha actual:",fechaActual)
edad = fechaActual.year - fechaNacimiento.year
mesVerificador = fechaActual.month - fechaNacimiento.month
fechaVerificador = fechaActual.day - fechaNacimiento.day

edad = int(edad)
mesVerificador = int(mesVerificador)
fechaVerificador = int(fechaVerificador)

if mesVerificador < 0 :
    edad = edad-1
elif fechaVerificador < 0 and mesVerificador == 0:
    edad = edad-1

if fechaNacimiento.month <= fechaActual.month:
    if fechaNacimiento.day <= fechaActual.day:
        if edad > 0:
            print("Ya cumplió años en el año actual", fechaActual.year)
        else:
            print("Nació en el año actual", fechaActual.year)
    else:
        print("No ha cumplido años en el año actual", fechaActual.year)
else:
    print("No ha cumplido años en el año actual", fechaActual.year)

print(SEPARADOR * 1)
print("Su edad es de: {0:d}".format(edad), "año(s)")
