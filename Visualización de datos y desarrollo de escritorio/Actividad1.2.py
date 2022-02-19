#Creación de Gráfica de Pie
import matplotlib.pyplot as plt
import numpy as np

x = ['Mujeres', 'Hombres']
y = [5, 15]

colores = ['#E86DF0','#8989F0']

plt.pie(y, labels=x, colors=colores)

plt.title('Comparativo Cuantos son Mujeres y Cuantos Hombres')

plt.grid(True)

plt.show()