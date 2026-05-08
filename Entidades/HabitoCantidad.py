from Entidades.Habito import Habito

class HabitoCantidad(Habito):
    """Hábito que se completa al alcanzar una cantidad objetivo."""

    def __init__(self, identificador:int , nombre: str, frecuencia:str, importancia: int,  objetivo:int) -> None:
        super().__init__(identificador, nombre, frecuencia, importancia)
        self._objetivo : int = objetivo
        self._cantidad_actual : int= 0

    @property
    def objetivo(self) -> int:
        return self._objetivo

    @property
    def cantidad_actual(self) -> int:
        return self._cantidad_actual

    def agregar_cantidad(self, cantidad:int) -> None:
        self._cantidad_actual += cantidad

    def reiniciar(self) -> None:
        self._cantidad_actual = 0

    def cumplido(self) -> bool :
        return self._cantidad_actual >= self._objetivo

    def notificar(self) -> None:
        restante = self._objetivo - self._cantidad_actual
        if restante > 0:
            print(f"[{self._nombre}] Te faltan {restante} unidades. ¡Sigue así!")
        else:
            print(f"¡Enhorabuena, [{self._nombre}]! ¡Objetivo alcanzado!")

    def __str__(self) -> str:
        estado = "Cumplido" if self.cumplido() else "En progreso"
        return f"Cantidad: {self._nombre} ({self._frecuencia}) - {self._cantidad_actual}/{self._objetivo} - {estado}"