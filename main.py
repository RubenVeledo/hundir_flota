import funciones.py

#creamos el tablero
funciones.crear_tablero(tamaño)

#Ponemos las coordenas de los barcos en formato tupla y le asignamos el valor de "O"
funciones.colocar_barco(barco, tablero)

#Realizamos la función para crear barcos
funciones.crear_barco(eslora)

#Ahora hacemos una función para colocar varios barcos del jugador

funciones.colocacion_barco(tablero)

#Ahora deberíamos mostrar el tablero con todos los barcos colocados

#replicamos la colocación de los barcos pero esta vez para los elegidos por la maquina
funciones.colocacion_barco_maquina(tablero)

#Ahora vamos al paso de disparar. En primer lugar una función para el turno del jugador
funciones.disparar_usuario(casilla, tablero)

#Para que la maquina también dispare en su turno
funciones.disparar_maquina(tablero)