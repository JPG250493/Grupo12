#######################################
#######################################
########### Funciones #################
#######################################
#######################################
import numpy as np

def comprobar_victoria(tablero1, tablero2):

    if ( not np.any(tablero1.tablero_barcos == 'O') ) or ( not np.any(tablero2.tablero_barcos == 'O')):

        if ( not np.any(tablero1.tablero_barcos == 'O') ):
            print(f"Game Over: Se han hundido todos tus barcos")
        else:
            print(f"Enhorabuena has ganado la partida")
            
        return True
    
    else:
        return False


