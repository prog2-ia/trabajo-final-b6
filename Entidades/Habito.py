from abc import ABC, abstractmethod

class Habito(ABC):
    """
    Crea la estructura del habito que añade el usuario.
    Puede ser de tipo check o cantidad
    """
    total_habitos = 0

    def __init__(self, identificador:int , nombre: str, frecuencia:int, importancia: int, fecha=None):
        self._identificador : int = identificador
        self._nombre : str = nombre
        self._frecuencia : int = frecuencia
        self._activo = True
        # Podríamos usar Habitos.total_habitos y seguiría funcionando, pero si en un futuro separamos HabitoCheck y HabitoCantidad, se quedaría en la clase base
        type(self).total_habitos += 1
        self._importancia : int = importancia
        if fecha == None:
            self._fecha : list = []
        else:
            self._fecha = fecha

        self._reviews : list= []

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

    # Sobrecarga del operador < para comparar por importancia
    def __lt__(self, other):
        return self._importancia < other._importancia

    # Método abstracto
    @abstractmethod
    def cumplido(self):
        pass