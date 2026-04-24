from Entidades.Habito import Habito

class RepositorioHabito:
    """Almacena hábitos en memoria."""

    def __init__(self)->None:
        self._habitos: dict[int, Habito] = {}  # diccionario: id -> objeto Habito

    def agregar(self, habito: Habito)->None:
        self._habitos[habito.identificador] = habito

    def eliminar(self, identificador:int)->bool:
        if identificador in self._habitos:
            del self._habitos[identificador]
            return True

        return False


    def obtener(self, identificador:int)->Habito | None:
        return self._habitos.get(identificador)

    def obtener_todos(self)->list[Habito]:
        return list(self._habitos.values())