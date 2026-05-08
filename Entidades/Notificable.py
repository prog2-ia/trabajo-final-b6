class Notificable:
    """Clase que se aplica a quelas que pueden genera notificaciones"""

    def notificar(self, mensaje: str, cumplido: bool) -> None:
        if mensaje.strip() == "":
            raise MensajeVacioError("El mensaje no puede estar vacío")

        if cumplido:
            raise HabitoYaCompletadoError("El hábito ya está completado")

        print(mensaje)


    def mensaje_alerta(self) -> str:
        return "¡Recuerda completar tu hábito!"

class NotificacionError(Exception):
    pass

class MensajeVacioError(NotificacionError):
    pass

class HabitoYaCompletadoError(NotificacionError):
    pass

