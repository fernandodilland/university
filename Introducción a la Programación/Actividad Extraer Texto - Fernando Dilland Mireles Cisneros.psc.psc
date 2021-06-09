Proceso actividadExtraerTexto
	// Código hecho por: Fernando Dilland Mireles Cisneros (1837532), Grupo 14.
	// Escribir un programa que permita extraer de un texto una parte del mismo.
	// El programa debe solicitar el texto a procesar. Para especificar que
	// se va a extraer, se debe solicitar la posición de inicio de
	// la extracción y cuántos carácteres desea extraer.
	
	Escribir "Ingrese el texto al cual le vamos a extraer: "
	Leer textoParaExtraer
	
	Escribir "Ingrese la posición inicial de la extración del texto (número): "
	Leer posicionInicial
	
	Escribir "Ingrese la cantidad de carácteres a extraer: "
	Leer cantidadCaracteres
	
	// Corregimos la posición inicial para que empieze de la letra indicada.
	correccionPosicionInicial <- posicionInicial-1
	
	textoExtraido <- subcadena(textoParaExtraer,correccionPosicionInicial,cantidadCaracteres)
	
	Escribir "El texto extraído es: ", textoExtraido
	
FinProceso