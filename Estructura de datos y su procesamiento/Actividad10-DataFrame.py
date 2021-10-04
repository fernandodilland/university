#1 - Definir un diccionario con las ventas por mes (Invente ud. las cifras) para cinco sucursalIterablees (Norte, Centro, Sur, Este y Oeste).
#2 - Crear un df que contendrá los datos del diccionario teniendo un renglón por sucursal.
#3 - Obtener le promedio de venta anual de cada sucursal.
#4 - Obtener el promedio de ventas por mes consdierando la totalidad de las sucursalIterablees.

import pandas as pd
SEPARADOR =  "\n"+("*" * 80) + "\n"

# Punto 1
# Dentro de cada "[]" se encuentran: Norte, Centro, Sur, Este y Oeste
diccionario_ventas_por_mes ={"Enero":[1096209,490821,1279237,441118,1215379], "Febrero":[1089504,247306,669321,771181,708803], "Marzo":[966558,1089386,1406091,533771,1103525],
                             "Abril":[1475398,700408,191849,514360,1312325], "Mayo":[1125689,151367,1000920,576175,507439], "Junio":[552001,201251,1376033,1070815,1081205],
                             "Julio":[619942,929189,408917,889525,578141], "Agosto":[731892,881623,950061,299610,1088085], "Septiembre":[309903,900920,1190240,204404,865270],
                             "Octubre":[542128,933853,1171697,533895,573903], "Noviembre":[469235,1161300,730867,1436646,1058090], "Diciembre":[1145698,1295648,1082557,1486302,235037]}

# Punto 2
dataFrame_ventas = pd.DataFrame(diccionario_ventas_por_mes)

print(dataFrame_ventas)
print(SEPARADOR)

dataFrame_ventas.index = ["Norte","Centro","Sur","Este","Oeste"]

print(dataFrame_ventas)
print(SEPARADOR)

# Punto 3
print("Promedios de venta anual por sucursalIterable:")
for sucursalIterable in dataFrame_ventas.index:
    print(f"{sucursalIterable}: {dataFrame_ventas.loc[sucursalIterable].mean()}")
print(SEPARADOR)

# Punto 4.
print("Promedios por mes:")
print(dataFrame_ventas.mean())
print(SEPARADOR)