Proceso actividadOperacionesAritmeticas
	// Código hecho por: Fernando Dilland Mireles Cisneros (1837532), Grupo 14.
	// Escribir un programa que realice las operaciones aritméticas
	// (suma, resta, multiplicación y división). El usuario podrá indicar los números
	// a utilizar y la operación que desea realizar. Es decir el programa
	// sólo realizará una de las 4 operaciones, la que el usuario indique.
	
	Escribir  "" 
	Escribir "<< Bienvenido al programa de Operaciones Aritmeticas >>" 
	Escribir  "" 
	
	Escribir "Escriba el número 1 usado en la operación: "
	Leer numeroUno
	
	Escribir "Escriba el número 2 usado en la operación: "
	Leer numeroDos
	
	Escribir "Seleccione el tipo de operación aritmética:"
	Escribir "1) Suma"
	Escribir "2) Resta"
	Escribir "3) Multiplicación"
	Escribir "4) División"
	Leer operacionSeleccionada
	
	si operacionSeleccionada == "1" Entonces
		Escribir "------------  SUMA  --------------"
		resultado <- numeroUno+numeroDos
		Escribir "El resultado es: ", resultado
	SiNo
		si operacionSeleccionada == "2" Entonces
			Escribir "------------  Resta  --------------"
			resultado <- numeroUno-numeroDos
			Escribir "El resultado es: ", resultado
		SiNo
			si operacionSeleccionada == "3" Entonces
				Escribir "------------  Multiplicación  --------------"
				resultado <- numeroUno*numeroDos
				Escribir "El resultado es: ", resultado
			SiNo
				si operacionSeleccionada == "4" Entonces
					Escribir "------------  División  --------------"
					resultado <- numeroUno/numeroDos
					Escribir "El resultado es: ", resultado
				FinSi
			FinSi
		FinSi
	FinSi
	
FinProceso
