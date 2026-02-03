from jugador import Jugador
from juego import Juego

if __name__ == "__main__":
    print("=== TA-TE-TI ===")
    nombre1 = input("Nombre del jugador 1 (X): ")
    nombre2 = input("Nombre del jugador 2 (O): ")

    jugador1 = Jugador(nombre1, "X")
    jugador2 = Jugador(nombre2, "O")

    juego = Juego(jugador1, jugador2)
    juego.iniciar()
