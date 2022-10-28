#Jonathan Eliud Fernández Zamora
#A01571108
#Este programa crea un juego de cruzar al otro lado y termina al llegar a la última columna

import random

#Crea el tablero en el que se va a jugar
def tablero():
    tab = []
    renglones = 6
    columnas = 6
    jugador = "G"
    obs = "#"
    i = 0

    for ren in range(renglones):
        mat = []
        for col in range(columnas):
            mat.append("_")
        tab.append(mat)

    while i < 6:        
        ran = random.randrange(0,6)
        ran2 = random.randrange(1,6)
        if tab[ran][ran2] == "#":
            ran = random.randrange(1,6)
            ran2 = random.randrange(1,6)
        tab[ran][ran2] = obs
        i = i+1
    tab[2][0] = jugador
    tab[3][0] = jugador
    return tab

#Hace avanzar a la persona, siempre avanza hacia adelante
def avanzar(ren,col,direccion,tab):
    if direccion == "e" and tab[ren-1][col+1] != "#":
        if ren-1 == -1:
            return tab
        tab[ren][col] = "_"
        tab[ren-1][col+1] = "G"
    elif direccion == "d" and tab[ren][col+1] != "#":
        tab[ren][col] = "_"
        tab[ren][col+1] = "G"
    elif ren+1 == 6:
            return tab
    elif direccion == "x" and tab[ren+1][col+1] != "#":
        tab[ren][col] = "_"
        tab[ren+1][col+1] = "G"
    else:
        return tab
    return tab

#La función principal que tiene todo el programa
def main():
    tab = tablero()
    print("    0    1    2    3    4    5")
    for ren in range(len(tab)):
        print(ren, end= " ")
        print(tab[ren])
    ren = int(input("En que renglon se encuentra? "))
    col = int(input("En que columna se encuentra? "))
    direccion = str(input("A donde se quiere mover? (arriba = e, derecha = d, abajo = x) "))
    jugar = avanzar(ren,col,direccion,tab)
    print("    0    1    2    3    4    5")
    for ren in range(len(tab)):
        print(ren, end= " ")
        print(jugar[ren])
    cont = str(input("Quiere seguir jugando? (Si - s, No - n) "))
    while True:
        if cont == "s":
            ren = int(input("En que renglon se encuentra? "))
            col = int(input("En que columna se encuentra? "))
            direccion = str(input("A donde se quiere mover? (arriba = e, derecha = d, abajo = x) "))
            jugar = avanzar(ren,col,direccion,tab)
            print("    0    1    2    3    4    5")
            for ren in range(len(tab)):
                print(ren, end= " ")
                print(jugar[ren])
            if col+1 == 5:
                print("¡Ganaste!")
                break
            else:
                cont = str(input("Quiere seguir jugando? (Si - s, No - n) "))
        elif cont == "n":
            print("Gracias por jugar")
            break
        else:
            cont = str(input("Quiere seguir jugando? (Si - s, No - n) "))
main()