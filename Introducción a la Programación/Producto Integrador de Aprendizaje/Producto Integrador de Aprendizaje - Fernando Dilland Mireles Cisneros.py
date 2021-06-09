# Creado por: Fernando Dilland Mireles Cisneros

def Funcion_1_Bienvenida():
    # Introducción al usuario a "Empresa de envíos Fast Turtle"
    print ("")
    print ("--------- Bienvenido(a) a envíos Fast Turtle ---------")
    print ("")
    print ("             Conozca nuestras tarifas:")
    print ("             Servicio:         Tarifa:")
    print ("             Día siguiente.....$147.00")
    print ("             2 días............$128.00")
    print ("             Terrestre.........$103.00")
    print ("")
    print ("------------------------------------------------------")
    #Fin Funcion Funcion_1_Bienvenida

# Funcion recibe las 3 variables para calcular el Peso Volumetrico
def CalculadorPesoVolumetrico(CantidadLargoPaquete, CantidadAltoPaquete, CantidadAnchoPaquete):
    PesoVolumetricoCalculado = (CantidadLargoPaquete * CantidadAltoPaquete * CantidadAnchoPaquete)/5000
    return PesoVolumetricoCalculado

# Se calcula el precio de envío
def Funcion_3_SistemaDeCalculo(AlmacenaTipoDeEnvio, AlmacenaContenidoDelEnvio, AlmacenaPesoVolumetrico, AlmacenaPesoFisico, AlmacenaPorcentajeAumento, AlmacenaDistanciaKilometros):
    
    # Se almacenan en las variables las cantidades de tarifas
    TarifaDiaSiguiente = 147
    TarifaDosDias = 128
    TarifaTerrestre = 103
    
    # AlmacenaTipoDeEnvio = 1 es Día Siguiente, 2 es 2 días, 3 es terrestre
    # AlmacenaContenidoDelEnvio = 1 es sobre, 2 es paquete
    if (AlmacenaContenidoDelEnvio == 1):
        if (AlmacenaTipoDeEnvio == 1):
            print( "La tarifa para día siguiente es: $", TarifaDiaSiguiente, " pesos")
            CoreccionPorcentajeAumento = AlmacenaPorcentajeAumento / 100
            CantidadDeAumento = TarifaDiaSiguiente * CoreccionPorcentajeAumento
            PrecioSubFinalConDescuentoDistanciaKM = TarifaDiaSiguiente + CantidadDeAumento
        elif (AlmacenaTipoDeEnvio == 2):
            print("La tarifa para dos días es: $", TarifaDosDias, " pesos")
            CoreccionPorcentajeAumento = AlmacenaPorcentajeAumento/100
            CantidadDeAumento = TarifaDosDias*CoreccionPorcentajeAumento
            PrecioSubFinalConDescuentoDistanciaKM = TarifaDosDias+CantidadDeAumento
        elif (AlmacenaTipoDeEnvio == 3):
            print("La tarifa Terrestre es: $", TarifaTerrestre, " pesos")
            CoreccionPorcentajeAumento = (AlmacenaPorcentajeAumento/100)
            CantidadDeAumento = TarifaTerrestre*CoreccionPorcentajeAumento
            PrecioSubFinalConDescuentoDistanciaKM = TarifaTerrestre+CantidadDeAumento
        
        print("El porcentaje de aumento por los ", AlmacenaDistanciaKilometros , " KM es: ", AlmacenaPorcentajeAumento,"%, equivale a: $", CantidadDeAumento, " pesos")
        print( "----------------------------------------------")
        print( "        El Total del envío del sobre es: $", PrecioSubFinalConDescuentoDistanciaKM, " pesos")
        
    elif (AlmacenaContenidoDelEnvio == 2):
        # Operacion para conocer si el Peso Volumetrico es mayor al Peso Físico
        # En caso de aplicar, se toma el peso físico para calcular el precio final con sobreprecio
        if AlmacenaPesoVolumetrico > AlmacenaPesoFisico:
            PesoAConsiderarParaAmparar = AlmacenaPesoVolumetrico
            print ("Se tomó en cuenta el Peso Volumétrico (para su envío)")
        else:
            PesoAConsiderarParaAmparar = AlmacenaPesoFisico
            print ("Se tomó en cuenta el Peso Físico (para su envío)")

        if (AlmacenaTipoDeEnvio == 1):
            print ("La tarifa para día siguiente es: $", TarifaDiaSiguiente, " pesos")
            CoreccionPorcentajeAumento = AlmacenaPorcentajeAumento / 100
            CantidadDeAumento = TarifaDiaSiguiente * CoreccionPorcentajeAumento
            PrecioSubFinalConDescuentoDistanciaKM = TarifaDiaSiguiente + CantidadDeAumento
            print ("El porcentaje de aumento por los ", AlmacenaDistanciaKilometros , " KM es: ", AlmacenaPorcentajeAumento,"%, equivale a: $", CantidadDeAumento, " pesos")
            print ("----------------------------------------------")
            print ( "El subtotal del envío es: $", PrecioSubFinalConDescuentoDistanciaKM, " pesos")
            print ( "----------------------------------------------")

            if (PesoAConsiderarParaAmparar <= 1):  # No hay sobreprecio por exceder el peso permitido (1KG en Dia Siguiente)
                print ("No se cobra sobreprecio por ser menos de 1 Kg")
                PrecioFinalPaquete = PrecioSubFinalConDescuentoDistanciaKM;
            else:
                GuardaPesoExtra = PesoAConsiderarParaAmparar - 1
                CantidadPorPesoExtra = GuardaPesoExtra * 19
                print ("Sobreprecio por: ",GuardaPesoExtra," Kg de más ($19 c/u) = $", CantidadPorPesoExtra," pesos")
                PrecioFinalPaquete = CantidadPorPesoExtra + PrecioSubFinalConDescuentoDistanciaKM
                print ("Se cobra $", PrecioSubFinalConDescuentoDistanciaKM ," + $", CantidadPorPesoExtra)
                print ("----------------------------------------------")
                
        elif (AlmacenaTipoDeEnvio == 2):
            print ("La tarifa para dos días es: $", TarifaDosDias, " pesos")
            CoreccionPorcentajeAumento = AlmacenaPorcentajeAumento / 100
            CantidadDeAumento = TarifaDosDias * CoreccionPorcentajeAumento
            PrecioSubFinalConDescuentoDistanciaKM = TarifaDosDias+CantidadDeAumento
            print ("El porcentaje de aumento por los ", AlmacenaDistanciaKilometros , " KM es: ", AlmacenaPorcentajeAumento,"%, equivale a: $", CantidadDeAumento, " pesos")
            print ("----------------------------------------------")
            print ( "El subtotal del envío es: $", PrecioSubFinalConDescuentoDistanciaKM, " pesos")
            print ( "----------------------------------------------")
            
            if (PesoAConsiderarParaAmparar <= 2):
                print ("No se cobra sobreprecio por ser menos de 2 Kg")
                PrecioFinalPaquete = PrecioSubFinalConDescuentoDistanciaKM;
            else:
                GuardaPesoExtra = PesoAConsiderarParaAmparar - 2
                CantidadPorPesoExtra = GuardaPesoExtra * 10
                print ("Sobreprecio por: ",GuardaPesoExtra," Kg de más ($10 c/u) = $", CantidadPorPesoExtra," pesos")
                PrecioFinalPaquete = CantidadPorPesoExtra + PrecioSubFinalConDescuentoDistanciaKM
                print ("Se cobra $", PrecioSubFinalConDescuentoDistanciaKM ," + $", CantidadPorPesoExtra)
                print ("----------------------------------------------")
                
        elif (AlmacenaTipoDeEnvio == 3):
            print ("La tarifa para envío terrestre: $", TarifaTerrestre, " pesos")
            CoreccionPorcentajeAumento = AlmacenaPorcentajeAumento / 100
            CantidadDeAumento = TarifaTerrestre * CoreccionPorcentajeAumento
            PrecioSubFinalConDescuentoDistanciaKM = TarifaTerrestre+CantidadDeAumento
            print ("El porcentaje de aumento por los ", AlmacenaDistanciaKilometros , " KM es: ", AlmacenaPorcentajeAumento,"%, equivale a: $", CantidadDeAumento, " pesos")
            print ("----------------------------------------------")
            print ( "El subtotal del envío es: $", PrecioSubFinalConDescuentoDistanciaKM, " pesos")
            print ( "----------------------------------------------")
            
            if (PesoAConsiderarParaAmparar <= 5):
                print ("No se cobra sobreprecio por ser menos de 5 Kg")
                PrecioFinalPaquete = PrecioSubFinalConDescuentoDistanciaKM;
            else:
                GuardaPesoExtra = PesoAConsiderarParaAmparar - 5
                CantidadPorPesoExtra = GuardaPesoExtra * 8
                print ("Sobreprecio por: ",GuardaPesoExtra," Kg de más ($8 c/u) = $", CantidadPorPesoExtra," pesos")
                PrecioFinalPaquete = CantidadPorPesoExtra + PrecioSubFinalConDescuentoDistanciaKM
                print ("Se cobra $", PrecioSubFinalConDescuentoDistanciaKM ," + $", CantidadPorPesoExtra)
                print ("----------------------------------------------")
        print(" El total del envío del paquete es: $", PrecioFinalPaquete, " pesos")
    
 
