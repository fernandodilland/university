from collections import namedtuple

SEPARADOR = ("*" * 20)

Vehiculos= namedtuple("Vehiculos",["marca","año","kilometraje"])
ListaVehiculos=[]

while True:
    print("\nBienvenido Usuario al Menu, porfavor Introduzca los siguientes datos:")
    marca=input("Porfavor ingrese la marca del automovil (x para salir): ")
    if marca=="x":
        break
    else:
        año=input("Porfavor introduzca el año del automovil: ")
        kilometraje=input("Porfavor introduzca el kilometraje del automovil: ")
        TuplaVehiculo = Vehiculos(marca,año,kilometraje)
        ListaVehiculos.append(TuplaVehiculo)

print("\nA continuacion le mostraremos los vehiculos introducidos: ")

for entrada in ListaVehiculos:
    print(entrada.marca)
    print(entrada.año)
    print(entrada.kilometraje)
    print(SEPARADOR)