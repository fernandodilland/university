# ********************************* AQUI EMPIEZA PAGOS ***********************************************

# Fernando Chavez, Juan de Dios <<<<<<<<<<<<<<<<<<<<<<

# Como primer paso, extraemos los datos del archivo en donde los tenemos
# luego, de eso, lo colocamos en un vector que llamaremos pagosAgua
pagosAgua = c(57,70,100,100,100,100,100,100,101,101,
              104.05,105,108,123,150,150,207,220,230,247,250,
              250,250,260,281,284.25,285,285,290,300,300,
              300,300,345,350,350,353,370,380,380,380,450,
              500,500,500,550,600,600,700,800,950,950,
              1200,1300,1500,1545.98,1600)

pagosAgua

# Despues de eso, ordemos los datos utilizando la funcion sort

pagosOrdenados = sort(pagosAgua)
length(pagosOrdenados)
pagosOrdenados

# Una vez ordenado, procedemos a extraer las frecuencias de los datos, con la funcion
# table, que nos devuelve la frecuencia de cada dato, y esa frecuencia los guardamos
# en una variable llamada frecuenciaPagos

frecuenciaPagos = table(pagosOrdenados)
frecuenciaPagos

# Una vez ordenado los datos, y obtenida su frecuencia, podemos empezar a sacar las
# medidas de tendencia central, y empezaremos primero por la moda la cual vamos 
# a utilizar un metodo llamado moddest el cual primero tenemos que exportar

# install.packages("modeest")

library(modeest)

modaPagos <- mlv(pagosOrdenados, method = "mfv")
modaPagos

# Una vez sacada la moda, continuamos con la media, que utilizaremos el metodo mean

mediaPagos <- mean(pagosOrdenados)
mediaPagos

# Ya la media obtenida continuamos por ultimo con la mediana, y para ello utilizamos
# la funcion median

medianaPagos <- median(pagosOrdenados)
medianaPagos

# Y con esto concluimos las medidas de tendencia central
# Y empezamos con la tabla de dispersion

# Y empezamos a restar cada dato que tenemos con la media

x_Media <- c(pagosOrdenados- mediaPagos)
x_Media

# Luego continuamos con la siguiente columna que seria elevar nuestro vector x_Media
# al cuadrado

x_MediaCuadrado <- c(x_Media*x_Media)
x_MediaCuadrado

# Para la tercer columna simplementes obtenemos la frecuencia de los datos
# pero como previamente ya los obtuvimos, los colocamos en la tabla

frecuenciaPagos

# Y continuamos la cuarta columna que seria en este caso la Varianza

varianzaPagos <- c(x_MediaCuadrado/(length(x_MediaCuadrado) - 1))
varianzaPagos

# Y luego sumamos las varianzas obtenidas

sumaVarianzaPagos <- sum(varianzaPagos)
sumaVarianzaPagos

# Y con eso tenemos la varianza, y para obtener la desviacion le sacamos la raiz a la 
# varianza

desviacionPagos <- sqrt(sumaVarianzaPagos)
desviacionPagos

# Y con esto terminamos la tabla de dispersion, y empezamos la tabla de frecuencias
# y para hacer mas resumido el proceso, vamos a empezar creando clases, para tener un
# rango de cada dato

# Y para obtener las clases, obtenemos la K

k <- 0
while (2^k < length(pagosOrdenados)) {
  k <- k + 1
}
k

# La k ya obtenida, obtenemos los intervalos

intervalo <- (pagosOrdenados[length(pagosOrdenados)] - pagosOrdenados[1]) / k
intervalo

# Ya obtenido el intervalo, comenzamos a obtener las clases

intervalos <- cut(pagosOrdenados, breaks = k)
intervalos

# 

tablaF <- as.data.frame(table(Clases = factor(cut(pagosOrdenados, breaks = k))))
tablaF

frecuenciaTabla <- transform(tablaF,
          Fac = cumsum(Freq),
          Rel = round(prop.table(Freq), 4),
          RelAc = round(cumsum(prop.table(Freq)), 4)
)
frecuenciaTabla

# Ya con las tablas obtenidas, podemos das pie a las graficas, que son
# el historgrama, poligono de frequencias y el diagrama pastel

