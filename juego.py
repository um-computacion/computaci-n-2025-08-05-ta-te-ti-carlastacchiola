from tablero import Tablero 
from excepciones import PosicionOcupadaException, PosicionInvalidaException

class Juego:
    def __init__(self, jugador1, jugador2):
        self.tablero = Tablero()
        self.jugadores = [jugador1, jugador2]
        self.jugador_actual = jugador1

    def siguiente_turno(self):
        if self.jugador_actual == self.jugadores[0]:
            self.jugador_actual = self.jugadores[1]
        else:
            self.jugador_actual = self.jugadores[0]


    def hay_ganador(self):
        simbolo = self.jugador_actual.simbolo
        for fila in self.tablero.contenedor:
            if all(celda == simbolo for celda in fila): 
                return True #revisa filas
            
        for col in range(3):
            if all(self.tablero.contenedor[f][col] == simbolo for f in range(3)):
                return True #revisa columnas 
            
        if all(self.tablero.contenedor[i][i] == simbolo for i in range(3)):
            return True
        if all(self.tablero.contenedor[i][2 - i] == simbolo for i in range(3)):
            return True
        return False #revisa diagonales


    def iniciar(self):
        while True:
            self.tablero.mostrar()
            try:
                fila, columna = self.jugador_actual.jugar()
                self.tablero.poner_ficha(fila, columna, self.jugador_actual.simbolo)

            except PosicionOcupadaException as e:
                print(e)
                continue 
            except PosicionInvalidaException as e:
                print(e)
                continue

            if self.hay_ganador():
                self.tablero.mostrar()
                print (f"¡Tenemos un ganador! {self.jugador_actual.nombre} ganó!")
                break

            if self.tablero.lleno():
                self.tablero.mostrar()
                print("¡Empate!")
                break

            self.siguiente_turno()
