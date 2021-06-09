"""
Materia: Programación avanzada (Grupo 21), Profesor: Dr. José Felipe Ramirez Ramirez.
Programa realizado por: Fernando Dilland Mireles Cisneros, 1837532.
"""

# Un encuestador está solicitando un programa de encuestas
# de salida para el día de la elección.
#
# Fundamentalmente, se debe caprurar en una bitácora lo siguiente:
# id: (int) Número entero positivo y consecutivo, que inicia en 1. Se asignará
#           automáticamente por el sistema.
# preferencia: (int) Partido por el cual se tuvo preferencia.
# sexo: (str) Sexo del votante
# edad: (int) Edad del votante
# marca_temporal: (datetime) Fecha y hora en la que se registra el dato. Toma la fecha y 
#           hora del sistema.

# EJERCICIO 1: REALIZA LOS IMPORTS NECESARIOS PARA EL TRABAJO CON ARCHIVOS DE SISTEMA
# OPERATIVO, TIPOS DATETIME, EXPRESIONES REGULARES, Y JSON

import os
from datetime import datetime
import re
import json
import time # Solo se usará para el sleep, usado para mostrar la fecha y hora del registro

# DICCIONARIOS DE TRABAJO
partidos={
    1: "PARTIDO ACCIÓN NACIONAL",
    2: "PARTIDO REVOLUCIONARIO INSTITUCIONAL",
    3: "PARTIDO DE LA REVOLUCIÓN DEMOCRÁTICA",
    4: "PARTIDO MOVIMIENTO CIUDADANO",
    5: "PARTIDO MORENA"
}

sexo={
    1: "HOMBRE",
    2: "MUJER"
}

# EJERCICIO 2: DECLARA UN CLASE LLAMADA Sufragio PARA MANEJAR LOS DATOS. LA CLASE 
# DEBERÁ TENER UN MÉTODO CONSTRUCTOR PARA PODER GENERAR LA INSTANCIA Y PROPORCIONAR LOS 
# VALORES EN UNA SOLA LÍNEA.

class Sufragio:
    ID = 0
    Pref_Partido = 0
    Sexo = 0
    Edad = 0
    marca_temporal = 0
    # Constructor
    def __init__(self,ID,Pref_Partido,Sexo,Edad,marca_temporal):
        # Atributos
        self.ID = ID
        self.Pref_Partido = Pref_Partido
        self.Sexo = Sexo
        self.Edad = Edad
        self.marca_temporal = marca_temporal

    # Metodo valores en una sola línea
    def ValoresLineal(self):
        print(self.ID,"",self.Pref_Partido,"",self.Sexo,"",self.Edad,"",self.marca_temporal)

# EJERCICIO 3: CODIFICA EL ENTRY POINT (CÓDIGO FUERA DE TODO PROCEDIMIENTO)
# QUE HAGA LO SIGUIENTE.
# 3.1: DECLARA UNA LISTA LLAMADA Sufragios, QUE PUEDA CONTENER LOS creaContenidoS CAPTURADOS.

Sufragios=[]

# 3.2 DECLARA UNA VARIABLE QUE TE PERMITA CONTAR EL id

ContadorID_Actual=0

# 3.3 GENERA UN CICLO INFINITO QUE PREGUNTE LOS DATOS. EL CICLO TERMINA CUANDO SE OMITA
#       EL PRIMER DATO (preferenCIA). DEBE PREGUNTAR LOS DATOS HASTA QUE SEAN CORRECTOS.
#
#       EN CADA CICLO DEBE OCURRIR LO SIGUIENTE.
#       - CALCULAR CUÁL ES EL id QUE SIGUE
#       - PREGUNTAR CUÁL ES EL PARTIDO DE PREFERENCIA (DEBE ESTAR EN EL DICCIONARIO
#           partidos).
#       - PREGUNTAR EL SEXO (DEBE ESTAR EN EL DICCIONARIO sexos).
#       - PREGUNTAR LA EDAD (DEBE SER MAYOR A 18)
#       - RECUPERAR LA FECHA Y HORA DEL SISTEMA.
#       - SI TODOS LOS DATOS SON CORRECTOS, GENERAR UN creaContenido BASADO EN LA CLASE
#           Sufragio, Y AGREGARLA A LA LISTA Sufragios.

