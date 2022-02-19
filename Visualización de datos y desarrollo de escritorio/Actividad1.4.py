# histograma de linea
import matplotlib.pyplot as plt
import numpy as np

cantidades_mamas = [54,37,36,50,23,35,45,45,55,40,39,54,48,48,42,47,46,33,42,47]
edades_mamas = [23,33,35,36,37,39,40,42,45,46,47,48,50,54,55]

plt.hist(cantidades_mamas, edades_mamas, edgecolor='black')

#Titulo Eje X
plt.xlabel("Edades")

#Titulo Eje Y
plt.ylabel("Cantidad de personas")

#Titulo de la Gráfica
plt.title("Histograma con Edad de Mamás")

plt.show()

cantidades_papas = [62,39,39,45,26,39,47,46,48,43,48,59,55,50,39,50,52,35,45,48]
edades_papas = [26,35,39,43,45,46,47,48,50,52,55,59,62]

plt.hist(cantidades_papas, edades_papas, edgecolor='black')

#Titulo Eje X
plt.xlabel("Edades")

#Titulo Eje Y
plt.ylabel("Cantidad de personas")

#Titulo de la Gráfica
plt.title("Histograma con Edad de Papás")

plt.show()