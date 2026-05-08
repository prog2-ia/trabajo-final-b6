from Entidades.Habito import Habito

class RepositorioHabito:
    """Almacena hábitos en memoria."""

    def __init__(self)->None:
        self._habitos: dict[int, Habito] = {}  # diccionario: id -> objeto Habito

    def agregar(self, habito: Habito)->None:

        if not isinstance(habito, Habito):
            raise TypeError("Solo se pueden almacenar objetos del tipo Habito")

        if habito.identificador in self._habitos:
            raise KeyError(f"Ya existe un hábito con el identificador {habito.identificador}")

        self._habitos[habito.identificador] = habito

    def eliminar(self, identificador:int)->bool:

        if not isinstance(identificador, int):
            raise TypeError("El identificador debe ser un entero")

        if identificador in self._habitos:
            del self._habitos[identificador]
            return True

        return False


    def obtener(self, identificador:int)->Habito | None:

        if not isinstance(identificador, int):
            raise TypeError("El identificador debe ser un número entero")

        return self._habitos.get(identificador)

    def obtener_todos(self)->list[Habito]:
        return list(self._habitos.values())