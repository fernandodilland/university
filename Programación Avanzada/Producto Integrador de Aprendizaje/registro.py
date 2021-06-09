"""
Materia: Programación avanzada (Grupo 21), Profesor: Dr. José Felipe Ramirez Ramirez.
Programa realizado por: Fernando Dilland Mireles Cisneros, 1837532.
"""

# Producto Integrador de Aprendizaje

# "registro.py" Programa principal del proyecto

# Módulo de llamado de clase dentro de programa secundario "clases.py"
from clases import Participante

# Módulos (Librerías)
import re # Expresiones Regulares (Regex)
from datetime import datetime # Manejo de fecha/hora
import os # Gestión de archivos a nivel del sistema operativo
import json # Formato de texto y Se usará al final para serializar
import csv # Archivos tipo CSV
from csv import writer # Se importa escritor de CSV

# Variable para limpiar consola
LimpiarPantalla = lambda: os.system('cls') # on Windows System

# Se declara lista global
listaObjetos = []

# Declaración de Expresiones Regulares
RegexCorreo = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
                                        # Admite ejemplo "correo@gmail.com"
RegexNombre = r'[A-Z][a-z]*'            # Adminte ejemplo "Fernando"
RegexFecha = r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$"
                                        # Admite ejemplo 03-05-1999
RegexOpcionesMenu = r"^[12345678X]{1}$" # Admite ejemplo "1" o "X"

# Variable print muy utilizada en inputs para permitir lectura de impresiones
enterContinuar="Pulse enter para continuar..."


# ---------- Procedimientos ----------

# Función [1] Cargar información de CSV
# Parte trabajada por: Fernando Mireles, Alejandro López y Carlos Martínez.
def funcionCargarInformacionCSV():

    # Para respaldo y carga de información, si hay archivo de datos
    if os.path.exists(archivo):
        print("\n--- Se encontró un archivo existente ----")

        # Se abre el archivo existente
        f = open(archivo,"r+")
        print("--- El sistema abrió internamente el archivo existente ignorando encabezado ----\n")
        # Declaración lista de objetos e ignorador de primera línea (header)
        lector_CSV = csv.reader(f)
        header=0 # Saltador del header (primera fila)
        for fila in lector_CSV :
            print("Fila que se está leyendo: ", fila)
            #  Habilitar para pruebas de inyección directa desde archivo registro.csv
            if header==1:
                listaObjetos.append(Participante(fila[0],fila[1],fila[2],fila[3]))
            header=1
        print("\nLa lista completa es: ",listaObjetos,"\n")
        f.close()

    # Si no existe el archivo
    if not os.path.exists(archivo):
        # Crea el archivo CSV
        f = open(archivo,"w+")
        # Escribe el encabezado
        f.write("Correo | Nombre | Nacimiento | Momento")
        print("--- No se encontró archivo, se creó y se puso únicamente encabezado ----")
        f.close()

# Función que recibe correo y busca
# Parte realizada por: Joselyn Guerra, Samantha Medina y Fernando Mireles.
def busquedaCorreo(correoBusqueda):
    Contador=1
    Encontrado=False
    Omision=False
    for objeto in listaObjetos:
        if objeto.correo==correoBusqueda:
            print("\nEncontrado en la fila: ", Contador," de la lista.")
            print("Fila de donde se encontró: ", objeto)
            Encontrado=True
        Contador=Contador+1
    if correoBusqueda=="":
        Omision=True
    if Encontrado==False:
        if Omision==False:
            print("Este correo ", correoBusqueda, " no está registrado en la lista")


# Prodecimiento serialización
# Parte realizada por: Joselyn Guerra, Samantha Medina y Fernando Mireles.
def sistemaSerializar():
    print("Ha elegido: \"Serializar información a JSON\"")
    json_data = json.dumps(listaObjetos, default=lambda o: o.__dict__, indent=4)
        # En línea anterior se serializa.
    print("\nLa lista original es: ",listaObjetos,"\n")
    print("La lista serializada es: ",json_data)