# Proceso para calcular el aumento (porcentaje) a la tarifa conforme a la distancia en kilómetros
def PorcentajeDeAumentoATarifaNormal(DistanciaKilometrosRecibido):
    if ((DistanciaKilometrosRecibido >= 0) and (DistanciaKilometrosRecibido <= 250)):
        ReferenciadorKM = 0
    else:
        if ((DistanciaKilometrosRecibido >= 251) and (DistanciaKilometrosRecibido <= 500)):
            ReferenciadorKM = 20
        else:
            if ((DistanciaKilometrosRecibido >= 501) and (DistanciaKilometrosRecibido <= 1000)):
                ReferenciadorKM = 40
            else:
                if ((DistanciaKilometrosRecibido >= 1001) and (DistanciaKilometrosRecibido <= 1600)):
                    ReferenciadorKM = 80
            
                else:
                    if ((DistanciaKilometrosRecibido >= 1601) and (DistanciaKilometrosRecibido <= 2200)):
                        ReferenciadorKM = 90
                    else:
                        if ((DistanciaKilometrosRecibido >= 2201) and (DistanciaKilometrosRecibido <= 2800)):
                            ReferenciadorKM = 100
                        else:
                            ReferenciadorKM =200
                            
         
    return ReferenciadorKM
            
           
