# Importación de módulos
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

# Construcción de diccionario con datos de imagen proporcionada
"""
dict_datos = {
    "Años": [2015, 2016, 2017, 2018, 2019], # Coordenada "X" (Horizontal)
    "Matrículas": [181033,190169,197381,202039,206640] # Coordenada "Y" (Vertical)
}

# Generación de gráfica de Barra

grafica = plt.bar(dict_datos["Años"],dict_datos["Matrículas"])
plt.ylim(170000, None) # Se define inicio de coordenada "Y" (Vertical)
plt.title('Matrículas')
plt.xlabel('Años')
plt.ylabel('Cantidad')
#plt.show()

# Generación de gráfica de Línea

grafica = plt.plot(dict_datos["Años"],dict_datos["Matrículas"])
plt.ylim(170000, None) # Se define inicio de coordenada "Y" (Vertical)
plt.title('Matrículas')
plt.xlabel('Años')
plt.ylabel('Cantidad')
#plt.show()  # display

# Generación de gráfica de Pie

grafica = plt.pie(dict_datos["Matrículas"],
                explode=[0, 0, 0, 0, 0.2],
                labels = dict_datos["Años"],
                autopct='%.1f%%')
plt.title('Matrículas')
#plt.show()
"""
# Gráfica de disperción con base a filtro
# Buscando la variación de la cuenta que pagan las mujeres, en la cena de los sábados, comparar cuanto pagan las que fuman y las que no fuman
df2 = pd.read_csv("tips.csv")
df2.head()
plt.scatter(df2['total_bill'][df2.sex == 'Female'][df2.day == 'Sat'][df2.time == 'Dinner'][df2.smoker == 'No'],
            df2['tip'][df2.sex == 'Female'][df2.day == 'Sat'][df2.time == 'Dinner'][df2.smoker == 'No'],
            color='blue',
            label='No fumadoras')
plt.scatter(df2['total_bill'][df2.sex == 'Female'][df2.day == 'Sat'][df2.time == 'Dinner'][df2.smoker == 'Yes'],
            df2['size'][df2.sex == 'Female'][df2.day == 'Sat'][df2.time == 'Dinner'][df2.smoker == 'Yes'],
            color='red',
            label='Fumadoras')
plt.xlabel('Factura total')
plt.ylabel('Propina')
plt.legend()
plt.show()

# Gráfica de disperción con base a filtro
# Comprobar es cual es la variación de la cuenta que pagan los hombres, en la comida de los jueves, comparar cuanto pagan los que fuman y los que no fuman.
df2 = pd.read_csv("tips.csv")
df2.head()
plt.scatter(df2['total_bill'][df2.sex == 'Male'][df2.day == 'Thur'][df2.time == 'Lunch'][df2.smoker == 'No'],
            df2['tip'][df2.sex == 'Male'][df2.day == 'Thur'][df2.time == 'Lunch'][df2.smoker == 'No'],
            color='blue',
            label='No fumadores')
plt.scatter(df2['total_bill'][df2.sex == 'Male'][df2.day == 'Thur'][df2.time == 'Lunch'][df2.smoker == 'Yes'],
            df2['size'][df2.sex == 'Male'][df2.day == 'Thur'][df2.time == 'Lunch'][df2.smoker == 'Yes'],
            color='red',
            label='Fumadores')
plt.xlabel('Factura total')
plt.ylabel('Propina')
plt.legend()
plt.show()