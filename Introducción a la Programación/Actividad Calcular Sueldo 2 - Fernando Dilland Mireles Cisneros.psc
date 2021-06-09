Proceso actividadCalcularSueldo
	// Código hecho por: Fernando Dilland Mireles Cisneros (1837532), Grupo 14.
	// Escribir un programa que calcule el suelo de un empleado. Solicitar al empleado cuántas horas
	// Trabajo a la semana y el pago por hora. En esta empresa los empleados trabajanb por lo general 8 horas
	// Diarias y 5 días a la semana, es decir 40 horas a la semana. Si un trabajador super alas 40 horas
	// Quiere decir que trabajó horas extras. Estas(cada una) se pagan al triple de una hora normal.
	
	Definir horasTrabajadasPorSemana, guardaHorasExtra, sueldoTotal Como Entero
	horasTrabajadasPorSemana <- 40
	guardaHorasExtra <- 0
	Escribir  "" 
	Escribir "<< Bienvenido al programa de Calcular Sueldo >>" 
	Escribir  "" 
	
	Escribir "Ingrese la cantidad de horas que trabajó el empleado en la semana:"
	Leer horasTrabajadasPorSemana
	
	Escribir "Ingrese la cantidad del pago por hora: "
	Leer pagoPorHora
	
	si horasTrabajadasPorSemana>40 Entonces
		guardaHorasExtra <- horasTrabajadasPorSemana-40
		sueldoTotal <- ((horasTrabajadasPorSemana-guardaHorasExtra)*pagoPorHora) + ((guardaHorasExtra*pagoPorHora)*3)
		
	sino sueldoTotal <- horasTrabajadasPorSemana*pagoPorHora
		
	FinSi
	
	Escribir  "" 
	Escribir "--------------------------"
	Escribir  "El sueldo total es: ", sueldoTotal
	Escribir  ""
	
FinProceso
