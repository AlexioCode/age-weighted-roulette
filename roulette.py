import random
import datetime as dt

oneYearAddsXProbability = 20
ageMultiplier = oneYearAddsXProbability / 365

class Element:
    def __init__(self, name, date, prob = 0.0):
        self.name = name
        self.date = date
        self.prob = prob

# Asignar probabilidades a los juegos y devuelve el índice del juego que más probabilidad tiene
def assignProbabilitesToElements(elementsList: list):
    elementIndex = 0
    probMax = 0
    for element in elementsList:
        element.prob = random.randint(0, 100)
        antiguedad = dt.datetime.now() - element.date
        element.prob = element.prob + antiguedad.days * ageMultiplier # antiguedad.days is int
        if (element.prob > probMax):
            probMax = element.prob
            elementIndex = elementsList.index(element)
    return elementIndex


if __name__ == '__main__':

    elementStr = ""
    elementsList = []

    # Introducir juegos ($ para terminar)
    while (elementStr != "$"):
        elementStr = input("Introduce juego y fecha en la que lo apuntaste en la lista (e.g. Stendhal, 29/02/2023) (no es obligatorio introducir fecha) [$ para terminar]: \n")
        
        if elementStr != "": # Si no se introduce nada, vuelve a pedir que se introduzca
            if (elementStr != "$"): # Si no se ha introducido '$'
                if(elementStr[0] == "-"): # Eliminar guión del principio
                    elementStr = elementStr[1:]
                if(elementStr[0] == " "): # Eliminar espacio del principio
                    elementStr = elementStr[1:]
                if(elementStr[0].islower()): # Si la primera letra es minúscula, poner en mayúscula
                    elementStr = elementStr[0].upper() + elementStr[1:]
                elementName = elementStr.split(",")[0]

                if (len(elementStr.split(",")) > 1): # Si fecha está especificada
                    dateStr = elementStr.split(",")[1]
                    if(dateStr[0] == " "): # Eliminar espacio después de la coma
                        dateStr = dateStr[1:]
                else: # Si no indicamos fecha, se le asigna la actual
                    dateStr = dt.datetime.now().strftime("%d/%m/%Y")
                    
                # Construir el juego y añadirlo a la lista
                elementsList.append(Element(elementName, dt.datetime.strptime(dateStr, "%d/%m/%Y")))

    print("\n\nTienes " + str(len(elementsList)) + " juegos pendientes.")
    print("Lista de juegos pendientes:")
    for element in elementsList:
        print(element.name)

    repeat = 's'
    while repeat == 's' and elementsList: # mientras selecciones que sí y haya elementos en la lista
        print("\nTirando de la ruleta...")
        elementIndex = assignProbabilitesToElements(elementsList)
        print("\n\nTE HA TOCADO JUGAR: " + elementsList[elementIndex].name + "\ncon una probabilidad de " + str(elementsList[elementIndex].prob))
        elementsList.pop(elementIndex)
        if elementsList:
            repeat = input("¿Quieres volver a tirar de la ruleta? (s/n): ")