FA = table(intervalos)
FA

barplot(FA, main = "Histograma")

# Una vez hecho el histograma, podemos hacer el poligono de frecuencias

mpagosOrdenados <- min(pagosOrdenados)
contador <- 0
clasesP <- 0
while (contador <= k + 1) {
  clasesP[contador] <- c(mpagosOrdenados + (intervalo * (contador - 1)))
  contador <- contador + 1
}
clasesP
length(clasesP)

contador <- 1
contador2 <- 1
puntoM <- 0
while (contador2 <= length(clasesP)) {
  if (contador2 == 7){
    break
  }
  puntoM[contador2] <- c((clasesP[contador2] + clasesP[contador2 + 1]) / 2)
  contador2 <- contador2 + 1
}
puntoM

minimoM <- ( (min(clasesP) - intervalo) + min(clasesP) ) / 2
minimoM

maximoM <- ( (max(clasesP) + intervalo) + max(clasesP) ) / 2
maximoM

puntoMM <- sort(c(puntoM, minimoM, maximoM))
puntoMM

FA <- c(0,FA,0)
FA

plot(x = puntoMM, y = FA, col = 2, type = "b", main = "Poligono de frecuencias")

# Ya con el poligono de frecuencias realizado, podemos hacer el diagrama pastel

FR <- table(intervalos) / length(pagosOrdenados)
FR <- round(FR, 4)
FR

# Lo siguiente a ver es el Diagrama pastel, el cual podemos sacar primero,
# convirtiendo la frecuencia relativa a porcentaje, como a continuacion se
# muestra

porcentaje <-FR * 100
porcentaje

# Luego para darle un formato correcto a nuesto porcentaje, utilizamos la
# funcion paste

etiqueta <- paste(porcentaje, "%", sep = " ")
etiqueta

# Despues de eso, creamos el vecto de colores, el cual, le ponemos la cantidad
# de colores que representan cada intervalo

colores <- c("Blue", "Green", "Red", "Purple","Orange","Yellow")
colores

# Una vez hecho todo esto, podemos dar pie a crear nuestro diagrama pastel,
# utilizando la funcion pie

pie(porcentaje,
    labels = etiqueta,
    clockwise = TRUE,
    col = colores,
    main = "Diagrama Pastel")

# Ya por ultimo y como dato extra, podemos agregar, un pequenio recuadro
# que represente a cada clase, eso lo podemos hacer con un vector,
# y asignandole colores a cada vector

legend("topright",
       c(" $57.00	$315.17 ",
         " $315.17	$572.33 ",
         " $572.33	$829.50 ",
         " $829.50	$1,086.67 ",
         " $1,086.67	$1,343.83 ",
         " $1,343.83	$1,601.00 "),
       cex = 0.5,
       fill = colores)

# Podemos concluir que 56.14% de la poblacion entrevistada,
# paga al rededor de $57.00 a 315.17$ pesos mexicanos por el recibo del agua

# ********************************* AQUI EMPIEZA FAMILIAS ***********************************************

# Fernando Dilland, Miguel del Castillo <<<<<<<<<<<<<<<<<<<<<<

# Ahora pasaremos con las familias

familiasP <- c(4, 4, 6, 4, 2,	3, 5,	6, 3,	3,
               5,	3, 4, 4, 4, 5, 7, 5, 4,	4,
               6, 4, 4, 6, 3, 5, 5, 4, 3, 7,
               4, 7, 4, 5, 3, 3, 4, 5, 6, 4,
               5, 5, 4, 8, 5, 5, 3, 2, 4, 4,
               6, 6, 4, 4, 5, 3, 10)
Ofamilias <- sort(familiasP)
Ofamilias

OFfamilias <- table(Ofamilias)
OFfamilias

# Medidas de tendencia central

OFMfamilias <- mean(Ofamilias)
OFMfamilias

OFMefamilias <- median(Ofamilias)
OFMefamilias

OFMofamilias <- mlv(Ofamilias, method = "mfv")
OFMofamilias

#Tabla de Dispersion

# Primera columna de la tabla x-media

print('X - MEDIA')
OFMXMfamilias <- c(Ofamilias- OFMfamilias)
OFMXMfamilias
class(OFMXMfamilias)

