from Entidades.Habito import Habito
from Persistencia.RepositorioHabito import RepositorioHabito

class ServiciosHabitos:
    """Operaciones sobre la lista de hábitos del repositorio."""

    def __init__(self, repositorio: RepositorioHabito)->None:
        self._repositorio: RepositorioHabito = repositorio

    def agregar_habito(self, habito: Habito)->None:
        self._repositorio.agregar(habito)

    def eliminar_habito(self, identificador:int)->bool:
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