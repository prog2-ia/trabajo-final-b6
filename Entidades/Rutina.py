class Rutina:
    #Agrupa varios hábitos bajo un mismo nombre.

    def __init__(self, nombre):
        self.nombre = nombre
        self.habitos = []

    def agregar_habito(self, habito):
        self.habitos.append(habito)

    def resumen(self):
        print(f"\nRutina: {self.nombre}")
        for h in self.habitos:
            print(f"  {h}")
