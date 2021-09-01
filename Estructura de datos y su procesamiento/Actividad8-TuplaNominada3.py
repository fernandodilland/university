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

while True: #Menú de opciones polivalentes
    print("\n-- Bienvenido(a) al Menu")
    print("1) Agregar una persona")
    print("2) Búsqueda específica")
    print("3) Ver listado completo")
    print("4) Salir")
    opcionElegida = input("> ")
    
    if opcionElegida == "4": # Salida
        print("Gracias por usar el programa, buen día")
        break

    if opcionElegida == "1": # Agregar persona
        clave = input("Porfavor ingrese su clave: ")
        nombre = input("Porfavor ingrese su nombre: ")
        correoElectronico = input("Porfavor introduzca su correo electrónico: ")
        TuplaPersona = Personas(clave,nombre,correoElectronico) # Se organiza la tupla temporal
        print(SEPARADOR)
        ListaPersonas.append(TuplaPersona) # Se almacena en lista la tupla temporal

    if opcionElegida == "2": # Búsqueda específica
        if ListaPersonas:
            claveBuscado = input("Ingrese la clave a buscar: ")
            for busqueda in ListaPersonas:
                if(busqueda.clave) == claveBuscado:
                    print("\nHemos encontrado la clave:", claveBuscado)
                    print("El nombre es:", busqueda.nombre, "y su correo:", busqueda.correoElectronico)
        else:
            print("No se encuentra ningun registro")
            
    if opcionElegida == "3": # Impresión de listado completo
        if ListaPersonas:
            print("\nListado completo de personas:")
            print("|{:<10}|{:<15}|{:<25}|".format("Clave","Nombre","Correo electrónico"))
            for entrada in ListaPersonas: # Ciclo "for" para impresión vertical
                print("|{:<10}|{:<15}|{:<25}|".format(entrada.clave,entrada.nombre,entrada.correoElectronico))
        else:
            print("No se encuentra ningún registro")
