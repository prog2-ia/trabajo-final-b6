from Entidades.Habito import Habito
class Review:
    """Permite valorar un hábito"""
    def __init__(self, fecha : str, nota : int, comentario: str, habito: Habito) -> None:

        # Validación de comentario vacío
        if not comentario or comentario.strip() == "":
            raise ComentarioVacioError("El comentario no puede estar vacío")

        # Validación de nota inválida
        if not 0 <= nota <= 10:
            raise NotaInvalidaError("La nota debe estar entre 0 y 10")

        # Validación de fecha vacía
        if not fecha or fecha.strip() == "":
            raise FechaReviewInvalidaError("La fecha no puede estar vacía")

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
        else:
            raise NotaInvalidaError('La nota debe de estar entre 0 y 10')

    @property
    def fecha(self) -> str:
        return self._fecha

    @property
    def habito(self) -> Habito:
        return self._habito

    def __str__(self)-> str:
        return f"Se ha añadido la siguiente review al hábito con id {self._habito.identificador}:  fecha: {self._fecha}, nota: {self.nota}/10"


class NotaInvalidaError(Exception):
    pass

class ComentarioVacioError(Exception):
    pass

class FechaReviewInvalidaError(Exception):
    pass