# Procedimiento Actualizar CSV
# Parte realizada por Fernando Mireles.
def actualizarCSV():
    print("Ha elegido: \"Actualizar información de CSV\"")
    if os.path.exists(archivo):
        print("\n--- Se encontró un archivo existente ----")
        # Verifica si hay respaldo, y lo elimina
        if os.path.exists(archivo_respaldo):
            os.remove(archivo_respaldo)
            print("--- Se encontró un respaldo existente, se ha eliminado ----")
        # Pasa el archivo del archivo al respaldo
        os.rename(archivo,archivo_respaldo)
        print("--- Se pasó el archivo actual a respaldo ----")

        # Se abre el archivo existente
        f = open(archivo,"w+")
        with open(archivo, 'a', newline="\n") as objetoIOWrapper:
            writer_object = writer(objetoIOWrapper)
            print(listaObjetos)
            writer_object.writerow(f"Correo|Nombre|Nacimiento|Momento".split())
                        # Escribe en la primera fila el "header" en este caso Correo, Nombre, etc
            cantidadfilas=len(listaObjetos)
            salida=0    # Ayuda a limitar teniendo en cuenta la cantidad de filas para recorrer
                        # toda la lista y salirse al terminar
            contador=-1 # Contador sirve para posicionar index de lista para su extracción
            while salida<cantidadfilas:
                contador=contador+1
                objetoTemporal=listaObjetos[contador]
                print("Elemento temporal: ", objetoTemporal)
                elementoCorreoTemporal=objetoTemporal.correo    # Obtiene el dato especifico de la lista
                                                                # dentro de la característica dada
                                                                # por la clase
                print("Elemento correo: ", "\""+elementoCorreoTemporal)
                elementoNombreTemporal=objetoTemporal.nombre
                print("Elemento nombre: ", "\""+elementoNombreTemporal)
                elementoNacimientoTemporal=objetoTemporal.nacimiento
                print("Elemento nacimiento: ", "\""+elementoNacimientoTemporal)
                elementoMomentoTemporal=objetoTemporal.momento
                print("Elemento momento: ", "\""+elementoMomentoTemporal)
                print("Elemento temporal (Pseudo-final): ", objetoTemporal)
                salida=salida+1
                print("\n--- Se ha actualizado la información del CSV con éxito ---\n")
                writer_object.writerow((elementoCorreoTemporal).split()+(elementoNombreTemporal).split()+(elementoNacimientoTemporal).split()+(elementoMomentoTemporal).split())
                    # El línea anterior es el más importante, escribe después del header (primera fila)
                    # los elementos slpliteados (para quitar comas) y los elementos se ordenan horizontalmente en cada fila
                    # respetando las características de la clase y sus propiedades.
            objetoIOWrapper.close()
        f.close() # Se abrió 2 veces por experimentación, no nos funcionó el programa sin este mecanismo.

# Procedimiento de eliminación
# Parte hecha por Alejandro López y Fernando Mireles.
def eliminacionPersona():
    LimpiarPantalla()
    print("Ha elegido: \"Eliminar participantes\"")
    validacionExistenciaCorreo=False
    while validacionExistenciaCorreo==False:
        Contador=1
        validacionCorreo=False
        while validacionCorreo==False:
            correoRegistro=str(input("Ingrese el correo: "))
            if correoRegistro=="":
                validacionCorreo=True
                validacionExistenciaCorreo=True
            else:
                if re.match(RegexCorreo,correoRegistro):
                    print("Formato del correo válido")
                    validacionCorreo=True
                else:
                    print("Formato de correo inválido, intente nuevamente")
        Encontrado=False
        Omision=False
        for objeto in listaObjetos:
            if objeto.correo==correoRegistro:
                Encontrado=True
                LimpiarPantalla()
                print("El correo", correoRegistro, " si se encontró en lista, a él lo eliminaremos")
                print("\nEncontrado en la fila: ", Contador," de la lista.")
                print("Fila de donde se eliminará: ", objeto)
                ContadorIndex=Contador-1
                listaObjetos.remove(objeto)
                print("\nLista con modificación: ", listaObjetos)
                validacionCorreo=True
                validacionExistenciaCorreo=True
                Omision=True
            Contador=Contador+1
        if correoRegistro=="":
            Omision=True
        if Encontrado==False:
            if Omision==False:
                LimpiarPantalla()
                print("Este correo", correoRegistro, "no está registrado en la lista, intente de nuevo")
                input(enterContinuar)
    print("\n--- Se ha eliminado con éxito ---\n")