# Subproceso inicializa el sistema de envío.
def Funcion_2_SistemaDeEnvio():
    
    # Se definen estas variables en específico por si sucede situación #A2 (seleccionar "sobre")
    PesoPaquete = 0
    LargoPaquete = 0
    AltoPaquete = 0
    AnchoPaquete = 0
    
    VariableAlmacenaSiEsSobre = "falso" # Se crea esta variable para definir si el sistema funcionará con sobre o paquete.
    
    print("Escriba las siguientes características de su envío:")
    print("")
    print("¿Le gustaría enviar un sobre o un paquete?")
    print("1) Sobre")
    print("2) Paquete")
    ContenidoDelEnvio = int(input("Escriba la opción deseada (1-2):"))
    print("----------------------------------------------")
    
    if (ContenidoDelEnvio == 1): #Si usuario selecciona "sobre", se aplica la situación #A2 (no preguntar peso ni dimensiones, ni mostrarlas al final)
        VariableAlmacenaSiEsSobre = "verdadero"
    
    print("¿Qué tipo de envío le gustaría hacer?")
    print("1) Día siguiente")
    print("2) 2 días")
    print("3) Terrestre")
    TipoDeEnvioDeseado = int(input("Escriba la opción deseada (1-3):"))
    print("----------------------------------------------")
    
    DistanciaKilometros = int(input("Distancia de envío (kilómetros):"))
    print("----------------------------------------------")
    
    # Nota de desarrollo: La situación #A1 (seleccionar "paquete") muestra las siguientes preguntas, situación #A2 (seleccionar "sobre") no despliega
    if (VariableAlmacenaSiEsSobre == "falso"):
        PesoPaquete = int(input("Peso físico (kilogramos):"))
        LargoPaquete = int(input("Largo (centímetros):"))
        AltoPaquete = int(input("Alto (centímetros):"))
        AnchoPaquete = int(input("Ancho (centímetros):"))
        print("----------------------------------------------")
 
    # Nota de desarrollo: Se mantienen (las variables) con "0" en situación #A2, no se usarán en un futuro en la situación mencionada
    
    # Se solicita al subproceso la cantidad de aumento (porcentaje) conforeme a los kilómetros recorridos
    PorcentajeAumento = PorcentajeDeAumentoATarifaNormal(DistanciaKilometros)
    
    #Se envía al subproceso las 3 variables para calcular el Peso Volumétrico
    PesoVolumetrico = CalculadorPesoVolumetrico(LargoPaquete, AltoPaquete, AnchoPaquete)
    
    print("------------------ Confirmación de envío ------------------")
    
    if (VariableAlmacenaSiEsSobre == "falso"):
        print("Las dimensiones de su paquete son: ",LargoPaquete, "X", AltoPaquete, "X", AnchoPaquete)
        print("Peso físico: ", PesoPaquete, " Kg, Peso volumétrico: ", PesoVolumetrico)
    else:
        print("(Usted enviará un sobre, no aplica dimensiones ni pesos)")
        
    # Se manda a llamar la Función con la información para calcular el precio de envío del paquete o sobre
    Funcion_3_SistemaDeCalculo(TipoDeEnvioDeseado, ContenidoDelEnvio, PesoVolumetrico, PesoPaquete, PorcentajeAumento, DistanciaKilometros)
    
    print("----------------------------------------------")
    #Continuacion = int(input("Haga enter para continuar"))

