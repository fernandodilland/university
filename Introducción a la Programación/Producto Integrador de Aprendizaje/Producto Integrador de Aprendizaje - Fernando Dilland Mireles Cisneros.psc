// Creado por: Fernando Dilland Mireles Cisneros.

SubProceso Funcion_1_Bienvenida
	
	// Introducción al usuario a "Empresa de envíos Fast Turtle"
	Escribir "";
	Escribir "--------- Bienvenido(a) a envíos Fast Turtle ---------";
	Escribir "";
	Escribir "             Conozca nuestras tarifas:";
	Escribir "             Servicio:         Tarifa:";
	Escribir "             Día siguiente.....$147.00";
	Escribir "             2 días............$128.00";
	Escribir "             Terrestre.........$103.00";
	Escribir "";
	Escribir "------------------------------------------------------";
	
FinSubProceso // Fin SubProceso Funcion_1_Bienvenida

// Subproceso recibe las 3 variables para calcular el Peso Volumetrico
SubProceso PesoVolumetricoCalculado <- CalculadorPesoVolumetrico(CantidadLargoPaquete, CantidadAltoPaquete, CantidadAnchoPaquete)
	PesoVolumetricoCalculado <- (CantidadLargoPaquete * CantidadAltoPaquete * CantidadAnchoPaquete)/5000;
FinSubProceso

