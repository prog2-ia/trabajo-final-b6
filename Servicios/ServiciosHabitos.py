from entidades.HabitoCheck import HabitoCheck
from entidades.HabitoCantidad import HabitoCantidad


class ServiciosHabitos:
    """Operaciones sobre la lista de hábitos del repositorio."""

    def __init__(self, repositorio):
        self._repositorio = repositorio

    def agregar_habito(self, habito):
        self._repositorio.agregar(habito)

    def eliminar_habito(self, identificador):
        self._repositorio.eliminar(identificador)

    def listar_todos(self):
        for h in self._repositorio.obtener_todos():
            print(h)

    def listar_cumplidos(self):
        for h in self._repositorio.obtener_todos():
            if h.cumplido():
                print(h)

    def resumen(self):
        habitos = self._repositorio.obtener_todos()
        total = len(habitos)
        cumplidos = sum(1 for h in habitos if h.cumplido())
        print(f"Total: {total} | Cumplidos: {cumplidos} | Pendientes: {total - cumplidos}")