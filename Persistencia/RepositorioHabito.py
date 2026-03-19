class RepositorioHabito:
    """Almacena hábitos en memoria."""

    def __init__(self):
        self._habitos = {}  # diccionario: id -> objeto Habito

    def agregar(self, habito):
        self._habitos[habito.identificador] = habito

    def eliminar(self, identificador):
        if identificador in self._habitos:
            del self._habitos[identificador]
            return True

        return False


    def obtener(self, identificador):
        return self._habitos.get(identificador)

    def obtener_todos(self):
        return list(self._habitos.values())