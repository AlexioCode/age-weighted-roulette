import random
import datetime as dt

ONE_YEAR_ADDS_X_PROBABILITY = 20
AGE_MULTIPLIER = ONE_YEAR_ADDS_X_PROBABILITY / 365

class Element:
    def __init__(self, name, date, prob = 0.0):
        self.name = name
        self.date = date
        self.prob = prob

# Asignar probabilidades a los elementos y devuelve el índice del elemento que más probabilidad tiene
def assignProbabilitesToElements(elementsList: list):
    elementIndex = 0
    probMax = 0
    for element in elementsList:
        element.prob = random.randint(0, 100)
        antiguedad = dt.datetime.now() - element.date
        element.prob = element.prob + antiguedad.days * AGE_MULTIPLIER # antiguedad.days es int
        if (element.prob > probMax):
            probMax = element.prob
            elementIndex = elementsList.index(element)
    return elementIndex


if __name__ == '__main__':

    elementTypeSingular = input("What type of element are we talking about (singular): ")
    elementTypePlural = input("What type of element are we talking about (plural): ")
    if not elementTypeSingular or not elementTypePlural:
        elementTypeSingular = "element"
        elementTypePlural = "elements"

    elementStr = ""
    elementsList = []

    # Introducir elementos ($ para terminar)
    while (elementStr != "$"):
        elementStr = input(f"Introduce a {elementTypeSingular} and the date when you added it to the list (e.g., Stendhal, 29/02/2023) (it is not required to introduce the date) [$ to finish]: \n")
        
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
                    
                # Construir el Elemento y añadirlo a la lista
                elementsList.append(Element(elementName, dt.datetime.strptime(dateStr, "%d/%m/%Y")))

    print("\n\nThere's " + str(len(elementsList)) + f" {elementTypePlural} remaining.")
    print(f"List of remaining {elementTypePlural}:")
    for element in elementsList:
        print(element.name)

    repeat = 'y'
    while repeat == 'y' and elementsList: # mientras selecciones que sí y haya elementos en la lista
        print("\n\nGACHAPÓÓÓÓN WEEEY!!! (Spinning the wheel...)")
        elementIndex = assignProbabilitesToElements(elementsList)
        print("\nWINNING" + f" {elementTypeSingular}".upper() + ": " + elementsList[elementIndex].name + "\nwith a probability of: " + str(elementsList[elementIndex].prob))
        elementsList.pop(elementIndex)
        if elementsList:
            repeat = input("Do you want to spin the wheel again? (y (yes) / any (no)): ")