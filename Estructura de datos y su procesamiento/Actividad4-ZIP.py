'''Ejemplo para demostrar el manejo de agregado sobre iterables'''
import functools #Necesario para reduce()
import itertools #Necesario para accumulate()

def al_doble(valor1):
    return valor1+valor1
def sumas_dos(valor1,valor2):
    return valor1+valor2

#Demostración de la función zip para combinar dos iterables
lista_numeros = [1,2,3,4,5,6]
lista_letras = 'aeioux'
print(lista_numeros)
print(lista_letras)
resultado_combinado = zip(lista_numeros,lista_letras)
print(f'El tipo del objeto commbinado resultante es {type(resultado_combinado)}')
print(f'El resultado combinado es: {list(resultado_combinado)}')

#Demostración de la función map para procesar cada elemento de una lista
numeros_al_doble = list(map(al_doble, lista_numeros))
print('El doble de cada elemento de la lista original: ')
print(numeros_al_doble)

#Demostración de la función reduce() y accumulate() para agregar elementos a una lista
print(f'La lista de numeros es: {lista_numeros}')
print("El agregado de la lista mediante 'reduce()' es: ")
print(functools.reduce(sumas_dos,lista_numeros))
print("El agregado de la lista mediante 'accumulate()' es: ")
print(list(itertools.accumulate(lista_numeros, sumas_dos)))