class Historial:
    def __init__(self):
        self.registros= {}

    def progreso(self, fecha, habito,progreso):
        if habito.nombre not in self.registros:
            self.registros[habito.nombre]={}

            self.registros[habito.nombre][fecha]= progreso