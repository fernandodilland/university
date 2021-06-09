//Programa por Fernando Dilland Mireles Cisneros (1837532)

Proceso Ejercicio1Evidencia2Veronica
	
		Escribir "Escriba el nombre completo:"
		Leer NombreDeclarado
		Escribir "Escriba Edad:"
		Leer EdadDeclarada
		Escribir "Escriba País:"
		Leer PaisDeclarado
		Escribir "Escriba Género F ó M"
		Leer GeneroDeclarado
		
		GuardaDato <- CalcularCantidad(NombreDeclarado,EdadDeclarada,PaisDeclarado,GeneroDeclarado)
		
FinProceso //aquí termina el proceso, no subproceso

Funcion CantFinal <- CalcularCantidad(NombreDeclarado, EdadDeclarada, PaisDeclarado, GeneroDeclarado) //funcion separada
	
	Count <- 1
	
	PaisVariable2 <- Subcadena(PaisDeclarado, 0, 0)
	
	LongitudCaracter <- Longitud(NombreDeclarado)
	
	AjustaNombre <- Subcadena(NombreDeclarado, 0, 0)
	
	CalculaGeneroDeclarado <- Subcadena(GeneroDeclarado, 0, 0)
	
Para guardadorDato <- 0 Hasta LongitudCaracter - 1 Con Paso 1 Hacer
	
	Si " " == Subcadena(NombreDeclarado, guardadorDato, guardadorDato) Entonces //subadena
				
		Si Subcadena(NombreDeclarado, guardadorDato + 1, guardadorDato + 1) == " " Entonces
					
			Count <- 1 + Count
		SiNo
					
			concatenacion <- Subcadena(NombreDeclarado, guardadorDato + 1, guardadorDato + 1)
					
					
			AjustaNombre <- AjustaNombre + concatenacion
					
				FinSi
			FinSi
			
FinPara
	
	
	SumFinal <- AjustaNombre + PaisVariable2 + CalculaGeneroDeclarado + EdadDeclarada
	
	Escribir "El código de seguridad es:  ",  SumFinal
	
FinFuncion

SubProceso SistemaCantidad (numDatos, numSimbolo)
	
	Para guardadorDato <- 1 hasta numDatos Hacer
		Escribir Sin Saltar numSimbolo
		
	FinPara
	
FinSubProceso
