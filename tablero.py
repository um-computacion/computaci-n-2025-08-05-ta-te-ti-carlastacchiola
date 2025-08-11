from excepciones import PosicionOcupadaException, PosicionInvalidaException

class Tablero: 
    def __init__(self): 
        self.contenedor = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

    def mostrar(self):
        for i, fila in enumerate(self.contenedor):
            print(" | ".join(fila))
        if i < len(self.contenedor) - 1:
            print("-" * len(" | ".join(fila)))


    def poner_ficha(self, fila, columna, simbolo):
        # Verificar que la posición esté dentro de 0-2
        if fila not in range(3) or columna not in range(3):
            raise PosicionInvalidaException(fila, columna)
        # Verificar que la celda esté libre
        if self.contenedor[fila][columna] != " ":
            raise PosicionOcupadaException(fila, columna)
        # Colocar ficha
        self.contenedor[fila][columna] = simbolo

    def lleno(self):
        return all(celda != " " for fila in self.contenedor for celda in fila)
