import matplotlib.pyplot as plt
import numpy as np

Edad_mujer = np.array([18,19,20,21,22,23])
Edad_max_cant_F = np.array([0,3,0,0,2,0])

Edad_hombre = np.array([18,19,20,21,22,23])
Edad_max_cant_M = np.array([2,6,1,3,1,1])

plt.plot(Edad_mujer, Edad_max_cant_F, marker='o', linestyle='dashed', color='#E86DF0', label='MUJERES')
plt.plot(Edad_hombre, Edad_max_cant_M, marker='o', linestyle='dashed', color='#8989F0', label="HOMBRES")
plt.legend(loc='lower right')

#Titulo Eje X
plt.xlabel("Años de edad")

# Titulo Eje Y
plt.ylabel('Cantidad de estudiantes')

#Titulo de la Gráfica
plt.title("Comparativo edades entre Mujeres y Hombres")

plt.grid(True)

plt.savefig('grafica_linea.png')

plt.show()
