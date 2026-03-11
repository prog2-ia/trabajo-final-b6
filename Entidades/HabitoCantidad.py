
from Hábito import Habito

#definimos la clase hija HabitoCantidad
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

    def verificar_regla(self):
        return self.cantidad_actual >= self.objetivo  # Umbral: objetivo alcanzado
