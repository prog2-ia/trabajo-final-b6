class Review:
    """Permite valorar un hábito"""
    def __init__(self, fecha, nota, comentario, habito):
        self._fecha = fecha
        self.nota= nota
        self.__comentario= comentario #Garantiza privacidad del usuario
        self._habito = habito

    @property
    def comentario(self):
        return self.__comentario

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota (self, value):
        if 0 <= value <= 10:
            self._nota = int(value)

    @property
    def fecha(self):
        return self._fecha

    @property
    def habito(self):
        return self._habito

    def __str__(self):
        return f"Se ha añadido la siguiente review al hábito con id {self._habito.identificador}:  fecha: {self._fecha}, nota: {self.nota}/10"

