"""
Materia: Programación avanzada (Grupo 21), Profesor: Dr. José Felipe Ramirez Ramirez.
Programa realizado por: Fernando Dilland Mireles Cisneros, 1837532.
"""

# CRUD es el acrónimo de Create, Read, Update, Delete.
# Es el equivalente a lo que antes se conocía como altas, bajas, cambios y consultas.
# Tiene una secuencia:
# - Se captura información.
# - Si la llave primaria existe, se muestran los datos.
# - En ese caso, las acciones posibles son Actualizar o Eliminar.
# - Si la llave primaria no existe, sólo se puede agregar.

# Supongamos que tenemos un repositorio llamado clientes, que tiene la siguiente
# estructura de datos:
# (key) cliente (int->10000:99999)
# (val) nombre (str->3:30, caracteres latinos)
#       apellidos (str->3:30 caracteres latinos)
#       fnac (datetime->Fecha YYYY-MM-DD)
#       correo (str->Correo electrónico)

# SECCIÓN DE IMPORTACIÓN DE MÓDULOS:
import datetime
import re # Librería Regex
# Módulo para trabajar con archivos a nivel sistema operativo.
import os
from csv import writer

# SECCIÓN DE VARIABLES GLOBALES:
# Secuencias Regular Expression requeridas ----------------------------------
RegexCorreo = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
RegexNombre = r'[A-Z][a-z]*'
RegexFecha = r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$"
# Variables de trabajo para la captura ____----------------------------------
cliente = 0
nombre=''
apellidos=''
Fnac='' # Fecha de nacimiento
correo=''

# Crear el repositorio general, de tipo diccionario, por lo cual tendrá
# una llave (key/k) y un valor (value/v), que en este caso será
# una lista de valores.
 #Diccionario
clientes={}

# SECCIÓN DE FUNCIONES REQUERIDAS
# Esa función muestra el contenido total del diccionario Clientes, de
# forma tabulada.
def muestra_datos():
    global clientes
    print("\n")
    print("{:<10} {:<20} {:<20} {:<10} {:<20}".format("Número","Nombre","Apellido(s)","Nacimiento","Correo"))
    print("{:<10} {:<20} {:<20} {:<10} {:<20}".format("-"*10,"-"*20,"-"*20,"-"*10,"-"*20))
    for k,v in clientes.items(): # "k" es llave
        print("{0:<10} {1:<20} {2:<20} {3:<10} {4:<20}".format(k,v[0],v[1],v[2],v[3]))

# Función que se encarga de preguntar los datos no primos (que no forman la llave)
def pregunta_datos():
    global cliente, nombre, apellidos, Fnac, correo # Se manejan globales (NO LOCALES)
    # Capturar los datos que no son llaves.
    # usar las variables globales.
    while True: # Valida Nombre
        nombre = input("Ingrese nombre: ")
        if(re.search(RegexNombre, nombre)):
            break
        else:
            print("--- Formato de nombre inválido ---")

    while True: # Valida Apellido
        apellidos = input("Ingrese apellido: ")
        if(re.search(RegexNombre, apellidos)):
            break
        else:
            print("--- Formato de apellido inválido ---")

    while True: # Valida Fecha
        Fnac = input("Ingrese fecha de nacimiento (Formato ##-##-####): ")
        if(re.search(RegexFecha, Fnac)):
            break
        else:
            print("--- Formato de fecha inválido ---")

    while True: # Valida Correo
        correo = input("Ingrese el correo: ")
        if(re.search(RegexCorreo, correo)):
            break
        else:
            print("--- Formato de correo inválido ---")

ruta=os.path.abspath(os.getcwd())

# Nombres de archivos para trabajo.
archivo_trabajo = ruta+"\\clientes.csv"

