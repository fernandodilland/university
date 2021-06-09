"""
Materia: Programación avanzada (Grupo 21), Profesor: Dr. José Felipe Ramirez Ramirez.
Programa realizado por: Fernando Dilland Mireles Cisneros, 1837532.
"""

# Información conocida:
dinero_disponible = 500.00 # Pesos.
velocidad_constante_coche = 80 # Kilómetros por hora.

# Introducción al programa:
print("\nBienvenido(a) al programa de calculo de distancia y tiempo del coche:")

print("El presupuesto disponible es: ${0:<.2f} pesos".format(dinero_disponible)," y va a: ",velocidad_constante_coche,"km/h",sep="")

# Captura y validación de "rendimiento_variable_disponible":
mensaje_solicitud = "\nIntroduzca el rendimiento: " # Se almacena en "mensaje_solicitud" el texto solicitante.
while True:
    rendimiento_variable_disponible = input(mensaje_solicitud)

    try: # Revisa en primera instancia si lo declarado es número positivo (si declara un número), de lo contrario Error #1.
        rendimiento_variable_disponible = float(rendimiento_variable_disponible)
        if rendimiento_variable_disponible  <= 0:
            mensaje_solicitud = "\nError #1, Ha introducido un número no positivo.\nIntroduzca el rendimiento: "
            continue
        estado_revision_declarado = True

    except ValueError: # En caso de ser una declaración no-número en "ValueError" ejecuta el Error #2.
        estado_revision_declarado = False
        mensaje_solicitud = "\nError #2, Ha introducido un carácter no permitido.\nIntroduzca el rendimiento: "

    if estado_revision_declarado:
        break

# Captura y validación de "precio-litro":
mensaje_solicitud = "\nIntroduzca el precio por cada litro de combustible: " # Se almacena en "mensaje_solicitud" el texto solicitante.
while True:
    gasolina_precio_litro = input(mensaje_solicitud)

    try: # Revisa en primera instancia si lo declarado es número positivo (si declara un número), de lo contrario Error #1.
        gasolina_precio_litro = float(gasolina_precio_litro)
        if gasolina_precio_litro  <= 0:
            mensaje_solicitud = "\nError #3, Ha introducido un número no positivo.\nIntroduzca el precio por cada litro de combustible: "
            continue
        estado_revision_declarado = True

    except ValueError: # En caso de ser una declaración no-número en "ValueError" ejecuta el Error #2.
        estado_revision_declarado = False
        mensaje_solicitud = "\nError #4, Ha introducido un carácter no permitido.\nIntroduzca el precio por cada litro de combustible: "

    if estado_revision_declarado:
        break

# Cálculos del programa:
combustible_disponible = dinero_disponible / gasolina_precio_litro # Litro(s) en disponibilidad.
distancia_recorrida = combustible_disponible * rendimiento_variable_disponible # Kilometro(s) que se logran recorrer.
tiempo_decimal = distancia_recorrida / velocidad_constante_coche # Hora(s) y minuto(s) en base a 100.
tiempo_hora = int(tiempo_decimal) # Hora(s).
tiempo_minutos = int((tiempo_decimal - tiempo_hora) * 60)

# Impresión de resultados:
print("\n------\nCon ${0:<.2f} pesos".format(dinero_disponible),sep="") # Presupuesto
print("se recorren:",round(distancia_recorrida,2),"Km") # Distancia
print("en:",tiempo_hora,"horas y", tiempo_minutos, "minutos.\n------") #Tiempo
