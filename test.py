import unittest
from tablero import Tablero
from jugador import Jugador
from juego import Juego
from excepciones import PosicionInvalidaException, PosicionOcupadaException

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tablero = Tablero()

    def test_ficha_valida(self):
        self.tablero.poner_ficha(0, 0, "X")
        self.assertEqual(self.tablero.contenedor[0][0], "X")

    def test_ficha_posicion_invalida(self):
        with self.assertRaises(PosicionInvalidaException):
            self.tablero.poner_ficha(3, 0, "O")  # fuera de rango

    def test_ficha_posicion_ocupada(self):
        self.tablero.poner_ficha(1, 1, "X")
        with self.assertRaises(PosicionOcupadaException):
            self.tablero.poner_ficha(1, 1, "O")  # misma posición ocupada

    def test_lleno(self):
        # llenar todo el tablero
        for i in range(3):
            for j in range(3):
                self.tablero.contenedor[i][j] = "X"
        self.assertTrue(self.tablero.lleno())

class TestJugador(unittest.TestCase):
    def test_creacion(self):
        jugador = Jugador("Ana", "O")
        self.assertEqual(jugador.nombre, "Ana")
        self.assertEqual(jugador.simbolo, "O")

class TestJuego(unittest.TestCase):
    def setUp(self):
        self.jugador1 = Jugador("Ana", "X")
        self.jugador2 = Jugador("Luis", "O")
        self.juego = Juego(self.jugador1, self.jugador2)

    def test_alternar_turno(self):
        self.assertEqual(self.juego.jugador_actual, self.jugador1)
        self.juego.siguiente_turno()
        self.assertEqual(self.juego.jugador_actual, self.jugador2)
        self.juego.siguiente_turno()
        self.assertEqual(self.juego.jugador_actual, self.jugador1)

    def test_hay_ganador_filas(self):
        # Poner tres X en fila 0
        self.juego.tablero.contenedor[0] = ["X", "X", "X"]
        self.juego.jugador_actual = self.jugador1
        self.assertTrue(self.juego.hay_ganador())

    def test_hay_ganador_columnas(self):
        for i in range(3):
            self.juego.tablero.contenedor[i][1] = "O"
        self.juego.jugador_actual = self.jugador2
        self.assertTrue(self.juego.hay_ganador())

    def test_hay_ganador_diagonal(self):
        for i in range(3):
            self.juego.tablero.contenedor[i][i] = "X"
        self.juego.jugador_actual = self.jugador1
        self.assertTrue(self.juego.hay_ganador())

    def test_no_ganador(self):
        self.juego.tablero.contenedor = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", "O"],
        ]
        self.juego.jugador_actual = self.jugador1
        self.assertFalse(self.juego.hay_ganador())

if __name__ == "__main__":
    unittest.main()