# Se crea variable temporal "SalidaPrograma" por si omite
SalidaPrograma=0
while (SalidaPrograma==0):

    # El contador incrementa el consecutivo
    ContadorID_Actual+=1

    Salida_omision = False
    os.system('cls') # Limpia pantalla del terminal
    print("----- Programa hecho por: Fernando Dilland Mireles Cisneros, 1837532 -----")
    print("\nBienvenido(a) votante, su ID es:",ContadorID_Actual,)

    # Input Partido Político
    Validador_temporal = False
    while (Validador_temporal==False):
        solicitudPartido="\n>>> Vote por alguno de los siguientes partidos políticos <<<\n1) PARTIDO ACCIÓN NACIONAL\n2) PARTIDO REVOLUCIONARIO INSTITUCIONAL\n3) PARTIDO DE LA REVOLUCIÓN DEMOCRÁTICA\n4) PARTIDO MOVIMIENTO CIUDADANO\n5) PARTIDO MORENA\nOmita para saltar\nEscriba la elección (1-5, o enter): "
        while True:
            partido_declarado=input(solicitudPartido)
            try:
                verificador = float(partido_declarado)
            except ValueError:
                if not partido_declarado: # Se verifica que sea o no la omisión
                    Salida_omision = True
                    SalidaPrograma=1
                    Validador_temporal = True
                    break # El break fuerza a salir del verificador ValueError y continúa con la omisión (salida final)
                else: # En caso de introducir algo que no sea omisión o número
                    os.system('cls')
                    print("\n--- Error, favor de escribir un número ---")
                continue
            else:
                break
        if not partido_declarado:
            Salida_omision = True # Para evitar mostrar siguientes preguntas
            SalidaPrograma=1 # Una vez terminado el ciclo while, se sale
            Validador_temporal = True # Se sale del mini while
        else:
            partido_declarado=int(partido_declarado) # Convierte a integer para trabajar con la búsqueda keys
            os.system('cls')
            if partido_declarado in partidos.keys(): # .keys para comprobar si existe el ID
                partido_declarado=partidos[partido_declarado] # Sustituye con el nombre del partido
                print("Usted eligió el partido:",partido_declarado)
                #if(partido_declarado in valor):
                Validador_temporal = True
                break
            else:
                os.system('cls')
                print("\n--- Error, partido" , partido_declarado ,"no encontrado, ingrese un número del 1 al 5 o omita con enter ---")

    if Salida_omision==False: # Si el partido se omitió, ya no pregunta lo demás

        # Input Sexo
        Validador_temporal = False
        while (Validador_temporal==False):
            sexo_declarado=input("\nSexo del votante (HOMBRE ó MUJER)\nEscriba el sexo: ")
            for valor in sexo.values(): # .values para comprobar si contenido existe
                if(sexo_declarado in valor):
                    Validador_temporal = True
                    os.system('cls') # Limpia pantalla para la edad
                    break
            else:
                os.system('cls')
                print("\n--- ERROR, DATO INVÁLIDO ---")

        # Input Edad
        Validador_temporal = False
        while (Validador_temporal == False):
            while True: # Verificador si input es integer
                edad_declarada = input("Edad del votante (mayor o igual a 18)\nEscriba la edad: ")
                try:
                    verificador = float(edad_declarada)
                except ValueError:
                    os.system('cls')
                    print("--- Error, favor de escribir un número ---\n")
                    continue
                else:
                    break
            edad_declarada=int(edad_declarada) # Convierte a integer para trabajar con >=
            if (edad_declarada >= 18):
                Validador_temporal = True
                os.system('cls')
            else:
                os.system('cls')
                print("\n--- ERROR, EDAD INCORRECTA ---\n")

        # Obtiene fecha y hora
        FechaHora = datetime.now()
        # Formato: dd/mm/YY H:M:S
        fecha_string = FechaHora.strftime( "%d/%m/%Y %H:%M:%S" )
        # Print de confirmación para la fecha y hora
        print("Gracias, su registro se realizó correctamente en la siguiente fecha y hora:", fecha_string)
        # Tiempo muerto para permitir confirmar fecha y hora
        print("5...")
        time.sleep(1)
        print("4...")
        time.sleep(1)
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)

        # Crear y agregar a lista
        creaContenido = Sufragio(ContadorID_Actual, partido_declarado, sexo_declarado, edad_declarada, fecha_string)
        Sufragios.extend([ContadorID_Actual, partido_declarado, sexo_declarado, edad_declarada, fecha_string])

os.system('cls')
print("\nTipo de lista:", type(Sufragios), " lista:", Sufragios)

# EJERCICIO 4: CODIFICA LO NECESARIO PARA SERIALIZAR A json EL CONENIDO
# DE LA LISTA Sufragios.

Sufragios=json.dumps(Sufragios)
print("\nSerialziación, tipo de lista:", type(Sufragios), " lista:", Sufragios)

# EJERCICIO 5: CODIFICA LO NECESARIO PARA GUARDAR EL CONTENIDO SERIALIZADO
# DE LA LISTA, EN UN ARCHIVO LLAMADO Sufragios.json, EN EL MISMO 
# DIRECTORIO DE TRABAJO EN DONDE SE ENCUENTRA EL ARCHIVO.
# SI EL ARCHIVO YA EXISTE, HAY QUE ELIMINARLO ANTES.

with open('Sufragios.json', 'w', encoding='utf-8') as f:
    json.dump(Sufragios, f, ensure_ascii=False, indent=4)
    print("\n--- Se ha guardado correctamente el archivo Sufragios.json con los datos ---\n")

# FIN DEL TRABAJO Y DEL SEMESTRE.
