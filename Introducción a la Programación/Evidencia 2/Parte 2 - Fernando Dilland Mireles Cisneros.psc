//Programa por Fernando Dilland Mireles Cisneros (1837532)

Proceso Ejercicio2Evidencia2Veronica
	
	Escribir "Numero inicial: "
	Leer Declaracion
	
	Escribir "1 - Suma"
	Escribir "2 - Resta"
	Escribir "3 - Division"
	Escribir "4 - Multiplicacion"
	Escribir "Tipo de tabla que desea: "
	
	Leer TablaSeleccionada
	
	Escribir "1 - Resultado de número"
	Escribir "2 - Resultado con carácter"
	Escribir "Tipo de resultado: "
	
	Leer TipoResultado
	
	TextoGenerador <- ConvertirATexto(TipoResultado)
	Si TextoGenerador == "1" Entonces
	guardaDato1 <- GeneracionTabla(Declaracion, TablaSeleccionada)
SiNo
	
	Escribir "Caracter a usar para separar: "
	Leer caracterParaSeparar
	guardaDato1 <- TablaGeneradaSistema(Declaracion, TablaSeleccionada, caracterParaSeparar)
	
FinSi

FinProceso
	
Funcion TablaGeneradaSistema <- TablaGeneradaSistema(Declaracion, TablaSeleccionada, caracterParaSeparar)
	tipoTabla <- ConvertirATexto(TablaSeleccionada)
	Si tipoTabla == "1" Entonces
	Para valor1 <- 1 Hasta 10 Con Paso 1 Hacer
		SeparadorGuardado <- "" 
	Para guardaDato1 <- 1 Hasta valor1+Declaracion Con paso 1 Hacer 
		valor2 <- caracterParaSeparar + SeparadorGuardado
	FinPara		
	Escribir Declaracion, " + ", valor1," =  ", SeparadorGuardado		
	FinPara		
	SiNo
	Si tipoTabla == "2" Entonces
	Para valor1 <- 1 Hasta 10 Con Paso 1 Hacer
		valor2 <- ""
	Para guardaDato1 <- 1 Hasta Declaracion-valor1 Con paso 1 Hacer
		valor2 <- caracterParaSeparar + SeparadorGuardado	
	FinPara
	Escribir Declaracion, " - ", valor1," =  ", SeparadorGuardado	
	FinPara
		SiNo
		Si tipoTabla == "3" Entonces
		Para valor1 <- 1 Hasta 10 Con Paso 1 Hacer
			valor2 <- ""
		Para guardaDato1 <- 1 Hasta trunc(Declaracion / valor1) Con paso 1 Hacer
			SeparadorGuardado<- caracterParaSeparar + SeparadorGuardado	
		FinPara
		Escribir Declaracion, " / ", valor1," =  ", SeparadorGuardado	
		
		FinPara
		SiNo
		Si tipoTabla == "4" Entonces
		Para valor1 <- 1 Hasta 10 Con Paso 1 Hacer
		valor2 <- ""
		Para guardaDato1 <- 1 Hasta Declaracion*valor1 Con paso 1 Hacer
			
			valor2 <- caracterParaSeparar + SeparadorGuardado	
		FinPara
		Escribir Declaracion, " * ", valor1, " =  ", SeparadorGuardado	
		FinPara
		FinSi
		
	FinSi
		FinSi
		FinSi
		FinFuncion

			Funcion GeneracionTabla <- GeneracionTabla(Declaracion, TablaSeleccionada)
			tipoTabla <- ConvertirATexto(TablaSeleccionada)
			Si tipoTabla == "1" Entonces
			Para valor1 <- 1 Hasta 10 Con Paso 1 Hacer
			Escribir Declaracion , "  +  ", valor1, " = ", Declaracion+ valor1
			FinPara
			SiNo
			Si tipoTabla == "2" Entonces
			Para valor1 <- 1 Hasta 10 Con Paso 1 Hacer
				Escribir Declaracion , " - ", valor1, " =  ", Declaracion- valor1
				
			FinPara
			SiNo
			Si tipoTabla == "3" Entonces
			Para valor1 <- 1 Hasta 10 Con Paso 1 Hacer
			Escribir Declaracion, " / ", valor1, " =  ", trunc(Declaracion / valor1)
			FinPara
			SiNo
			Si tipoTabla == "4" Entonces
			Para valor1 <- 1 Hasta 10 Con Paso 1 Hacer
			Escribir Declaracion , " * ", valor1, " =  ", Declaracion * valor1
			FinPara
			FinSi
			FinSi
			FinSi
			FinSi
FinFuncion