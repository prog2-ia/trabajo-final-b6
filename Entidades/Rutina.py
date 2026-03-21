class Rutina:
    #Agrupa varios hábitos bajo un mismo nombre.

    @property
    def nombre(self):
        return self._nombre

    @property
    def habitos(self):
        return self._habitos

    def __init__(self, nombre):
        self._nombre = nombre
        self._habitos = []

    def agregar_habito(self, habito):
        self._habitos.append(habito)

    def resumen(self):
        print(f"\nRutina: {self._nombre}")
        for h in self._habitos:
            print(f"  {h}")
