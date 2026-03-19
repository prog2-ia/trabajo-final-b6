
class ServiciosHabitos:
    """Operaciones sobre la lista de hábitos del repositorio."""

    def __init__(self, repositorio):
        self._repositorio = repositorio

    def agregar_habito(self, habito):
        self._repositorio.agregar(habito)

    def eliminar_habito(self, identificador):
        return self._repositorio.eliminar(identificador)

    def listar_todos(self):
        return self._repositorio.obtener_todos()


    def listar_cumplidos(self):
        cumplidos= []

        for h in self._repositorio.obtener_todos():
            if h.cumplido():
                cumplidos.append(h)

        return cumplidos

    def resumen(self):
        habitos = self._repositorio.obtener_todos()
        total = len(habitos)
        cumplidos = sum(1 for h in habitos if h.cumplido())
        return total, cumplidos