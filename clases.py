#############################################
#############################################
############      Clases     ################
#############################################
#############################################
#############################################
import variables as var
import numpy as np
import random

class Tablero:
    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
        self.filas = var.filas
        self.columnas = var.columnas
        self.dicc_barco = var.dicc_barco
        self.tablero_barcos = np.full((self.filas, self.columnas), " ")
        self.tablero_disparos = np.full((self.filas, self.columnas), " ")
    
    def colocar_barco_plus(tablero, barco):
        tablero_temp = tablero.copy()
        num_max_filas = tablero.shape[0]
        num_max_columnas = tablero.shape[1]
        for pieza in barco:
            fila = pieza[0]
            columna = pieza[1]
            if fila < 0 or fila >= num_max_filas:
                print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
                return False
            if columna < 0 or columna >= num_max_columnas:
                print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
                return False
            if tablero[pieza] == "O" or tablero[pieza] == "X":
                print(f"No puedo poner la pieza {pieza} porque hay otro barco")
                return False
            tablero_temp[pieza] = "O"
        return tablero_temp
    
    def crea_barco_aleatorio(tablero, eslora = 4, num_intentos = 100):
        num_max_filas = tablero.shape[0]
        num_max_columnas = tablero.shape[1]
        contador = 0

        while contador <= num_intentos:
            barco = []

            pieza_inicio = (random.randint(0, num_max_filas - 1), random.randint(0, num_max_columnas - 1))
            #print("Pieza original:", pieza_inicio)
            barco.append(pieza_inicio)

            orientacion = random.choice(["N", "S", "E", "O"])
            #print("Orientacion:", orientacion)
            
            fila = pieza_inicio[0]
            columna = pieza_inicio[1]

            for i in range(1, eslora -1):
                if orientacion == "N":
                    fila -= 1
                elif orientacion == "S":
                    fila += 1
                elif orientacion == "E":
                    columna += 1
                elif orientacion == "O":
                    columna -= 1
                
                pieza = (fila, columna)
                barco.append(pieza)

            tablero_temp = Tablero.colocar_barco_plus(tablero, barco)
        
            if type(tablero_temp) == np.ndarray:
                return tablero_temp
            
            print("Intentar colocar otro barco, intento numero:", contador)

    def recibir_disparo(tablero, coordenada):
        if tablero[coordenada] == "O":
            tablero[coordenada] = "X"
            print("Tocado")
        elif tablero[coordenada] == " ":
            tablero[coordenada] = "-"
            print("Agua")
        else:
            print("Ya ha disparado aquí")

    def mostrar_tablero(tablero):
        num_filas = tablero.shape[0]
        num_columnas = tablero.shape[1]

        encabezado = "   " + " ".join([str(i) for i in range(num_columnas)])
        print(encabezado)

        for fila in range(num_filas):
            fila_str = f"{fila} |" + "|".join(tablero[fila, :]) + "|"
            print(fila_str)


