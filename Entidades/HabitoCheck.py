from Entidades.Hábito import Habito


class HabitoCheck(Habito):
    """Hábito que se completa marcándolo como hecho (sí/no)."""

    def __init__(self, identificador, nombre, frecuencia):
        super().__init__(identificador, nombre, frecuencia)
        self._completado = False

    @property
    def completado(self):
        return self._completado

    def marcar_completado(self):
        self._completado = True

    def reiniciar(self):
        self._completado = False

    # Implementación del método abstracto
    def cumplido(self):
        return self._completado

    def __str__(self):
        estado = "✓ Hecho" if self._completado else "✗ Pendiente"
        return f"[CHECK] {self._nombre} ({self._frecuencia}) - {estado}"