# EJERCICIO 1: Carga de datos a diccionario.
# Elaborar un procedimiento llamado carga_datos_csv()
# que haga lo siguiente:
# - Debe usar la variable global clientes, que es el diccionario que contiene los datos.
# - Debe verificar la existencia del archivo clientes.csv
# - En caso de que exista el archivo
#   - Leer el archivo clientes.csv desde la ruta donde se encuentra el programa
#   - Agregar un elemento al dicionario por cada línea del archivo, excepto encabezado
#   - Cerrar el archivo csv

def carga_datos_csv():
    global clientes
    if os.path.exists(archivo_trabajo):
        f = open(archivo_trabajo,"w+")
        # Escribo la primer línea del archivo, con los encabezados.
        f.write(f'Número     Nombre               Apellido(s)          Nacimiento    Correo\n----------      ------------------- -----------------    -----------          ------------------\n')
        for k,v in clientes.items(): # "k" es llave
            f.write("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}\n".format(k,v[0],v[1],v[2],v[3]))
        f.close()
    else:
        f = open(archivo_trabajo,"w+")
        # Escribo la primer línea del archivo, con los encabezados.
        f.write(f'Número     Nombre               Apellido(s)          Nacimiento    Correo\n----------      ------------------- -----------------    -----------          ------------------\n')
        for k,v in clientes.items(): # "k" es llave
            f.write("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}\n".format(k,v[0],v[1],v[2],v[3]))
        f.close()


# EJERCICIO 2: Guarda datos a csv a partir de un diccionario.
# Elaborar un procedimiento llamado guardar_datos_csv()
# que haga lo siguiente:
# - Debe usar la variable global clientes, que es el diccionario que contiene los datos.
# - Debe verificar la existencia del archivo clientes.csv
# - En caso de que exista el archivo
#   - Eliminar el archivo clientes.csv que está en la ruta donde está el programa
#   - Crear el archivo clientes.csv
#   - Agregar la línea de encabezado
#   - Agregar cada uno de los elementos del diccionario como línea del archivo csv
#   - Cerrar el archivo

# SECCIÓN ENTRY-POINT

def guardar_datos_csv(nombre_def,apellido_def,fecha_def,correo_def):
    global clientes
# Determinar si el archivo de trabajo ya existe en la ruta
    if os.path.exists(archivo_trabajo):
        with open(archivo_trabajo, 'a', newline='') as objetoIOWrapper:
            # Pass this file object to csv.writer()
            # and get a writer object
            writer_object = writer(objetoIOWrapper)
            # Pass the list as an argument into
            # the writerow()
            #for k,v in clientes.items(): # "k" es llave
            # SI JALA DiccionarioTemporal={nombre_def+ apellido_def+fecha_def+correo_def}
            DiccionarioTemporal={(r"{0:<20} {1:<20} {2:<20} {3:<20}".format(nombre_def, apellido_def, fecha_def, correo_def) )}
            #writer_object.writerow("{0:<20} {1:<20} {2:<20} {3:<20}\n".format(nombre_def,apellido_def,fecha_def,correo_def))
            writer_object.writerow(DiccionarioTemporal)
            #Close the file object
            objetoIOWrapper.close()
    else:
        f = open(archivo_trabajo,"w+")
        f.write(f'Número     Nombre              Apellido(s)          Nacimiento     Correo\n----------      ------------------- -----------------    -----------          ------------------\n')
        f.close()
        with open(archivo_trabajo, 'a', newline='') as objetoIOWrapper:
            writer_object = writer(objetoIOWrapper)
            DiccionarioTemporal={(r"{0:<20} {1:<20} {2:<20} {3:<20}".format(nombre_def, apellido_def, fecha_def, correo_def) )}
            writer_object.writerow(DiccionarioTemporal)
            objetoIOWrapper.close()

