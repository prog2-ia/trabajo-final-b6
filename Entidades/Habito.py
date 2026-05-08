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
        self.nombre : str = nombre
        self.frecuencia : str = frecuencia
        self._activo: bool = True
        # Podríamos usar Habitos.total_habitos y seguiría funcionando, pero si en un futuro separamos HabitoCheck y HabitoCantidad, se quedaría en la clase base
        type(self).total_habitos += 1
        self.importancia : int = importancia

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

        if not isinstance(value, int):
            raise TypeError("La importancia debe ser un número entero")

        if value < 1 or value > 5:
            raise ValueError("El valor de importancia debe estar entre el 1 y 5")

        self._importancia = value

    @property
    def identificador(self) -> int:
        return self._identificador

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value:str) -> None:
        if not isinstance(value, str):
            raise TypeError("El nombre del hábito debe ser de tipo str")

        if value=="":
            raise ValueError("El nombre del hábito no puede estar vacía")

        self._nombre = value

    @property
    def frecuencia(self) -> str:
        return self._frecuencia

    @frecuencia.setter
    def frecuencia(self, value:str) -> None:
        if not isinstance(value, str):
            raise TypeError("La frecuencia debe ser de tipo str")

        if value not in ("diario", "semanal", "mensual"):
            raise ValueError("La frecuencia debe ser una de las siguientes opciones: diario, semanal o mensual")

        self._frecuencia = value

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