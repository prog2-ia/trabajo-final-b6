from abc import ABC, abstractmethod

class Habito(ABC):

    total_habitos = 0

    def __init__(self, identificador, nombre, frecuencia):
        self._identificador = identificador
        self._nombre = nombre
        self._frecuencia = frecuencia
        self._activo = True
        type(self).total_habitos += 1

    #Propiedades

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

    #Métodos

    def activar(self):
        self._activo = True

    def pausar(self):
        self._activo = False

    @classmethod
    def total(cls):
        return cls.total_habitos

    # Método abstracto: cada subclase lo implementa a su manera
    @abstractmethod
    def cumplido(self):
        pass