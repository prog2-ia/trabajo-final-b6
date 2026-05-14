from Entidades.Habito import Habito
from UI.Excepciones import ErrorHabitoDuplicado
import os

class RepositorioHabito:
    """Almacena hábitos en memoria."""
    ARCHIVO = "data/habitos.txt"

    def __init__(self)->None:
        self._habitos: dict[int, Habito] = {}  # diccionario: id -> objeto Habito
        self._cargar()
    def _cargar(self) -> None:
        """Carga los hábitos desde el archivo usando eval()"""
        if not os.path.exists(self.ARCHIVO):
            return

        try:
            with open(self.ARCHIVO, "r", encoding="utf-8") as f:
                contenido = f.read()
                if contenido.strip():
                    # El archivo tiene formato: id:repr(habito)\n
                    for linea in contenido.strip().split("\n"):
                        if linea:
                            id_str, repr_habito = linea.split(":", 1)
                            id_hab = int(id_str)
                            # RECONSTRUIR el objeto desde su representación string
                            habito = eval(repr_habito)
                            self._habitos[id_hab] = habito
        except Exception as e:
            print(f"Error al cargar: {e}")

    def _guardar(self) -> None:
        """Guarda todos los hábitos usando repr()"""
        # Asegurar que la carpeta existe
        os.makedirs("data", exist_ok=True)

        try:
            with open(self.ARCHIVO, "w", encoding="utf-8") as f:
                for id_hab, habito in self._habitos.items():
                    # Guardamos id:repr(habito)
                    f.write(f"{id_hab}:{repr(habito)}\n")
        except Exception as e:
            print(f"Error al guardar: {e}")


    def agregar(self, habito: Habito)->None:

        if not isinstance(habito, Habito):
            raise TypeError("Solo se pueden almacenar objetos del tipo Habito")

        if habito.identificador in self._habitos:
            raise ErrorHabitoDuplicado(f"Ya existe un hábito con el identificador {habito.identificador}")

        self._habitos[habito.identificador] = habito
        self._guardar()
    def eliminar(self, identificador:int)->bool:

        if not isinstance(identificador, int):
            raise TypeError("El identificador debe ser un entero")

        if identificador in self._habitos:
            del self._habitos[identificador]
            self._guardar()
            return True
        return False


    def obtener(self, identificador:int)->Habito | None:

        if not isinstance(identificador, int):
            raise TypeError("El identificador debe ser un número entero")

        return self._habitos.get(identificador)

    def obtener_todos(self)->list[Habito]:
        return list(self._habitos.values())