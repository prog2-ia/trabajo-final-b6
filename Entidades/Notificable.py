class Notificable:
    """Clase que se aplica a quelas que pueden genera notificaciones"""
    def notificar(self):
        return NotImplementedError

    def mensaje_alerta(self):
        return "¡Recuerda completar tu hábito!"