// Se calcula el precio de envío
SubProceso Funcion_3_SistemaDeCalculo(AlmacenaTipoDeEnvio, AlmacenaContenidoDelEnvio, AlmacenaPesoVolumetrico, AlmacenaPesoFisico, AlmacenaPorcentajeAumento, AlmacenaDistanciaKilometros)
	
	// Se almacenan en las variables las cantidades de tarifas
	TarifaDiaSiguiente <- 147;
	TarifaDosDias <- 128;
	TarifaTerrestre <- 103;

	//AlmacenaTipoDeEnvio = 1 es Día Siguiente, 2 es 2 días, 3 es terrestre
	//AlmacenaContenidoDelEnvio = 1 es sobre, 2 es paquete
	
	Segun AlmacenaContenidoDelEnvio Hacer
		1:
			Segun AlmacenaTipoDeEnvio Hacer
				1:
					Escribir "La tarifa para día siguiente es: $", TarifaDiaSiguiente, " pesos";
					// Se corrige el procentaje por que viene el número en entero, al dividirlo entre 100
					// Queda por ejemplo de 20 a .20 (para depsués hacer la multiplicación y su posterior suma)
					CoreccionPorcentajeAumento<-(AlmacenaPorcentajeAumento/100);
					CantidadDeAumento <- TarifaDiaSiguiente*CoreccionPorcentajeAumento;
					PrecioSubFinalConDescuentoDistanciaKM <- TarifaDiaSiguiente+CantidadDeAumento;
				2:
					Escribir "La tarifa para dos días es: $", TarifaDosDias, " pesos";
					CoreccionPorcentajeAumento<-(AlmacenaPorcentajeAumento/100);
					CantidadDeAumento <- TarifaDosDias*CoreccionPorcentajeAumento;
					PrecioSubFinalConDescuentoDistanciaKM <- TarifaDosDias+CantidadDeAumento;
				3: 
					Escribir "La tarifa Terrestre es: $", TarifaTerrestre, " pesos";
					CoreccionPorcentajeAumento<-(AlmacenaPorcentajeAumento/100);
					CantidadDeAumento <- TarifaTerrestre*CoreccionPorcentajeAumento;
					PrecioSubFinalConDescuentoDistanciaKM <- TarifaTerrestre+CantidadDeAumento;
			FinSegun
			
			Escribir "El porcentaje de aumento por los ", AlmacenaDistanciaKilometros , " KM es: ", AlmacenaPorcentajeAumento,"%, equivale a: $", CantidadDeAumento, " pesos";
			Escribir "----------------------------------------------";
			Escribir "        El Total del envío del sobre es: $", PrecioSubFinalConDescuentoDistanciaKM, " pesos";
			
		2:
			// Operacion para conocer si el Peso Volumetrico es mayor al Peso Físico
			// En caso de aplicar, se toma el peso físico para calcular el precio final con sobreprecio
			Si AlmacenaPesoVolumetrico>AlmacenaPesoFisico
				Entonces
					PesoAConsiderarParaAmparar <- AlmacenaPesoVolumetrico;
					Escribir "Se tomó en cuenta el Peso Volumétrico (para su envío)";
			SiNo
				PesoAConsiderarParaAmparar <- AlmacenaPesoFisico;
				Escribir "Se tomó en cuenta el Peso Físico (para su envío)";
			FinSi
			
			Segun AlmacenaTipoDeEnvio Hacer
				1:
					Escribir "La tarifa para día siguiente es: $", TarifaDiaSiguiente, " pesos";
						CoreccionPorcentajeAumento<-(AlmacenaPorcentajeAumento/100);
						CantidadDeAumento <- TarifaDiaSiguiente*CoreccionPorcentajeAumento;
						PrecioSubFinalConDescuentoDistanciaKM <- TarifaDiaSiguiente+CantidadDeAumento;
					Escribir "El porcentaje de aumento por los ", AlmacenaDistanciaKilometros , " KM es: ", AlmacenaPorcentajeAumento,"%, equivale a: $", CantidadDeAumento, " pesos";
					Escribir "----------------------------------------------";
					Escribir "El subtotal del envío es: $", PrecioSubFinalConDescuentoDistanciaKM, " pesos";
					Escribir "----------------------------------------------";
					
					Si PesoAConsiderarParaAmparar<=1 Entonces
						Escribir "No se cobra sobreprecio por ser menos de 1 Kg";
							PrecioFinalPaquete <- PrecioSubFinalConDescuentoDistanciaKM;
						// No hay sobreprecio por exceder el peso permitido (1KG en Dia Siguiente)
					Sino
							GuardaPesoExtra <- PesoAConsiderarParaAmparar-1;
							CantidadPorPesoExtra <- GuardaPesoExtra*19;
						Escribir "Sobreprecio por: ",GuardaPesoExtra," Kg de más ($19 c/u) = $", CantidadPorPesoExtra," pesos";
							PrecioFinalPaquete <- CantidadPorPesoExtra+PrecioSubFinalConDescuentoDistanciaKM;
						Escribir "Se cobra $", PrecioSubFinalConDescuentoDistanciaKM ," + $", CantidadPorPesoExtra;
						Escribir "----------------------------------------------";
					FinSi
					
				2:
					Escribir "La tarifa para dos días es: $", TarifaDosDias, " pesos";
						CoreccionPorcentajeAumento<-(AlmacenaPorcentajeAumento/100);
						CantidadDeAumento <- TarifaDosDias*CoreccionPorcentajeAumento;
						PrecioSubFinalConDescuentoDistanciaKM <- TarifaDosDias+CantidadDeAumento;
					Escribir "El porcentaje de aumento por los ", AlmacenaDistanciaKilometros , " KM es: ", AlmacenaPorcentajeAumento,"%, equivale a: $", CantidadDeAumento, " pesos";
					Escribir "----------------------------------------------";
					Escribir "El subtotal del envío es: $", PrecioSubFinalConDescuentoDistanciaKM, " pesos";
					Escribir "----------------------------------------------";
					
					Si PesoAConsiderarParaAmparar<=2 Entonces
						Escribir "No se cobra sobreprecio por ser menos de 2 Kg"
							PrecioFinalPaquete <- PrecioSubFinalConDescuentoDistanciaKM;
					Sino
							GuardaPesoExtra <- PesoAConsiderarParaAmparar-2;
							CantidadPorPesoExtra <- GuardaPesoExtra*10;
						Escribir "Sobreprecio por: ",GuardaPesoExtra," Kg de más ($10 c/u) = $", CantidadPorPesoExtra," pesos";
							PrecioFinalPaquete <- CantidadPorPesoExtra+PrecioSubFinalConDescuentoDistanciaKM;
						Escribir "Se cobra $", PrecioSubFinalConDescuentoDistanciaKM ," + $", CantidadPorPesoExtra;
						Escribir "----------------------------------------------";
					FinSi
					
				3: 
					Escribir "La tarifa para envío terrestre es: $", TarifaTerrestre, " pesos";
						CoreccionPorcentajeAumento<-(AlmacenaPorcentajeAumento/100);
						CantidadDeAumento <- TarifaTerrestre*CoreccionPorcentajeAumento
						PrecioSubFinalConDescuentoDistanciaKM <- TarifaTerrestre+CantidadDeAumento;
					Escribir "El porcentaje de aumento por los ", AlmacenaDistanciaKilometros , " KM es: ", AlmacenaPorcentajeAumento,"%, equivale a: $", CantidadDeAumento, " pesos";
					Escribir "----------------------------------------------";
					Escribir "El subtotal del envío es: $", PrecioSubFinalConDescuentoDistanciaKM, " pesos";
					Escribir "----------------------------------------------";
					
					Si PesoAConsiderarParaAmparar<=5 Entonces
						Escribir "No se cobra sobreprecio por ser menos de 5 Kg";
							PrecioFinalPaquete <- PrecioSubFinalConDescuentoDistanciaKM;
					Sino
							GuardaPesoExtra <- PesoAConsiderarParaAmparar-5;
							CantidadPorPesoExtra <- GuardaPesoExtra*8;
						Escribir "Sobreprecio por: ",GuardaPesoExtra," Kg de más ($8 c/u) = $", CantidadPorPesoExtra," pesos";
						PrecioFinalPaquete <- CantidadPorPesoExtra+PrecioSubFinalConDescuentoDistanciaKM;
						Escribir "Se cobra $", PrecioSubFinalConDescuentoDistanciaKM ," + $", CantidadPorPesoExtra;
						Escribir "----------------------------------------------";
					FinSi
					
			FinSegun
			Escribir "        El total del envío del paquete es: $", PrecioFinalPaquete, " pesos";
	FinSegun
	
