Proceso actividadCaracterVocal
	// Código hecho por: Fernando Dilland Mireles Cisneros (1837532).
	// Escribir un programa que pida al usuario un carácter y que imprima en la pantalla si el carácter es una
	// vocal u otro carácter
	
	definir caracterDeclarado Como Caracter
	
	Escribir  "" 
	Escribir "<< Bienvenido al programa de validar Caracter >>" 
	Escribir  "" 
	
	Escribir "Ingrese un carácter (en minusculas):"
	Leer caracterDeclarado
	
	// Sistema (todo junto)
	Escribir "--------------------------"
	
	si caracterDeclarado == "a" o caracterDeclarado == "e" o caracterDeclarado == "i" o caracterDeclarado == "o" o caracterDeclarado == "u" Entonces
		Escribir "El carácter ", caracterDeclarado, " es una vocal"
	SiNo
		Escribir "El carácter ", caracterDeclarado, " es una consonante"
	FinSi
	
FinProceso
