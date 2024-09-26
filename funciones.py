import numpy as np
import random

#Creamos el tablero
def crear_tablero(tamaño):
    tablero = np.full((tamaño,tamaño), "_")
    return tablero

#Ponemos las coordenas de los barcos en formato tupla y le asignamos el valor de "O"
def colocar_barco(barco, tablero):
    for casilla in barco:
        fila, columna = casilla  #Extraemos fila y columna de cada tupla
        tablero[fila, columna] = "O"  #Colocamos "O" en las coordenadas especificadas
    return tablero


#Realizamos la función para crear barcos

def crear_barco(eslora):
    casilla_0 = (random.randint(0,9), random.randint(0,9))
    orientacion = random.choice(["Vertical", "Horizontal"])

    barco = [casilla_0]
    casilla = casilla_0
    while len(barco) < eslora:
        if orientacion == "Vertical":
            casilla = (casilla[0]+1, casilla[1])
            barco.append(casilla) # Vertical
        else:
            casilla = (casilla[0], casilla[1]+1)
            barco.append(casilla) # Horizontal

    return barco


#Ahora hacemos una función para colocar varios barcos del jugador

def colocacion_barco(tablero):
    lista_barcos = [crear_barco(2),crear_barco(2),crear_barco(2),crear_barco(3),crear_barco(3),crear_barco(4)]
    print(lista_barcos)

    for barco in lista_barcos:
        print("barco :",barco)
        for fila, columna in barco:
            #print(fila)
            #print(columna)

            if fila < 0 or fila >= len(tablero): 
                print("Coordenadas incorrectas para la fila")
                colocacion_barco(tablero)
            if columna < 0 or columna >= len(tablero):
                print("Coordenadas incorrectas para la columna")
                colocacion_barco(tablero)
            if tablero[fila][columna] != "_":
                print("celda ocupada")
                colocacion_barco(tablero)
        
    return lista_barcos

#guardamos los barcos creados por el usuario en una lista
lista_final_usuario = colocacion_barco(tablero)

#Ahora deberíamos mostrar el tablero con todos los barcos colocados


#replicamos la colocación de los barcos pero esta vez para los elegidos por la maquina

def colocacion_barco_maquina(tablero):
    lista_barcos_maquina = [crear_barco(2),crear_barco(2),crear_barco(2),crear_barco(3),crear_barco(3),crear_barco(4)]
    print(lista_barcos_maquina)

    for barco in lista_barcos_maquina:
        print("barco :",barco)
        for fila, columna in barco:
            print(fila)
            print(columna)

            if fila < 0 or fila >= len(tablero): 
                print("Coordenadas incorrectas para la fila")
                colocacion_barco_maquina(tablero)
            if columna < 0 or columna >= len(tablero):
                print("Coordenadas incorrectas para la columna")
                colocacion_barco_maquina(tablero)
            print(tablero[fila][columna])
            if tablero[fila][columna] != "_":
                print("celda ocupada")
                colocacion_barco_maquina(tablero)
        
    return lista_barcos_maquina


#guardamos los barcos creados por la maquina en una lista
lista_final_maquina = colocacion_barco_maquina(tablero)

#Ahora deberíamos mostrar el tablero con todos los barcos colocados


#Ahora vamos al paso de disparar. En primer lugar una función para el turno del jugador

def disparar_usuario(casilla, tablero):
    fila, columna = casilla

    if fila < 0 or fila >= len(tablero) or columna < 0 or columna >= len(tablero):
        print("Coordenadas fuera del tablero")
        return tablero
    
    if tablero[fila][columna] == "O":
        print("Tocado")
        tablero[fila][columna] = "X"  
    elif tablero[fila][columna] == "_":
        print("Agua")
        tablero[fila][columna] = "A" 
    else:
        print("Ya disparaste a esta casilla") 

    return tablero


#mostramos el tablero después del disparo

tablero = disparar_usuario(disparo, tablero)




#Ahora vamos al paso de disparar. Después la función para que dispare la maquina

def disparar_maquina(tablero):
    fila = random.randint(0, len(tablero) - 1)
    columna = random.randint(0, len(tablero) - 1)
    
    print("La máquina dispara a:" + fila + columna)
    
    if tablero[fila][columna] == "O":
        print("Tocado")
        tablero[fila][columna] = "X"  
    elif tablero[fila][columna] == "_":
        print("Agua")
        tablero[fila][columna] = "A" 
    else:
        print("La máquina ya disparó a esta casilla")


    return tablero