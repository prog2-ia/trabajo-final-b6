from Entidades.Habito import Habito
from Entidades.Notificable import Notificable

""" Esta clase representa un hábito de tipo check"""

class HabitoCheck(Habito, Notificable):

    def __init__(self,identificador: int,nombre: str,frecuencia: str,importancia: int) -> None:
        super().__init__(identificador, nombre, frecuencia, importancia)
        self._completado : bool= False

    @property
    def completado(self) -> bool:
        return self._completado

    def marcar_completado(self) -> None:
        self._completado = True

    def reiniciar(self) -> None:
        self._completado = False

    # Implementación del método abstracto de Habito
    def cumplido(self) -> bool:
        return self._completado

    def notificar(self) -> None:
        if not self._completado:
            print(f" [{self._nombre}] {self.mensaje_alerta()}")
        else:
            print(f" [{self._nombre}] ¡Ya completado!")

    def __str__(self) -> str:
        if self._completado:
            estado=" Hecho"
        else:
            estado=" Pendiente"

        return f"[CHECK] {self._nombre} ({self._frecuencia}) - {estado}"