# Creación de Gráfica de Barra
import matplotlib.pyplot as plt
import numpy as np

# Gráfica 1
x = ['PC', 'Laptop', 'Tablet', 'Smart Phone','Other']
y = [5, 3, 0, 2, 0]

lista_de_barra = plt.bar(x,y)
lista_de_barra[0].set_color('#196cff')
lista_de_barra[1].set_color('#ff80ab')
lista_de_barra[2].set_color('#ff403d') # No visible
lista_de_barra[3].set_color('#ffc738')
lista_de_barra[4].set_color('#07B33D') # No visible

plt.title('Dispositivos usados para entrar a clase')
plt.xlabel('Dispositivo')
plt.ylabel('Cantidad de personas')
plt.grid(True)

plt.show()

# Gráfica 2
x = ['Monterrey', 'San Nicolás', 'Guadalupe', 'Apodaca', 'San Pedro', 'Juárez', 'García', 'Other City', 'Escobedo']
y = [1, 1, 2, 3, 0, 0, 1, 2, 0]

lista_de_barra = plt.bar(x,y)
lista_de_barra[0].set_color('#196cff')
lista_de_barra[1].set_color('#ff80ab')
lista_de_barra[2].set_color('#ff403d')
lista_de_barra[3].set_color('#ffc738')
lista_de_barra[4].set_color('#07B33D') # No visible
lista_de_barra[5].set_color('#07B33D') # No visible
lista_de_barra[6].set_color('#cc660a')
lista_de_barra[7].set_color('#196cff')
lista_de_barra[8].set_color('#ff80ab') # No visible

plt.title('De cual Ciudad/Estado se conecta')
plt.xlabel('Ciudad/Estado')
plt.ylabel('Cantidad de personas')
plt.grid(True)

plt.show()

# Gráfica 3
x = ['Starting', 'In process', 'Good']
y = [0, 9, 1]

lista_de_barra = plt.bar(x,y)
lista_de_barra[0].set_color('#196cff')
lista_de_barra[1].set_color('#ff80ab')
lista_de_barra[2].set_color('#ff403d')

plt.title('Nivel de habla inglesa')
plt.xlabel('Nivel')
plt.ylabel('Cantidad de personas')
plt.grid(True)

plt.show()