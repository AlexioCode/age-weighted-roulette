import random
import datetime as dt

oneYearAddsXProbability = 20
ageMultiplier = oneYearAddsXProbability / 365

class Element:
    def __init__(self, nombre, fecha, prob = 0.0):
        self.nombre = nombre
        self.fecha = fecha
        self.prob = prob

# Asignar probabilidades a los juegos
def asignarProbabilidadesAJuegos(listaJuegos: list):
    indiceJuego = 0
    probMax = 0
    for juego in listaJuegos:
        juego.prob = random.randint(0, 100)
        antiguedad = dt.datetime.now() - juego.fecha
        juego.prob = juego.prob + antiguedad.days * ageMultiplier # antiguedad.days is int
        if (juego.prob > probMax):
            probMax = juego.prob
            indiceJuego = listaJuegos.index(juego)
    return indiceJuego


if __name__ == '__main__':

    cadJuego = ""
    listaJuegos = []

    # Introducir juegos ($ para terminar)
    while (cadJuego != "$"):
        cadJuego = input("Introduce juego y fecha en la que lo apuntaste en la lista (e.g. Stendhal, 29/02/2023) (no es obligatorio introducir fecha) [$ para terminar]: \n")
        if (cadJuego != "$"): # Si no se ha introducido '$'
            if(cadJuego[0] == "-"): # Eliminar guión del principio
                cadJuego = cadJuego[1:]
            if(cadJuego[0] == " "): # Eliminar espacio del principio
                cadJuego = cadJuego[1:]
            if(cadJuego[0].islower()): # Si la primera letra es minúscula, poner en mayúscula
                cadJuego = cadJuego[0].upper() + cadJuego[1:]
            
            nombreJuego = cadJuego.split(",")[0]
            if (len(cadJuego.split(",")) > 1): # Si fecha está especificada
                cadFecha = cadJuego.split(",")[1]
                if(cadFecha[0] == " "): # Eliminar espacio después de la coma
                    cadFecha = cadFecha[1:]
            else: # Si no indicamos fecha, se le asigna la actual
                cadFecha = dt.datetime.now().strftime("%d/%m/%Y")
                
            # Construir el juego y añadirlo a la lista
            listaJuegos.append(Element(nombreJuego, dt.datetime.strptime(cadFecha, "%d/%m/%Y")))

    print("\n\nTienes " + str(len(listaJuegos)) + " juegos pendientes.")
    print("Lista de juegos pendientes:")
    for juego in listaJuegos:
        print(juego.nombre)

    repetir = 's'
    while repetir == 's' and listaJuegos: # mientras selecciones que sí y haya elementos en la lista
        print("\nTirando de la ruleta...")
        indiceJuego = asignarProbabilidadesAJuegos(listaJuegos)
        print("\n\nTE HA TOCADO JUGAR: " + listaJuegos[indiceJuego].nombre + "\ncon una probabilidad de " + str(listaJuegos[indiceJuego].prob))
        listaJuegos.pop(indiceJuego)
        if listaJuegos:
            repetir = input("¿Quieres volver a tirar de la ruleta? (s/n): ")