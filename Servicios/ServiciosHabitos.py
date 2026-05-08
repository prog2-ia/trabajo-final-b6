from Entidades.Habito import Habito
from Persistencia.RepositorioHabito import RepositorioHabito
class ServiciosHabitos:
    """Operaciones sobre la lista de hábitos del repositorio."""

    def __init__(self, repositorio: RepositorioHabito)->None:
        if not isinstance(repositorio, RepositorioHabito):
            raise TypeError("El repositorio debe ser de tipo RepositorioHabito")

        self._repositorio: RepositorioHabito = repositorio

    def agregar_habito(self, habito: Habito)->None:
        if not isinstance(habito, Habito):
            raise TypeError("Solo se pueden agregar objetos de tipo Habito")

        self._repositorio.agregar(habito)

    def eliminar_habito(self, identificador:int)->bool:

        if not isinstance(identificador, int):
            raise TypeError("El identificador debe ser un número entero")

        return self._repositorio.eliminar(identificador)

    def listar_todos(self)->list[Habito]:
        # Ordenamos los hábitos por importancia
        #Hemos usado la sobrecarga del operador < para simplificar el código de la comparación
        habitos: list[Habito] = self._repositorio.obtener_todos()
        for i in range(len(habitos)):
            for j in range(i+1,len(habitos)):
                if habitos[i]<habitos[j]:
                    aux = habitos[i]
                    habitos[i] = habitos[j]
                    habitos[j] = aux

        return habitos

    def listar_cumplidos(self) -> list[Habito]:
        cumplidos: list[Habito]= []

        for h in self._repositorio.obtener_todos():
            if h.cumplido():
                cumplidos.append(h)

        return cumplidos

    def resumen(self) -> tuple[int,int]:
        habitos: list[Habito] = self._repositorio.obtener_todos()
        total: int = len(habitos)
        cumplidos: int = sum(1 for h in habitos if h.cumplido())

        return total, cumplidos