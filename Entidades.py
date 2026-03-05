#Definimos la clase padre Habito de la que derivaran el resto de clases hijas



class Habito:
    total_habitos=0
    def __init__(self, identificador, nombre, frecuencia, activo, recordatorio = False):
        self.identificador = identificador
        self.nombre = nombre
        self.frecuencia = frecuencia
        self.activo = activo
        self.recordatorio = recordatorio
        self.dia = None
        self.hora = None
        type(self).total_habitos += 1

#Inicializamos el atributo recordatorio en false porque no sabemos si el ususario quiere ser avisado o simplemente quiere una to-do list


    #Creamos los métodos de instancia
    def activar (self):
        self.activo = True

    def esta_activo(self):
        return self.activo

    def activar_recordatorio(self, dia, hora):
        self.recordatorio = True
        self.dia=dia
        self.hora=hora

    def desactivar_recordatorio(self):
        self.recordatorio = False
        self.dia = None
        self.hora = None


    def pausar(self):
        self.activo=False


    #Creamos métodos de clase
    @classmethod
    def total_habito(cls):
        return f'El usuario tiene un total de {cls.total_habitos}'


    #definimos la clase hija HabitoCheck

class HabitoCheck(Habito): #marca si el habito está hecho o no
    def __init__(self, identificador, nombre, frecuencia, activo):
        super().__init__(identificador, nombre, frecuencia,  activo)
        self.completado= False

    def marcar_completado(self):
        self.completado = True

    def reiniciar(self):
        self.completado = False

class HabitoCantidad(Habito):
    def __init__(self, identificador, nombre, frecuencia, activo, objetivo):
        super().__init__(identificador,nombre, frecuencia, activo)
        self.objetivo = objetivo
        self.cantidad_actual=0

    def anadir_cantidad(self, cantidad):
        self.cantidad_actual += cantidad

    def cumplido (self):
        return self.cantidad_actual >= self.objetivo

    def reiniciar(self):
        super().activar()
        self.cantidad_actual = False

    def esta_activo(self):
        return self.activo