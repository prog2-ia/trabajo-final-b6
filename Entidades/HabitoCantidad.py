from Entidades.Habito import Habito

class HabitoCantidad(Habito):
    """Hábito que se completa al alcanzar una cantidad objetivo."""

    def __init__(self, identificador:int , nombre: str, frecuencia:str, importancia: int,  objetivo:int) -> None:
        super().__init__(identificador, nombre, frecuencia, importancia)
        self.objetivo : int = objetivo
        self._cantidad_actual : int= 0

    @property
    def objetivo(self) -> int:
        return self._objetivo

    @objetivo.setter
    def objetivo(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("El objetivo debe ser un número entero")

        if value <= 0:
            raise ValueError("El objetivo debe ser mayor que 0")

        self._objetivo = value


    @property
    def cantidad_actual(self) -> int:
        return self._cantidad_actual

    def agregar_cantidad(self, cantidad:int) -> None:
        if not isinstance(cantidad, int):
            raise TypeError("La cantidad debe ser un número entero")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0")

        self._cantidad_actual += cantidad

    def reiniciar(self) -> None:
        self._cantidad_actual = 0

    def cumplido(self) -> bool :
        return self._cantidad_actual >= self._objetivo

    def notificar(self) -> None:
        restante = max(0, self._objetivo - self._cantidad_actual)

        if restante > 0:
            print(f"[{self._nombre}] Te faltan {restante} unidades. ¡Sigue así!")
        else:
            print(f"¡Enhorabuena, [{self._nombre}]! ¡Objetivo alcanzado!")

    def __str__(self) -> str:
        estado = "Cumplido" if self.cumplido() else "En progreso"
        return f"Cantidad: {self._nombre} ({self._frecuencia}) - {self._cantidad_actual}/{self._objetivo} - {estado}"

    def __repr__(self) -> str:
        return f"HabitoCantidad({self._identificador}, '{self._nombre}', '{self._frecuencia}', {self._importancia}, {self._objetivo})"