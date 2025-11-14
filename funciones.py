#######################################
#######################################
########### Funciones #################
#######################################
#######################################
import numpy as np
import clases as cl

def comprobar_victoria(id_jugador, tablero1, tablero2):

    if ( not np.any(tablero1 == 'O') ) or ( not np.any(tablero2 == 'O')):

        if ( not np.any(tablero1 == 'O') ):
            print(f"Lo siento {id_jugador} Game Over: Se han hundido todos tus barcos 💀💀💀💀")
        else:
            print(f"Enhorabuena {id_jugador} has ganado la partida 🏆 🎉🎉🎉🎉🎉")
            
        return True
    
    else:
        return False