print("\nCRUD de clientes basado en diccionarios.")
print("\n   * en Número de cliente, muestra el contenido del directorio.")
print("\n   Dejar vacío el Número de cliente, guarda los datos y sale del programa.")
while True:
    # Opciones para menú de elección del los ejercicios
    ciclo=False
    opcion=0
    print(" ")
    print("-"*50)
    Cliente=input("Dame el número de cliente (* Consulta):")
    # Validación de( captura usando Regular Expresions.
    if (Cliente==''):
        break
    if (Cliente=='*'):
        muestra_datos()
        continue
    cliente=int(Cliente)
    if (cliente in clientes):
        # Mostrar datos registrados.
        muestra_datos()
        # Preguntar qué deseo hacer: Actualizar, Eliminar, Siguiente.
        accion=input("\nActualizar/Eliminar/Siguiente (primer letra): ")
        # Si Actualizar, se pregunta el resto de los datos, y se actualiza el diccionario.
        if accion=="A":
            pregunta_datos()
            clientes[cliente]=[nombre,apellidos,Fnac,correo]
            while not ciclo:
                opcion=int(input("Para trabajar con el archivo, eliga el Ejercicio deseado (escriba 1 ó 2):"))
                if opcion == 1:
                    carga_datos_csv()
                    print("Se ejecutó satisfactoriamente el Ejercicio 1, revise su archivo .csv")
                    ciclo = True
                elif opcion == 2:
                    guardar_datos_csv(nombre,apellidos,Fnac,correo)
                    print("Se ejecutó satisfactoriamente el Ejercicio 2, revise su archivo .csv")
                    ciclo = True
        # Si Eliminar, se borra el elemento del diccionario.
        if accion=="E":
            del clientes[cliente]
            while not ciclo:
                opcion=int(input("Para trabajar con el archivo, eliga el Ejercicio deseado (escriba 1 ó 2):"))
                if opcion == 1:
                    carga_datos_csv()
                    print("Se ejecutó satisfactoriamente el Ejercicio 1, revise su archivo .csv")
                    ciclo = True
                elif opcion == 2:
                    guardar_datos_csv(nombre,apellidos,Fnac,correo)
                    print("Se ejecutó satisfactoriamente el Ejercicio 2, revise su archivo .csv")
                    ciclo = True
        # Si Siguiente, entonces regresa a preguntar otro cliente.
        if accion=="S":
            while not ciclo:
                opcion=int(input("Para trabajar con el archivo, eliga el Ejercicio deseado (escriba 1 ó 2):"))
                if opcion == 1:
                    carga_datos_csv()
                    print("Se ejecutó satisfactoriamente el Ejercicio 1, revise su archivo .csv")
                    ciclo = True
                elif opcion == 2:
                    guardar_datos_csv(nombre,apellidos,Fnac,correo)
                    print("Se ejecutó satisfactoriamente el Ejercicio 2, revise su archivo .csv")
                    ciclo = True
            continue
    else:
        # Pregunta el resto de los datos, y agrega el elemento.
        pregunta_datos()
        clientes[cliente]=[nombre,apellidos,Fnac,correo]
        while not ciclo:
            opcion=int(input("Para trabajar con el archivo, eliga el Ejercicio deseado (escriba 1 ó 2):"))
            if opcion == 1:
                carga_datos_csv()
                print("Se ejecutó satisfactoriamente el Ejercicio 1, revise su archivo .csv")
                ciclo = True
            elif opcion == 2:
                guardar_datos_csv(nombre,apellidos,Fnac,correo)
                print("Se ejecutó satisfactoriamente el Ejercicio 2, revise su archivo .csv")
                ciclo = True

# Acceder al programa.
# Ingresar 3 registros.
# Salir del programa.
# Entrar de nuevo. Deberán cargarse los registros de la ejecución pasada.
# Eliminar un registro existente.
# Agregar dos registros más, diferentes a los anteriores.
# Salir del programa.
# Entrar de nuevo. Deberán cargarse los registros de la ejecución pasada.
# Algo así tendrías que hacer en un programa para dispositivos móviles que
# no tenga base de datos instalada.