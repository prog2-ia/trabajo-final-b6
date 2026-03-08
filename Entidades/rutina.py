from Hábito import Habito

class Rutina:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitos = []  # Lista de objetos Habito

    def agregar_habito(self, habito):
        self.habitos.append(habito)