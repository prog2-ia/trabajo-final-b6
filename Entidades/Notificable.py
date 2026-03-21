class Notificable:
    def notificar(self):
        raise NotImplementedError

    def mensaje_alerta(self):
        return f"⚠️ Recuerda completar tu hábito!"