# Se inicializa funcion PIAProgramacion
# Se manda a llamar el Subproceso "Funcion_1_Bienvenida"
Funcion_1_Bienvenida()
DeseaHacerEnvio = 1
DeseaHacerEnvioOtraVez = 1
GuardaSegundaVezRealizado = 0

while DeseaHacerEnvioOtraVez == 1:
    while GuardaSegundaVezRealizado == 0:
        print("")
        print("¿Le gustaria hacer un envío con nosotros?")
        print("1) Si")
        print("2) No")
        DeseaHacerEnvio = int(input("Escriba la opción deseada (1-2): "))
        GuardaSegundaVezRealizado = 1
        
    while DeseaHacerEnvio == 1: # Sistema de envíos (si desea hacer envío)
        Funcion_2_SistemaDeEnvio() # Se ejecuta el sistema de envío en el SubProceso
        DeseaHacerEnvio = 0

    # Proceso para limpia "DeseaHacerEnvioOtraVez" para reiniciar o finalizar proceso
    if (DeseaHacerEnvio==2):
        DeseaHacerEnvioOtraVez = 2
    else:
        DeseaHacerEnvioOtraVez = 0
    
    # Si se ingresó al sistema de envíos 
    while DeseaHacerEnvioOtraVez == 0:
        print("¿Desea hacer otro envío?")
        print("1) Si")
        print("2) No")
        DeseaHacerEnvioOtraVez = int(input("Escriba la opción deseada (1-2): "))
        DeseaHacerEnvio = 1
        