FinSubProceso

// Proceso para calcular el aumento (porcentaje) a la tarifa conforme a la distancia en kilómetros
SubProceso ReferenciadorKM<-PorcentajeDeAumentoATarifaNormal(DistanciaKilometrosRecibido)
	Si DistanciaKilometrosRecibido>=0 y DistanciaKilometrosRecibido<=250 Entonces
		ReferenciadorKM<-0;
	SiNo
		Si DistanciaKilometrosRecibido>=251 y DistanciaKilometrosRecibido<=500 Entonces
			ReferenciadorKM<-20;
			
		SiNo
			Si DistanciaKilometrosRecibido>=501 y DistanciaKilometrosRecibido<=1000 Entonces
				ReferenciadorKM<-40;
			SiNo
				Si DistanciaKilometrosRecibido>=1001 y DistanciaKilometrosRecibido<=1600 Entonces
					ReferenciadorKM<-80;
				SiNo
					Si DistanciaKilometrosRecibido>=1601 y DistanciaKilometrosRecibido<=2200 Entonces
						ReferenciadorKM<-90;
					SiNo
						Si DistanciaKilometrosRecibido>=2201 y DistanciaKilometrosRecibido<=2800 Entonces
							ReferenciadorKM<-100;
						Sino
							ReferenciadorKM<-200;
						FinSi

					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinSubProceso

