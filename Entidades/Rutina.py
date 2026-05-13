from Entidades.Habito import Habito
class Rutina:
    """Agrupa varios hábitos bajo un mismo nombre."""

    def __init__(self, nombre: str) -> None:
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre de la rutina no puede estar vacío")

        self._nombre : str = nombre
        self._habitos: list[Habito] = []

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def habitos(self) -> list[Habito]:
        return self._habitos

    def agregar_habito(self, habito: Habito) -> None:
        if habito in self._habitos:
            raise HabitoDuplicadoError(f"El hábito '{habito.nombre}' ya está en la rutina")
        self._habitos.append(habito)

    def resumen(self) -> None:
        if len(self._habitos) == 0:
            raise RutinaVaciaError("La rutina está vacía")

        print(f"Rutina: {self._nombre}")

        for habito in self._habitos:
            print(habito)


class HabitoDuplicadoError(Exception):
    pass

class RutinaVaciaError(Exception):
    pass
