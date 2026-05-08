class Notificable:
    """Clase que se aplica a quelas que pueden genera notificaciones"""
    def notificar(self) -> None:
        return

    def mensaje_alerta(self) -> str:
        return "¡Recuerda completar tu hábito!"