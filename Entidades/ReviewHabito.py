class Review:
    def __init__(self, fecha, nota, comentario):
        self._fecha = fecha
        self._nota= nota
        self.__comentario= comentario

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota (self, value):
        if value<0 or value>10:
            print(f"El valor de la nota debe estar comprendido entre 0 y 10")

        else:
            self._nota = float(value)

    @property
    def fecha(self):
        return self._fecha

    def __str__(self):
        return f"Se ha añadido una review con fecha: {self._fecha} y nota: {self._nota}/10"