print('X - MEDIA^2')
OFMXM2familias <- c(OFMXMfamilias*OFMXMfamilias)
OFMXM2familias

print('FRECUENCIA')
OFMXM2Ffamilias <-table(Ofamilias)
OFMXM2Ffamilias

print('VARIANZA')
OFMXM2DNfamilias <- c(OFMXM2familias/(length(Ofamilias)-1))
OFMXM2DNfamilias

OSfamilias <- sum(OFMXM2DNfamilias)
print('Varianza: ')
print(OSfamilias)

print('DESVIACION')
OSDfamilias <- sqrt(OSfamilias)
print('Desviacion: ')
print(OSDfamilias)

# A continuacion la tabla de frequencias

# Y para obtener las clases, obtenemos la K

kF <- 0
while (2^kF < length(Ofamilias)) {
  kF <- kF + 1
}
kF

# La k ya obtenida, obtenemos los intervalos

OIfamilias <- ((Ofamilias[length(Ofamilias)] - Ofamilias[1]) / kF)
OIfamilias

# Ya obtenido el intervalo, comenzamos a obtener las clases

OISfamilias <- cut(Ofamilias , breaks = kF)
length(OISfamilias)
class(intervalos)

# Continuamos sacando la frecuencia

OISFAfamilias <- table(OISfamilias)
OISFAfamilias

# Continuamos sacando la frecuencia acumulada

OISFACfamilias = cumsum(OISFAfamilias)
OISFACfamilias

# Luego sacamos la frecuencia relativa

OFrfamilias <- c(OISFAfamilias/length(Ofamilias))
OFrfamilias

OFrpfamilias <- c(OFrfamilias*100)
OFrpfamilias <- round(OFrpfamilias, 2)
OFrpfamilias

OFrpefamilias <- paste(OFrpfamilias, "%", sep = " ")
OFrpefamilias

# Con la tabla hecha podemos hacer las graficas 
# Primero hacemos el histograma


barplot(OISFAfamilias, beside = TRUE)

# Luego hacemos el diagrama de frecuencias

OMenorfamilias <- min(Ofamilias)
contador <- 0
OClasefamilias <- 0
while (contador <= kF + 1) {
  if (contador == 1){
    OClasefamilias[contador] <- c(OMenorfamilias)
    contador <- contador + 1
  }
  else{
    OClasefamilias[contador] <- c(OClasefamilias[1] + 1 + (OIfamilias * (contador - 1)))
    contador <- contador + 1
  }
}
OClasefamilias
length(clasesP)

contador <- 1
contador2 <- 1
PuntoMfamilias <- 0
while (contador2 <= length(OClasefamilias)) {
  if (contador2 == 7){
    break
  }
  PuntoMfamilias[contador2] <- c((OClasefamilias[contador2] + OClasefamilias[contador2 + 1]) / 2)
  contador2 <- contador2 + 1
}
PuntoMfamilias

minimoMfamilias <- ( (min(OClasefamilias) - OIfamilias) + min(OClasefamilias) ) / 2
minimoMfamilias

maximoMfamilias <- ( (max(OClasefamilias) + OIfamilias) + max(OClasefamilias) ) / 2
maximoMfamilias

puntoMMfamilias <- sort(c(PuntoMfamilias, minimoMfamilias, maximoMfamilias))


OISFAfamilias <- c(0,OISFAfamilias,0)
OISFAfamilias


plot(x = puntoMMfamilias, y = OISFAfamilias, col = 2, type = "b", main = "Poligono de frecuencias")

# Como ultima grafica a obtener, concluiremos con el diagrama pastel

OFrpefamilias

coloresFamilia <- c("Blue", "Green", "Red", "Purple","Orange","Yellow","Pink","Black")
colores

# Una vez hecho todo esto, podemos dar pie a crear nuestro diagrama pastel,
# utilizando la funcion pie

pie(OFrpfamilias,
    labels = OFrpefamilias,
    clockwise = TRUE,
    col = coloresFamilia,
    main = "Diagrama Pastel Frecuencias Relativa")

