from Hábito import Habito

#definimos la clase hija HabitoCheck

class HabitoCheck(Habito): #marca si el habito está hecho o no
    def __init__(self, identificador, nombre, frecuencia, activo):
        super().__init__(identificador, nombre, frecuencia,  activo)
        self.completado= False

    def marcar_completado(self):
        self.completado = True

    def reiniciar(self):
        self.completado = False