// Subproceso inicializa el sistema de envío.
SubProceso Funcion_2_SistemaDeEnvio
	
	// Se definen estas variables en específico por si sucede situación #A2 (seleccionar "sobre")
	PesoPaquete <- 0;
	LargoPaquete <- 0;
	AltoPaquete <- 0;
	AnchoPaquete <- 0;
	
	Definir VariableAlmacenaSiEsSobre Como Logico; // Se hace "falso o verdadero" para definir el caso.
		VariableAlmacenaSiEsSobre<-falso; // Se crea esta variable para definir si el sistema funcionará con sobre o paquete.
	
	Limpiar Pantalla
	Escribir "Escriba las siguientes características de su envío:";
	Escribir "";
	Escribir "¿Le gustaría enviar un sobre o un paquete?";
	Escribir "1) Sobre";
	Escribir "2) Paquete";
	Escribir "Escriba la opción deseada (1-2):";
		Leer ContenidoDelEnvio;
	Escribir "----------------------------------------------";
	
	Si ContenidoDelEnvio=1 Entonces //Si usuario selecciona "sobre", se aplica la situación #A2 (no preguntar peso ni dimensiones, ni mostrarlas al final)
		VariableAlmacenaSiEsSobre<-verdadero;
	FinSi
	
	Limpiar Pantalla
	Escribir "¿Qué tipo de envío le gustaría hacer?";
	Escribir "1) Día siguiente";
	Escribir "2) 2 días";
	Escribir "3) Terrestre";
	Escribir "Escriba la opción deseada (1-3):";
		Leer TipoDeEnvioDeseado;
	Escribir "----------------------------------------------";
	
	Limpiar Pantalla
	Escribir "Distancia de envío (kilómetros):";
		Leer DistanciaKilometros;
	Escribir "----------------------------------------------";

	// Nota de desarrollo: La situación #A1 (seleccionar "paquete") muestra las siguientes preguntas, situación #A2 (seleccionar "sobre") no despliega 
	Si VariableAlmacenaSiEsSobre=falso Entonces
		
		Limpiar Pantalla
		Escribir "Peso físico (kilogramos):";
			Leer PesoPaquete;
		Escribir "----------------------------------------------";
		
		Limpiar Pantalla
		Escribir "Largo (centímetros):";
			Leer LargoPaquete;
		Escribir "Alto (centímetros):";
			Leer AltoPaquete;
		Escribir "Ancho (centímetros):";
			Leer AnchoPaquete;
		Escribir "----------------------------------------------";
		
	FinSi
	// Nota de desarrollo: Se mantienen (las variables) con "0" en situación #A2, no se usarán en un futuro en la situación mencionada
	
	// Se solicita al subproceso la cantidad de aumento (porcentaje) conforeme a los kilómetros recorridos
	PorcentajeAumento<-PorcentajeDeAumentoATarifaNormal(DistanciaKilometros);
	
	// Se envía al subproceso las 3 variables para calcular el Peso Volumétrico
	PesoVolumetrico<-CalculadorPesoVolumetrico(LargoPaquete, AltoPaquete, AnchoPaquete);
	
	Limpiar Pantalla
	Escribir "------------------ Confirmación de envío ------------------"
	
	Si VariableAlmacenaSiEsSobre=falso Entonces
		Escribir "Las dimensiones de su paquete son: ",LargoPaquete, "X", AltoPaquete, "X", AnchoPaquete;
		Escribir "Peso físico: ", PesoPaquete, " Kg, Peso volumétrico: ", PesoVolumetrico;
	SiNo
		Escribir "(Usted enviará un sobre, no aplica dimensiones ni pesos)";
	FinSi
	
	// Se manda a llamar la Función con la información para calcular el precio de envío del paquete o sobre
	Funcion_3_SistemaDeCalculo(TipoDeEnvioDeseado, ContenidoDelEnvio, PesoVolumetrico, PesoPaquete, PorcentajeAumento, DistanciaKilometros)

	Escribir "----------------------------------------------";
	Escribir "Haga enter para continuar";
		Leer Continuacion;
FinSubProceso

Proceso PIAProgramacion
	
	// Se manda a llamar el Subproceso "Funcion_1_Bienvenida"
	Funcion_1_Bienvenida;
	DeseaHacerEnvio <- 1; // No.0) Ya envió, No.1) Si desea enviar nuevo, No.2) No desea enviar nada -> (3 situaciones)
	DeseaHacerEnvioOtraVez <- 1;
	GuardaSegundaVezRealizado <- 0; // Empieza en 0 el primer ciclo, a partir del segundo ciclo cambia a 1
	
	Mientras DeseaHacerEnvioOtraVez = 1 Hacer
		
		Mientras GuardaSegundaVezRealizado=0 Hacer
			Escribir "";
			Escribir "¿Le gustaría hacer un envío con nosotros?";
			Escribir "1) Si";
			Escribir "2) No"
			Escribir "Escriba la opción deseada (1-2):";
			Leer DeseaHacerEnvio;
			GuardaSegundaVezRealizado <- 1; //Almacena para salir del Mientras
		FinMientras
		
		// Sistema de envíos (si desea hacer envío) 
		Mientras DeseaHacerEnvio=1 Hacer
			
			//Se ejecuta el sistema de envío en el SubProceso 
			Funcion_2_SistemaDeEnvio;
			
			// Variable "DeseaHacerEnvio" almacena que se ingresó al sistema de envíos (el 0)
			DeseaHacerEnvio <- 0;
		FinMientras
		
		// Proceso para limpia "DeseaHacerEnvioOtraVez" para reiniciar o finalizar proceso
		Si DeseaHacerEnvio=2 Entonces
			DeseaHacerEnvioOtraVez <- 2;
		SiNo
			DeseaHacerEnvioOtraVez <- 0;
		FinSi
		
		// Si se ingresó al sistema de envíos 
		Mientras DeseaHacerEnvioOtraVez=0 Hacer
			Limpiar Pantalla
			Escribir "¿Desea hacer otro envío?";
			Escribir "1) Si";
			Escribir "2) No";
			Escribir "Escriba la opción deseada (1-2):";
			Leer DeseaHacerEnvioOtraVez;
			DeseaHacerEnvio <- 1;
		FinMientras
	FinMientras
FinProceso
