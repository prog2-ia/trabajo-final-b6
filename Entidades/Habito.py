from abc import ABC, abstractmethod
from typing import Any

class Habito(ABC):
    """
    Crea la estructura del habito que añade el usuario.
    Puede ser de tipo check o cantidad
    """
    total_habitos = 0

    def __init__(self, identificador:int , nombre: str, frecuencia:str, importancia: int, fecha: list[str] | None = None) -> None:
        self._identificador : int = identificador
        self._nombre : str = nombre
        self._frecuencia : str = frecuencia
        self._activo: bool = True
        # Podríamos usar Habitos.total_habitos y seguiría funcionando, pero si en un futuro separamos HabitoCheck y HabitoCantidad, se quedaría en la clase base
        type(self).total_habitos += 1
        self._importancia : int = importancia

        if fecha == None:
            self._fecha : list[str] = []
        else:
            self._fecha  = fecha

        self._reviews: list[str]= []

    #Propiedades (control de acceso)
    @property
    def importancia(self) -> int:
        return  self._importancia

    @importancia.setter
    def importancia(self, value:int) -> None:
        if value < 1 or value > 5:
            print("El valor de importancia debe estar entre el 1 y 5")
        else:
            self._importancia = value
    @property
    def identificador(self) -> int:
        return self._identificador

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def frecuencia(self) -> str:
        return self._frecuencia

    @property
    def activo(self) -> bool:
        return self._activo

    #Métodos de instancia

    def poner_review(self, review:Any) -> None:
        self._reviews.append(review)

    def activar(self) -> None:
        self._activo = True

    def pausar(self) -> None:
        self._activo = False

    @classmethod
    def total(cls) -> int:
        return cls.total_habitos

    # Sobrecarga del operador < para comparar por importancia
    def __lt__(self, other: "Habito") -> bool:
        return self._importancia < other._importancia

    # Método abstracto
    @abstractmethod
    def cumplido(self) -> bool:
        pass