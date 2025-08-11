class PosicionOcupadaException(Exception):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.mensaje =f"La posición ({fila}, {columna}) ya está ocupada"
        super().__init__(self.mensaje)

        def __str__(self):
            return self.mensaje 
        

class PosicionInvalidaException(Exception):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.mensaje =f"La posición ({fila}, {columna}) no es válida"
        super().__init__(self.mensaje)

    def __str__(self):
        return self.mensaje 