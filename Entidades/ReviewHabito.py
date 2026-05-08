from Entidades.Habito import Habito
class Review:
    """Permite valorar un hábito"""
    def __init__(self, fecha : str, nota : int, comentario: str, habito: Habito) -> None:
        self._fecha : str = fecha
        self.nota : int= nota
        self.__comentario : str= comentario #Garantiza privacidad del usuario
        self._habito : Habito= habito

    @property
    def comentario(self) -> str:
        return self.__comentario

    @property
    def nota(self) -> int:
        return self._nota

    @nota.setter
    def nota(self, value: int) -> None:
        if 0 <= value <= 10:
            self._nota = int(value)

    @property
    def fecha(self) -> str:
        return self._fecha

    @property
    def habito(self) -> Habito:
        return self._habito

    def __str__(self)-> str:
        return f"Se ha añadido la siguiente review al hábito con id {self._habito.identificador}:  fecha: {self._fecha}, nota: {self.nota}/10"

