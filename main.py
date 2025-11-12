
import variables as var
import clases as cls
import funciones as funcion
import numpy as np


def main():
    
    print("Bienvendido al juego de Hundir la Flota. ¿Estás listo?\n El objetivo del juego es hundir todos los barcos del oponente.\n")
    
    id_jugador = input("Indica tu nombre de usuario: ")

    tablero_jugador1 = cls.Tablero(id_jugador=id_jugador)
    tablero_jugador2 = cls.Tablero(id_jugador="CPU")

    cls.Tablero.mostrar_tablero(tablero_jugador1.tablero_barcos)

    print("Colocando barcos del jugador 1...")
    for nombre_barco, eslora in var.dicc_barco.items():
         #print(f"Colocando {nombre_barco} de eslora {eslora}")

        nveces = 4 - eslora + 1
        for i in range(nveces):
            tablero_jugador1.tablero_barcos = cls.Tablero.crea_barco_aleatorio(tablero_jugador1.tablero_barcos, eslora, 100)
            tablero_jugador2.tablero_barcos = cls.Tablero.crea_barco_aleatorio(tablero_jugador2.tablero_barcos, eslora, 100)
    

    cls.Tablero.mostrar_tablero(tablero_jugador1.tablero_barcos)
    cls.Tablero.mostrar_tablero(tablero_jugador2.tablero_barcos)

    while True:

        # Turno humano                        
        while True:

            fila = int(input("Indica la primera coordenada del disparo (entre 0,9)"))

            while fila < 0 or fila > (var.filas - 1) or not isinstance(fila, int):
                fila = int(input("Indica una coordenada correcta (entre 0,9)"))    
            
            columna = int(input("Indica la segunda coordenada del disparo (entre 0,9)"))

            while columna < 0 or columna > (var.columnas - 1) or not isinstance(columna, int):
                columna = int(input("Indica una coordenada correcta (entre 0,9)"))    

            # Pasar coordenada a tupla!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            coordenada = []
            coordenada.append(fila)
            coordenada.append(columna)

            cls.Tablero.recibir_disparo(tablero_jugador2.tablero_barcos, coordenada)

            tablero_jugador1.tablero_disparos[coordenada] = tablero_jugador2.tablero_barcos[coordenada]

            cls.Tablero.mostrar_tablero(tablero_jugador1.tablero_disparos)
            
            if not tablero_jugador2.tablero_barcos[coordenada] == 'X':
                break

        if not funcion.comprobar_victoria(tablero_jugador1.tablero_barcos, tablero_jugador2.tablero_barcos):
            break

        # Turno máquina
        while True:

            fila = np.random.randint(0,var.filas)
            columna = np.random.randint(0,var.columnas)

            coordenada = []
            coordenada.append(fila)
            coordenada.append(columna)

            cls.Tablero.recibir_disparo(tablero_jugador1.tablero_barcos, coordenada)

            tablero_jugador2.tablero_disparos[coordenada] = tablero_jugador1.tablero_barcos[coordenada]

            cls.Tablero.mostrar_tablero(tablero_jugador2.tablero_disparos)
            
            if not tablero_jugador1.tablero_barcos[coordenada] == 'X':
                break

        if not funcion.comprobar_victoria(tablero_jugador1.tablero_barcos, tablero_jugador2.tablero_barcos):
            break
        

main()