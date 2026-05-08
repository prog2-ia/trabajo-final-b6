from Entidades.Habito import Habito
class Rutina:
    """Agrupa varios hábitos bajo un mismo nombre."""

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def habitos(self) -> list[Habito]:
        return self._habitos

    def __init__(self, nombre: str) -> None:
        self._nombre : str = nombre
        self._habitos: list[Habito] = []

    def agregar_habito(self, habito: Habito) -> None:
        self._habitos.append(habito)

    def resumen(self) -> None:
        print(f"\nRutina: {self._nombre}")
        for h in self._habitos:
            print(f"  {h}")
