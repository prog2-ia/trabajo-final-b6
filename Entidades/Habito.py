from abc import ABC, abstractmethod

class Habito(ABC):
    """
    Crea la estructura del habito que añade el usuario.
    Puede ser de tipo check o cantidad
    """
    total_habitos = 0

    def __init__(self, identificador, nombre, frecuencia, importancia, fecha=None):
        self._identificador = identificador
        self._nombre = nombre
        self._frecuencia = frecuencia
        self._activo = True
        # Podríamos usar Habitos.total_habitos y seguiría funcionando, pero si en un futuro separamos HabitoCheck y HabitoCantidad, se quedaría en la clase base
        type(self).total_habitos += 1
        self._importancia = importancia
        if fecha == None:
            self._fecha = []
        else:
            self._fecha = fecha

        self._reviews= []

    #Propiedades (control de acceso)
    @property
    def importancia(self):
        return  self._importancia

    @importancia.setter
    def importancia(self, value):
        if value < 1 or value > 5:
            print("El valor de importancia debe estar entre el 1 y 5")
        else:
            self._importancia = value
    @property
    def identificador(self):
        return self._identificador

    @property
    def nombre(self):
        return self._nombre

    @property
    def frecuencia(self):
        return self._frecuencia

    @property
    def activo(self):
        return self._activo

    #Métodos de instancia

    def poner_review(self, review):
        self._reviews.append(review)

    def activar(self):
        self._activo = True

    def pausar(self):
        self._activo = False

    @classmethod
    def total(cls):
        return cls.total_habitos

    # Método abstracto
    @abstractmethod
    def cumplido(self):
        pass