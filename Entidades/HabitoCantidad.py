from Entidades.Habito import Habito


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

    def cumplido(self):
        return self._cantidad_actual >= self._objetivo

    def notificar(self):
        restante = self._objetivo - self._cantidad_actual
        if restante > 0:
            print(f"[{self._nombre}] Te faltan {restante} unidades. {self.mensaje_alerta()}")
        else:
            print(f"[{self._nombre}] ¡Objetivo alcanzado!")

    def __str__(self):
        estado = "Cumplido" if self.cumplido() else "En progreso"
        return f"Cantidad: {self._nombre} ({self._frecuencia}) - {self._cantidad_actual}/{self._objetivo} - {estado}"