"""
Codificar un algoritmo en Python que permita registrar la clave (Por el momento,
no esn ecesario validar si la clave es unica), el nombre y correo electrónico
de múltiples personas, hasta que el usuario indique que ha concluído con la captura
correspondiente (proponga usted el mecanismo para esto).
Una vez concluída la captura, se deberá desplegar el listado completo de las personas registradas.
NOTA: Puede elegir utilizar tupla nominadas (recomendable) o bien, listas anidadadas"""

SEPARADOR = ("*" * 20)

from collections import namedtuple # Librería para tuplas nominadas

Personas = namedtuple("Personas",["clave","nombre","correoElectronico"]) # Declaración de estructura de tupla
ListaPersonas=[] # Lista vacía para meter datos (tuplas)

while True: # Ciclo para preguntar datos
    print("\n-- Bienvenido Usuario al Menu, porfavor Introduzca los siguientes datos:")
    clave = input("Porfavor ingrese su clave (x para salir): ")
    if clave == "x":
        break
    else:
        nombre=input("Porfavor ingrese su nombre: ")
        correoElectronico=input("Porfavor introduzca su correo electrónico: ")
        TuplaPersona = Personas(clave,nombre,correoElectronico) # Se organiza la tupla temporal
        print(">>> Tupla nominada temporal:",TuplaPersona)
        print(SEPARADOR)
        ListaPersonas.append(TuplaPersona) # Se almacena en lista la tupla temporal

# Impresión de datos
print("\nLista original:", ListaPersonas)
print("\nA continuación imprimimos las personas en vertical:")

for entrada in ListaPersonas: # Ciclo "for" para impresión vertical
    print(entrada.clave)
    print(entrada.nombre)
    print(entrada.correoElectronico)
    print(SEPARADOR)