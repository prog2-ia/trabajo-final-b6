from Entidades.Hábito import Habito
from Entidades.Notificable import Notificable

# Lo que hace esta clase es marcar como si o no

class HabitoCheck(Habito, Notificable):

    def __init__(self, identificador, nombre, frecuencia, importancia):
        super().__init__(identificador, nombre, frecuencia, importancia)
        self._completado = False

    @property
    def completado(self):
        return self._completado

    def marcar_completado(self):
        self._completado = True

    def reiniciar(self):
        self._completado = False

    # Método abstracto de la clase Habito
    def cumplido(self):
        return self._completado

    def notificar(self):
        if not self._completado:
            print(f"🔔 [{self._nombre}] {self.mensaje_alerta()}")
        else:
            print(f"✅ [{self._nombre}] ¡Ya completado!")

    def __str__(self):
        if self._completado:
            estado="✓ Hecho"
        else:
            estado="✗ Pendiente"

        return f"[CHECK] {self._nombre} ({self._frecuencia}) - {estado}"