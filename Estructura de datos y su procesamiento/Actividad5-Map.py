# 1 - Implementar una función que tome como argumento una fecha de nacimiento
#     y retorne la edad en años CUMPLIDOS para ese dato.

# 2 - Aplicar mediante la función map() la función para el cálculo de la edad
#     recién codificada en el paso 1 sobre una secuencia de fechas de nacimiento (min 4).
#     Desplegar el resultado de la función map, en un dato por renglón a la vez.

import datetime   # Necesario para obtener fecha

def calcular_edad(fecha_declarada): # Función
    fecha_nacimiento = datetime.datetime.strptime(fecha_declarada, "%d/%m/%Y").date()
    fecha_actual = datetime.date.today()
    año = fecha_actual.year - fecha_nacimiento.year

    if fecha_nacimiento.month >= fecha_actual.month and fecha_nacimiento.day > fecha_actual.day:
            año = año - 1
    return año

print("Bienvenido(a) al programa")
print(" --- Mandando a llamar función ---")

fechas_nacimiento = ["12/02/2004","6/04/2002","12/08/1999","12/02/2001", "15/01/2000", "15/10/2000",
                     "17/08/2000","19/08/2000","18/08/2000"] # Lista
print("\nConfirmación de lista:", fechas_nacimiento)
edades_actuales = list(map(calcular_edad, fechas_nacimiento))

for edad in edades_actuales:
    print("La edad es:", edad,"años")
    
print("\n--- Ha finalizado el programa ---")





