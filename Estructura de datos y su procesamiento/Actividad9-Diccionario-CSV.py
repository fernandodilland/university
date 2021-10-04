from collections import namedtuple
import csv
import os
from os import remove

Personas = namedtuple("Personas",["nombre","correoElectronico"])
DiccionarioPersonas = {}

while True:
    print("\n-- Bienvenido(a) al Menú")
    print("1) Agregar una persona")
    print("2) Búsqueda específica")
    print("3) Ver listado completo")
    print("4) Eliminar una persona")
    print("5) Guardar datos en CSV")
    print("6) Lectura de CSV y carga a Diccionario")
    print("7) Salir")
    opcionElegida = int(input("> "))

    if opcionElegida == 1:
        while True:
            clave = int(input("Porfavor ingrese la clave de la persona: "))
            if clave in DiccionarioPersonas.keys():
                print("Ya existe en el diccionario esa clave, intente nuevamente")
            else:
                nombre = input("Porfavor ingrese su nombre: ").capitalize()
                correoElectronico = input("Porfavor introduzca su correo electrónico: ").lower()
                TuplaPersona = Personas(nombre,correoElectronico)
                DiccionarioPersonas[clave] = TuplaPersona
                print(f"\n-- Confirmación de datos:\nClave: {clave}, Nombre: {nombre}, Correo: {correoElectronico}")
                break

    if opcionElegida == 2:
        if DiccionarioPersonas:
            claveBuscado = int(input("Ingrese la clave a buscar: "))
            if claveBuscado in DiccionarioPersonas:
                print("\n-- Resultado de búsqueda:")
                print(f"Nombre: {DiccionarioPersonas[claveBuscado].nombre}")
                print(f"Correo: {DiccionarioPersonas[claveBuscado].correoElectronico}")
            else:
                print("No existe la clave introducida, intente nuevamente")
            
    if opcionElegida == 3:
        if DiccionarioPersonas:
            print("\n-- Listado completo de personas")
            print(f'\n{"Clave":<5} | {"Nombre":^18} | {"Correo":<25}')
            for claveCiclo in DiccionarioPersonas.keys():
                print(f'{claveCiclo:<5} | {DiccionarioPersonas[claveCiclo].nombre:^18} | {DiccionarioPersonas[claveCiclo].correoElectronico:<25}')
        else:
            print("No se encuentra ningún registro")

    if opcionElegida == 4:
        claveEliminar = int(input('Clave del registro a eliminar: '))

        if claveEliminar in DiccionarioPersonas.keys():
            print('\n-- Registor a eliminar:')
            print(f'\n{"Clave":<5} | {"Nombre":^18} | {"Correo":<25}')
            print(f'{claveEliminar:<5} | {DiccionarioPersonas[claveEliminar].nombre:^18} | {DiccionarioPersonas[claveEliminar].correoElectronico:<25}')
            eliminacion_reg = int(input("\n¿Está seguro de eliminar este registro?\n1) Si\n2) No\n> "))
            if eliminacion_reg == 1:
                del DiccionarioPersonas[claveEliminar]
                print(f"Se ha eliminado satisfactoriamente al registro No. {claveEliminar}")
            elif eliminacion_reg == 2:
                print("No se eliminará el registro")
            else:
                print("El dato es inválido")
        else:
            print("No se encuentra la clave introducida")
            
    if opcionElegida == 5:
        with open("Personas.csv","w", newline="") as archivo:
            grabador = csv.writer(archivo)
            grabador.writerow(("Clave", "Nombre", "Correo"))
            grabador.writerows([(clave, datos.nombre, datos.correoElectronico) for clave, datos in DiccionarioPersonas.items()])

        print(f"\nGuardado CSV de manera correcta en {os.getcwd()}")
        
    if opcionElegida == 6:
        with open("Personas.csv","r", newline="") as archivo:
            lector = csv.reader(archivo)
            next(lector)
            
            for clave, nombre, correoElectronico in lector:
                DiccionarioPersonas[int(clave)] = Personas(nombre, correoElectronico)

    if opcionElegida == 7:
        print("Gracias por usar el programa, buen día.")
        break
