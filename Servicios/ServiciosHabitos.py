
class ServiciosHabitos:
    """Operaciones sobre la lista de hábitos del repositorio."""

    def __init__(self, repositorio):
        self._repositorio = repositorio

    # Sobrecarga del operador <
    def __lt__(self, other):
        return self._importancia < other._importancia

    def agregar_habito(self, habito):
        self._repositorio.agregar(habito)

    def eliminar_habito(self, identificador):
        return self._repositorio.eliminar(identificador)

    def listar_todos(self):
        # Ordenamos los hábitos por importancia
        #Hemos usado la sobrecarga del operador < para simplificar el código de la comparación
        habitos = self._repositorio.obtener_todos()
        for i in range(len(habitos)):
            for j in range(i+1,len(habitos)):
                if habitos[i]<habitos[j]:
                    aux = habitos[i]
                    habitos[i] = habitos[j]
                    habitos[j] = aux

        return habitos

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