# Podemos concluir que el 70.18% de 4 a 6 integrantes, de los cuales el 35.09% 
# pertenecen al rango de (3.33 a 4.67) y el otro 35.09% pertenecen al rango de (4.67,6)
# y que solo el 3.50% de las familias entrevistadas, tienen mas de 7 integrantes  

# ********************************* AQUI EMPIEZA MUNICIPIOS ***********************************************

# Kevin Caballero <<<<<<<<<<<<<<<<<<<<<<

# Y por ultimo los municipos donde viven las familias
municipioP <- c("Monterrey", "García",	"Escobedo",	"Escobedo",	'Apodaca',	'San Nicolás de los Garza',
                'Monterrey',	'Monterrey',	'San Nicolás de los Garza',	'Apodaca',	'Monterrey',
                'San Pedro Garza García',	'San Pedro Garza García',	'Santa Catarina',	'Monterrey',
                'Escobedo',	'Monterrey',	'Apodaca',	'Monterrey', 'Escobedo',	'Santiago',	'Monterrey',
                'Escobedo',	'Santa Catarina',	'Escobedo',	'Escobedo',	'Monterrey', 'Monterrey',	'Escobedo',
                'Monterrey',	'Monterrey',	'Monterrey',	'Monterrey',	'Monterrey', 'Monterrey',	'Escobedo',
                'San Nicolás de los Garza',	'Monterrey',	'Monterrey',	'Escobedo',	'Escobedo',	'Escobedo',
                'Escobedo',	'Monterrey',	'Escobedo',	'Escobedo',	'Monterrey', 'Santa Catarina',	'Monterrey',
                'Escobedo',	'San Nicolás de los Garza',	'Santiago',	'San Pedro Garza García',	'Apodaca',
                'Escobedo',	'Monterrey',	'Apodaca')
municipioP

#Una vez hecho el vector, lo ordenamos de A-Z

municipioP_O <- sort(municipioP)
municipioP_O

length(municipioP)

# Al ser datos que no son numericos, no podemos determinar una media de ellos
# Pero si podemos obtener la moda

modaMunicipio <- mlv(municipioP, method = "mfv")
modaMunicipio

# Al igual podemos obtener la mediana

median(municipioP_O)

# Al no tener el dato de la media no podemos obtener la tabla de dispersion
# Entonces pasamos directamente a la tabla de frecuencia

# donde empezamo a sacar la frecuencia de cada municipio

fMunicipio <- table(municipioP)
fMunicipio

# Continuamos sacando la frecuencia acumulada

fMunicipio[1]

contador <- 1
faMunicipio <- 0 

length(fMunicipio)

while (contador <= length(fMunicipio)) {
  if (contador == 1){
    faMunicipio[contador] <- fMunicipio[1]
    contador <- contador + 1
  }
  else{
    faMunicipio[contador] <- c(faMunicipio[contador - 1] + fMunicipio[contador])
    contador <- contador + 1
  }
  
}
faMunicipio
length(faMunicipio)

# Luego sacamos la frecuencia relativa

frMunicipio <- c(fMunicipio/length(municipioP))
frMunicipio

frpMunicipio <- c(frMunicipio*100)
frpMunicipio <- round(frpMunicipio, 2)
frpMunicipio

frpeMunicipio <- paste(frpMunicipio, "%", sep = " ")
frpeMunicipio

# Despues de obtener la frecuencia relativa, podemos obtener el diagrama pastel

frpecMunicipio <- c("Blue", "Green", "Red", "Purple","Orange","Yellow", "Pink","Black")
frpecMunicipio

# Una vez hecho todo esto, podemos dar pie a crear nuestro diagrama pastel,
# utilizando la funcion pie

pie(frpMunicipio,
    labels = frpeMunicipio,
    clockwise = TRUE,
    col = frpecMunicipio,
    main = "Diagrama Pastel de los Municipios")

legend("topleft",
       c("Apodaca",
         "Escobedo",
         "Garcia",
         "Monterrey",
         "San Nicolas de los Garza",
         "San Pedro Garza Garcia",
         "Santa Catarina",
         "Santiago"),
       cex=0.30,
       fill = frpecMunicipio
       )

# Y con esto podemos conlcuir que el 38.6% de los entrevistados, son de monterrey,
# Nuevo Leon predominando en la zona entrevistada



