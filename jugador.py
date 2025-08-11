class Jugador:
    def __init__(self, nombre, simbolo):
        self.nombre = nombre
        self.simbolo = simbolo # "X o O"


    def jugar(self): 
        fila = int(input(f"{self.nombre}, ingresar fila(0-2): "))
        columna = int(input(f"{self.nombre}, ingresar columna (0-2):  "))
        return fila, columna

    def __str__(self):
        return f"{self.nombre} juega con {self.simbolo}"