# histograma de linea
import matplotlib.pyplot as plt
import numpy as np

cantidades_estudiantes = [22,23,21,22,21,22,19,19,19,19,19,20,19,19,18,19,18,18,19,21]
edades = [18,19,20,21,22,23]

plt.hist(cantidades_estudiantes, edades, edgecolor='black')

#Titulo Eje X
plt.xlabel("Edades")

#Titulo Eje Y
plt.ylabel("Cantidad de Estudiantes")

#Titulo de la Gráfica
plt.title("Histograma con Columna Edad")

plt.savefig('histograma.png')

plt.show()