# Procedimiento Modificación de Elementos de Fila
# Parte hecha por Fernando Mireles y Alejandro Lopez.
def modificarParticipantes():
    LimpiarPantalla()
    print("Ha elegido: \"Modificar participantes\"")
    validacionExistenciaCorreo=False
    while validacionExistenciaCorreo==False:
        Contador=1
        validacionCorreo=False
        while validacionCorreo==False:
            correoRegistro=str(input("Ingrese el correo: "))
            if correoRegistro=="":
                validacionCorreo=True
                validacionExistenciaCorreo=True
            else:
                if re.match(RegexCorreo,correoRegistro):
                    print("Formato del correo válido")
                    validacionCorreo=True
                else:
                    print("Formato de correo inválido, intente nuevamente")

        Encontrado=False
        Omision=False
        for objeto in listaObjetos:
            if objeto.correo==correoRegistro:
                Encontrado=True
                LimpiarPantalla()
                print("El correo", correoRegistro, " si se encontró en lista, con él trabajaremos")
                print("\nEncontrado en la fila: ", Contador," de la lista.")
                print("Fila de donde se modificará: ", objeto)
                ContadorIndex=Contador-1
                validacionCorreo=False
                input(enterContinuar)
                while validacionCorreo==False:
                    LimpiarPantalla()
                    print("El correo a modificar es:",correoRegistro)
                    correoRegistro=input("Ingrese el correo nuevo (o el mismo): ")
                    if re.match(RegexCorreo,correoRegistro):
                        print("Formato de correo",correoRegistro,"válido")
                        validacionCorreo=True
                    else:
                        print("Formato de correo inválido, intente de nuevo")
                        input(enterContinuar)

                validacionNombre=False
                while validacionNombre==False:
                    LimpiarPantalla()
                    nombreRegistro=input("Ingrese el nombre nuevo (o el mismo): ")
                    if re.match(RegexNombre,nombreRegistro):
                        print("Formato de nombre",nombreRegistro,"válido")
                        validacionNombre=True
                    else:
                        print("Formato de nombre inválido, intente de nuevo")
                        input(enterContinuar)
                validacionFecha=False
                while validacionFecha==False:
                    LimpiarPantalla()
                    fechaNacimientoRegistro=input("Ingrese la fecha de nacimiento nueva (o la misma) (ej 03-05-1999): ")
                    if re.match(RegexFecha,fechaNacimientoRegistro):
                        print("Formato de fecha",fechaNacimientoRegistro,"válida")
                        ahora = datetime.now()
                        momentoRegistro=ahora.strftime("%d/%m/%Y-%H:%M:%S")
                        print("El registro se realizó en:",momentoRegistro)
                        validacionFecha=True
                    else:
                        print("Formato de fecha inválida, intente de nuevo")
                        input(enterContinuar)

                print("Confirmando datos nuevos:", correoRegistro, nombreRegistro,fechaNacimientoRegistro,momentoRegistro)
                input(enterContinuar)

                listaObjetos[ContadorIndex]=(Participante(correoRegistro,nombreRegistro,fechaNacimientoRegistro,momentoRegistro))
                print("\nLista con modificación: ", listaObjetos)
                validacionCorreo=True
                validacionExistenciaCorreo=True
                Omision=True
            Contador=Contador+1
        if correoRegistro=="":
            Omision=True
        if Encontrado==False:
            if Omision==False:
                LimpiarPantalla()
                print("Este correo", correoRegistro, "no está registrado en la lista, intente de nuevo")
                input(enterContinuar)

# Procedimiento de nuevo registro
# Parte realizada por Joselyn Guerra, Samantha Medina, Fernando Mireles, Alejandro López y Carlos Martínez.
def registroParticipante():
    LimpiarPantalla()
    print("Ha elegido: \"Registrar participantes\"")
    validacionExistenciaCorreo=False
    while validacionExistenciaCorreo==False:
        validacionCorreo=False
        while validacionCorreo==False:
            correoRegistro=str(input("Ingrese el correo: "))
            if correoRegistro=="":
                validacionCorreo=True
                validacionExistenciaCorreo=True
            else:
                if re.match(RegexCorreo,correoRegistro):
                    print("Formato del correo válido")
                    validacionCorreo=True
                else:
                    print("Formato de correo inválido, intente nuevamente")
        Encontrado=False
        Omision=False
        for objeto in listaObjetos:
            if objeto.correo==correoRegistro:
                Encontrado=True
                LimpiarPantalla()
                print("El correo", correoRegistro, "ya existe, intente con otro")
        if correoRegistro=="":
            Omision=True
        if Encontrado==False:
            if Omision==False:
                LimpiarPantalla()
                print("Este correo", correoRegistro, "no está registrado en la lista, continúe")
                input(enterContinuar)
                validacionNombre=False
                while validacionNombre==False:
                    LimpiarPantalla()
                    nombreRegistro=input("Ingrese el nombre del nuevo registro: ")
                    if re.match(RegexNombre,nombreRegistro):
                        print("Formato de nombre",nombreRegistro,"válido")
                        validacionNombre=True
                    else:
                        print("Formato de nombre inválido, intente de nuevo")
                        input(enterContinuar)
                validacionFecha=False
                while validacionFecha==False:
                    LimpiarPantalla()
                    fechaNacimientoRegistro=input("Ingrese la fecha de nacimiento (ej 03-05-1999): ")
                    if re.match(RegexFecha,fechaNacimientoRegistro):
                        print("Formato de fecha",fechaNacimientoRegistro,"válida")
                        ahora = datetime.now()
                        momentoRegistro=ahora.strftime("%d/%m/%Y-%H:%M:%S")
                        print("El registro se realizó en:",momentoRegistro)
                        validacionFecha=True

                        # Al llegar aquí, se completó declaración de registro, toca inyectarlo a lista
                        listaObjetos.append(Participante(correoRegistro,nombreRegistro,fechaNacimientoRegistro,momentoRegistro))
                        print("Datos introducidos: ", listaObjetos)
                    else:
                        print("Formato de fecha inválida, intente de nuevo")
                        input(enterContinuar)
                validacionExistenciaCorreo=True

