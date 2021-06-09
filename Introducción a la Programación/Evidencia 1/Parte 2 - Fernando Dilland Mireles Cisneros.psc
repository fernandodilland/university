// Fernando Dilland Mireles Cisneros

Proceso TablaMultiplicar
	
	// Se solicita cuál tabla desea
	Escribir "Escriba la tabla que le gustaría ver (número de 1 al 10):"
	Leer tablaElegida
	
	Escribir "--------- Tabla de multiplicar del: ", tablaElegida, " ---------"
	
	// Se ingresa al ciclo "para" y se imprime la tabla
	Para contador<-1 hasta 10 Con Paso 1 Hacer
		Escribir "         |        ", tablaElegida, " x " , contador, " = ", tablaElegida*contador, "        |"
	FinPara
	
FinProceso