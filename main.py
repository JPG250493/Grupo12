
import variables as var
import clases as cls


def main():
    
    print("Bienvendido al juego de Hundir la Flota. ¿Estás listo?\n El objetivo del juego es hundir todos los barcos del oponente.\n")

    tablero_jugador1 = cls.Tablero(id_jugador="Humano")
    tablero_jugador2 = cls.Tablero(id_jugador="CPU")

    cls.Tablero.mostrar_tablero(tablero_jugador1.tablero_barcos)

    print("Colocando barcos del jugador 1...")
    for nombre_barco, eslora in var.dicc_barco.items():
        #print(f"Colocando {nombre_barco} de eslora {eslora}")

        nveces = 4 - eslora + 1
        for i in range(nveces):
            tablero_jugador1.tablero_barcos = cls.Tablero.crea_barco_aleatorio(tablero_jugador1.tablero_barcos, eslora, 100)
    
    cls.Tablero.mostrar_tablero(tablero_jugador1.tablero_barcos)

main()