# Procedimiento menú
# Parte hecha por Fernando Mireles y Alejandro López.
def menuPrincipal():
    Linea1 = "[1] Cargar información de CSV\n"
    Linea2 = "[2] Registrar participantes\n"
    Linea3 = "[3] Buscar participante\n"
    Linea4 = "[4] Modificar participante\n"
    Linea5 = "[5] Eliminar participante\n"
    Linea6 = "[6] Ver lista de participantes\n"
    Linea7 = "[7] Actualizar información de CSV\n"
    Linea8 = "[8] Serializar información a JSON\n"
    Linea9 = "[X] Salir\n"
    Linea10 = "¿Qué opción desea? > "

    # Ciclo para permitir únicamente valores disponibles del menú
    while (True):
        LimpiarPantalla()
        print("--- Menú de opciones ---")
        print("{}{}{}{}{}{}{}{}{}".format(Linea1,Linea2,Linea3,
                                          Linea4,Linea5,Linea6,
                                          Linea7,Linea8,Linea9))

        # Declaración de opción elegida
        opcion_elegida = str(input(Linea10).upper())

        # Validador de opción válida en menú
        if re.match(RegexOpcionesMenu, opcion_elegida):

            # Elección del menú "X" (Salida)
            if opcion_elegida=="X":
                LimpiarPantalla()
                print("Ha elegido: \"Salir\"")
                break

            # Elección del menú "1" (Carga de CSV)
            if opcion_elegida=="1":
                LimpiarPantalla()
                print("Ha elegido: \"Cargar información de CSV\"")
                funcionCargarInformacionCSV()

            # Elección del menú "5" (Registro)
            if opcion_elegida=="2":
                registroParticipante()

            # Elección del menú "3" (Buscador)
            if opcion_elegida=="3":
                LimpiarPantalla()
                print("Ha elegido: \"Buscar participantes\"")
                correoABuscar=input("Escriba el correo a buscar: ")
                busquedaCorreo(correoABuscar)
                if correoABuscar=="":
                    validacionCorreo=True
                    validacionExistenciaCorreo=True

            # Elección del menú "4" (Modificación)
            if opcion_elegida=="4":
                modificarParticipantes()

            # Elección del menú "5" (Eliminación)
            if opcion_elegida=="5":
                eliminacionPersona()

            # Elección del menú "6" (Vista previa de lista).
            if opcion_elegida=="6":
                LimpiarPantalla()
                print("Ha elegido: \"Ver lista de participantes\"")

                print("Correo              Nombre              Nacimiento          Momento")
                for objeto in listaObjetos:
                    print("{:20}{:20}{:20}{:20} ".format(objeto.correo, objeto.nombre, objeto.nacimiento, objeto.momento))

            # Elección del menú "7" (Actualizar CSV).
            if opcion_elegida=="7":
                LimpiarPantalla()
                actualizarCSV()

            # Elección del menú "8" (Serialización).
            if opcion_elegida=="8":
                sistemaSerializar()
            input(enterContinuar)
            LimpiarPantalla()
        else:
            print("Opción inválida, intente nuevamente...")
            input(enterContinuar)
            LimpiarPantalla()

# Se declara ruta de archivos y nombres
ruta_archivo = os.path.abspath(os.getcwd())
archivo_respaldo = ruta_archivo+"\\registro.bak"
archivo = ruta_archivo + "\\registro.csv"

# Procedimiento main
# Parte hecha por Alejandro López.
def main():
    menuPrincipal()

main() # Se manda a llamar el main hasta el final, para tener cargado todo el código de manera previa.
