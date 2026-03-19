from Entidades.Hábito import Habito


class HabitoCantidad(Habito):
    """Hábito que se completa al alcanzar una cantidad objetivo."""

    def __init__(self, identificador, nombre, frecuencia, importancia, objetivo):
        super().__init__(identificador, nombre, frecuencia, importancia)
        self._objetivo = objetivo
        self._cantidad_actual = 0

    @property
    def objetivo(self):
        return self._objetivo

    @property
    def cantidad_actual(self):
        return self._cantidad_actual

    def agregar_cantidad(self, cantidad):
        self._cantidad_actual += cantidad

    def reiniciar(self):
        self._cantidad_actual = 0

    # Implementación del método abstracto
    def cumplido(self):
        return self._cantidad_actual >= self._objetivo

    def __str__(self):
        estado = "Cumplido" if self.cumplido() else "En progreso"
        return f"Cantidad: {self._nombre} ({self._frecuencia}) - {self._cantidad_actual}/{self._objetivo} - {estado}"