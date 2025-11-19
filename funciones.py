#######################################
#######################################
########### Funciones #################
#######################################
#######################################
import numpy as np
import clases as cls

def comprobar_victoria(id_jugador, tablero1, tablero2):

    if ( not np.any(tablero1 == 'O') ) or ( not np.any(tablero2 == 'O')):

        if ( not np.any(tablero1 == 'O') ):
            print(f"Lo siento {id_jugador} Game Over: Se han hundido todos tus barcos 💀💀💀💀")
        else:
            print(f"Enhorabuena {id_jugador} has ganado la partida 🏆 🎉🎉🎉🎉🎉")
            
        return True
    
    else:
        return False


def acciones_del_tablero(coordenada, tbl_jugador1, tbl_jugador2):

            cls.Tablero.recibir_disparo(tbl_jugador2.tablero_barcos, coordenada, tbl_jugador1.id_jugador)

            tbl_jugador1.tablero_disparos[coordenada] = tbl_jugador2.tablero_barcos[coordenada]

            cls.Tablero.mostrar_tablero(tbl_jugador1.tablero_disparos, tbl_jugador1.id_jugador)
            
