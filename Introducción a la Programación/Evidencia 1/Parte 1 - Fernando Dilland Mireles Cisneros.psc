// Fernando Dilland Mireles Cisneros

Proceso Actividad1Restaurant
	
	Escribir "Precios del restaurant: Orden de tacos (5) $80, Bebidas $15 y postre $10."
	
	// Se toma la orden al cliente
	Escribir "Escriba la cantidad de órdenes de tacos a llevar:"
	Leer tacos
	Escribir "Escriba la cantidad de bebidas a llevar"
	Leer bebidas
	Escribir "Escriba la cantidad de postres a llevar"
	Leer postres
	
	// Se calculan los precios
	Totaltacos <- tacos * 80
	Totalbebidas <- bebidas * 15
	Totalpostres <- postres * 10
	TotalNormal <- Totaltacos + Totalbebidas + Totalpostres
	Descuento <- TotalNormal * .05
	ConDescuento <- TotalNormal - Descuento
	
	// Se muestra la inforamción
	Escribir "-----------------------------"
	Si tacos > 0 Entonces
		Escribir tacos ," órden(es) de Tacos cuestan: $", Totaltacos
	FinSi
	
	Si bebidas > 0 Entonces
		Escribir bebidas ," Bebida(s): $", Totalbebidas
	FinSi
	
	Si postres > 0 Entonces
		Escribir postres ," Postre(s): $", Totalpostres
	FinSi
	
	Si tacos = 0 o bebidas = 0 o postres = 0 Entonces
		Escribir "-----------------------------"
		Escribir "El monto total es: $", TotalNormal
	SiNo
		Escribir "Se aplicó un descuento por: $", Descuento
		Escribir "-----------------------------"
		Escribir "El monto total con el descuento es: $", ConDescuento
	FinSi

FinProceso
