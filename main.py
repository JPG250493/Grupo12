
import variables as var
import clases as cls
import funciones as funcion
import numpy as np


def main():
    
    print("\nBienvendido al juego de Hundir la Flota. ¿Estás listo? 🕹️\n")
    print("El objetivo 🎯 del juego es hundir todos los barcos del oponente.\n\n")
    
    id_jugador = input("Indica tu nombre de usuario: ")

    print(f"Encantado {id_jugador} ¡Comencemos! ¡Que la fuerza te acompañe! 💪\n")

    tbl_jugador1 = cls.Tablero(id_jugador=id_jugador)
    tbl_jugador2 = cls.Tablero(id_jugador="CPU")

    #cls.Tablero.mostrar_tablero(tbl_jugador1.tablero_barcos)

    print(f"Colocando barcos de los jugadores {id_jugador} y CPU 🤖\n")
    for nombre_barco, eslora in var.dicc_barco.items():

        nveces = 4 - eslora + 1
        for i in range(nveces):
            tbl_jugador1.tablero_barcos = cls.Tablero.crea_barco_aleatorio(tbl_jugador1.tablero_barcos, eslora, 100)
            tbl_jugador2.tablero_barcos = cls.Tablero.crea_barco_aleatorio(tbl_jugador2.tablero_barcos, eslora, 100)           
        # break #Para que se coloque únicamente un barco de tamaño 4
    cls.Tablero.mostrar_tablero(tbl_jugador1.tablero_barcos, tbl_jugador1.id_jugador)

    # Al terminar asteriscar esta línea para no ver el tablero de la CPU
    # cls.Tablero.mostrar_tablero(tbl_jugador2.tablero_barcos, tbl_jugador2.id_jugador)

    while True:
                                            
        # Turno humano                        
        while True:
            print(f"\n¡¡Es tu turno {tbl_jugador1.id_jugador}!!\n")
            fila = int(input("Indica la primera coordenada del disparo (entre 0,9): "))

            while fila < 0 or fila > (var.filas - 1) or not isinstance(fila, int):
                fila = int(input("Indica una coordenada correcta (entre 0,9): "))    
            
            columna = int(input("Indica la segunda coordenada del disparo (entre 0,9): "))

            while columna < 0 or columna > (var.columnas - 1) or not isinstance(columna, int):
                columna = int(input("Indica una coordenada correcta (entre 0,9): "))    

            coordenada = (fila,columna)

            funcion.acciones_del_tablero(coordenada, tbl_jugador1, tbl_jugador2)
            
            if not tbl_jugador2.tablero_barcos[coordenada] == 'X':
                break
            elif funcion.comprobar_victoria(tbl_jugador1.id_jugador,tbl_jugador1.tablero_barcos, tbl_jugador2.tablero_barcos):
                return

        # Turno máquina
        while True:

            fila = np.random.randint(0,var.filas)
            columna = np.random.randint(0,var.columnas)

            coordenada = (fila, columna)

            funcion.acciones_del_tablero(coordenada, tbl_jugador2, tbl_jugador1)
            
            if ( not tbl_jugador1.tablero_barcos[coordenada] == 'X' ):
                break
            elif funcion.comprobar_victoria(tbl_jugador1.id_jugador,tbl_jugador1.tablero_barcos, tbl_jugador2.tablero_barcos):
                return
        

main()