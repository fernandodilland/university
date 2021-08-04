# Codificar un script que cante las cartas de la lotería
# Deben presentarse en orden aleatorio
# Preguntando en cada iteración si ya hubo "buena"; en caso de ser así detenerse
# Si se agotan las cartas y nadie ha ganado, entonces anunciar el fin del juego

import random

print("Bienvenido(a)")
listaDeCartasDisponibles = ["El gallo", "El diablito", "La dama", "l catrín", "El paraguas", "La sirena", "La escalera", "La botella", "El barril",
                            "El árbol", "El melón ", "El valiente", "El gorrito", "La muerte", "La pera", "La bandera", "El bandolón",
                            "El violoncello", "La garza", "El pájaro", "La mano", "La bota",
                            "La luna", "El cotorro", "El borracho", "El negrito", "El corazón", "La sandía", "El tambor", "El camarón",
                            "Las jaras", "El músico", "La araña", "El soldado", "La estrella", "El cazo", "El mundo", "El apache", "El nopal",
                            "El alacrán", "La rosa", "La calavera", "La campana", "El cantarito", "El venado", "El sol", "La corona", "La chalupa",
                            "El pino", "El pescado", "La palma", "La maceta", "El arpa", "La rana"]
print("Lista de cartas:", listaDeCartasDisponibles)
print("------------------------------------")
random.shuffle(listaDeCartasDisponibles) # Barajar las cartas

contador = 0
cantidadTotalCartas = 53

while cantidadTotalCartas > contador:
    contador = contador + 1
    print("Viene y se va corriendo con:", listaDeCartasDisponibles[contador])
    huboBuena = input("¿Hubo buena? (Si/No): ")
    agotaCartas = 1
    if huboBuena=="Si":
        agotaCartas = 0
        break;

if agotaCartas==1:
    print("> Se agotaron las cartas")

print("Gracias por jugar")

