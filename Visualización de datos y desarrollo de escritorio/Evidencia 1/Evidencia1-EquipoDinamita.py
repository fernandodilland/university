# Importación de módulos
import matplotlib.pyplot as plt
import pandas as pd

# Construcción de diccionario con datos de imagen proporcionada
dict_datos = {
    "Años": [2015, 2016, 2017, 2018, 2019], # Coordenada "X" (Horizontal)
    "Matrículas": [181033,190169,197381,202039,206640] # Coordenada "Y" (Vertical)
}

# Generación de gráfica de Barra
grafica = plt.bar(dict_datos["Años"],dict_datos["Matrículas"])
plt.ylim(170000, None) # Se define inicio de coordenada "Y" (Vertical)
plt.title('Matrículas') # Título de la gráfica
plt.xlabel('Años') # Título coordenada "X" (Horizontal)
plt.ylabel('Cantidad') # Título coordenada "Y" (Vertical)
plt.show() # Mostrar gráfica

# Generación de gráfica de Línea
grafica = plt.plot(dict_datos["Años"],dict_datos["Matrículas"])
plt.ylim(170000, None) # Se define inicio de coordenada "Y" (Vertical)
plt.title('Matrículas') # Título de la gráfica
plt.xlabel('Años') # Título coordenada "X" (Horizontal)
plt.ylabel('Cantidad') # Título coordenada "Y" (Vertical)
plt.show() # Mostrar gráfica

# Generación de gráfica de Pie
grafica = plt.pie(dict_datos["Matrículas"], # Datos a graficar
                explode=[0, 0, 0, 0, 0.2], # Separar cierta sección
                labels = dict_datos["Años"], # Títulos en cada sección
                autopct='%.1f%%')
plt.title('Matrículas')  # Título de la gráfica
plt.show() # Mostrar gráfica


# Gráfica de disperción con base a filtro
# Buscando la variación de la cuenta que pagan las mujeres, en la cena de los sábados, comparar cuanto pagan las que fuman y las que no fuman
datos = pd.read_csv("tips.csv") # Lectura del archivo .csv
datos.head()
plt.scatter(datos['total_bill'][datos.sex == 'Female'][datos.day == 'Sat'][datos.time == 'Dinner'][datos.smoker == 'No'],
            datos['tip'][datos.sex == 'Female'][datos.day == 'Sat'][datos.time == 'Dinner'][datos.smoker == 'No'],
            color='blue',
            label='No fumadoras')
plt.scatter(datos['total_bill'][datos.sex == 'Female'][datos.day == 'Sat'][datos.time == 'Dinner'][datos.smoker == 'Yes'],
            datos['size'][datos.sex == 'Female'][datos.day == 'Sat'][datos.time == 'Dinner'][datos.smoker == 'Yes'],
            color='red',
            label='Fumadoras')
plt.xlabel('Factura total') # Título coordenada "X" (Horizontal)
plt.ylabel('Propina') # Título coordenada "Y" (Vertical)
plt.legend()
plt.show() # Mostrar gráfica

# Gráfica de disperción con base a filtro
# Comprobar es cual es la variación de la cuenta que pagan los hombres, en la comida de los jueves, comparar cuanto pagan los que fuman y los que no fuman.
datos = pd.read_csv("tips.csv") # Lectura del archivo .csv
datos.head()
plt.scatter(datos['total_bill'][datos.sex == 'Male'][datos.day == 'Thur'][datos.time == 'Lunch'][datos.smoker == 'No'],
            datos['tip'][datos.sex == 'Male'][datos.day == 'Thur'][datos.time == 'Lunch'][datos.smoker == 'No'],
            color='blue',
            label='No fumadores')
plt.scatter(datos['total_bill'][datos.sex == 'Male'][datos.day == 'Thur'][datos.time == 'Lunch'][datos.smoker == 'Yes'],
            datos['size'][datos.sex == 'Male'][datos.day == 'Thur'][datos.time == 'Lunch'][datos.smoker == 'Yes'],
            color='red',
            label='Fumadores')
plt.xlabel('Factura total') # Título coordenada "X" (Horizontal)
plt.ylabel('Propina') # Título coordenada "Y" (Vertical)
plt.legend() # Mostrar recuadro con significado de puntos
plt.show() # Mostrar gráfica

# Gráfica (subplots) con gráficas anteriores
datos = pd.read_csv("tips.csv") # Lectura del archivo .csv
datos.head()
plt.subplot(1, 2, 1)
plt.scatter(datos['total_bill'][datos.sex == 'Female'][datos.day == 'Sat'][datos.time == 'Dinner'][datos.smoker == 'No'],
            datos['tip'][datos.sex == 'Female'][datos.day == 'Sat'][datos.time == 'Dinner'][datos.smoker == 'No'],
            color='blue',
            label='No fumadoras')
plt.scatter(datos['total_bill'][datos.sex == 'Female'][datos.day == 'Sat'][datos.time == 'Dinner'][datos.smoker == 'Yes'],
            datos['size'][datos.sex == 'Female'][datos.day == 'Sat'][datos.time == 'Dinner'][datos.smoker == 'Yes'],
            color='red',
            label='Fumadoras')
print("Cantidad 1:",len(datos['total_bill'][datos.sex == 'Female'][datos.day == 'Sat'][datos.time == 'Dinner'][datos.smoker == 'No'])+len(datos['total_bill'][datos.sex == 'Female'][datos.day == 'Sat'][datos.time == 'Dinner'][datos.smoker == 'Yes']))
plt.xlabel('Factura total') # Título coordenada "X" (Horizontal)
plt.ylabel('Propina') # Título coordenada "Y" (Vertical)
plt.legend() # Mostrar recuadro con significado de puntos
plt.title("Mujeres")

plt.subplot(1, 2, 2)
plt.scatter(datos['total_bill'][datos.sex == 'Male'][datos.day == 'Thur'][datos.time == 'Lunch'][datos.smoker == 'No'],
            datos['tip'][datos.sex == 'Male'][datos.day == 'Thur'][datos.time == 'Lunch'][datos.smoker == 'No'],
            color='blue',
            label='No fumadores')
plt.scatter(datos['total_bill'][datos.sex == 'Male'][datos.day == 'Thur'][datos.time == 'Lunch'][datos.smoker == 'Yes'],
            datos['size'][datos.sex == 'Male'][datos.day == 'Thur'][datos.time == 'Lunch'][datos.smoker == 'Yes'],
            color='red',
            label='Fumadores')
print("Cantidad 2:",len(datos['total_bill'][datos.sex == 'Male'][datos.day == 'Thur'][datos.time == 'Lunch'][datos.smoker == 'No'])+len(datos['total_bill'][datos.sex == 'Male'][datos.day == 'Thur'][datos.time == 'Lunch'][datos.smoker == 'Yes']))
plt.xlabel('Factura total') # Título coordenada "X" (Horizontal)
plt.ylabel('Propina') # Título coordenada "Y" (Vertical)
plt.legend() # Mostrar recuadro con significado de puntos
plt.title("Hombres")

plt.suptitle("Subplots")
plt.show() # Mostrar gráficas en formato Subplots