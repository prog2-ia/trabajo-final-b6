from Entidades.HabitoCheck import HabitoCheck
from Entidades.HabitoCantidad import HabitoCantidad
from Persistencia.RepositorioHabito import RepositorioHabito
from Servicios.ServiciosHabitos import ServiciosHabitos



class PantallaHabitos:

    def __init__(self):
        self._repo = RepositorioHabito()
        self._servicios = ServiciosHabitos(self._repo)

    def iniciar(self):
        opcion = ""
        while opcion != "4":
            print("\n=== MENÚ DE HÁBITOS ===")
            print("1. Crear hábito")
            print("2. Ver todos los hábitos")
            print("3. Eliminar hábito")
            print("4. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                self._crear_habito()
            elif opcion == "2":
                self._ver_habitos()
            elif opcion == "3":
                self._eliminar_habito()
            elif opcion == "4":
                print("¡Hasta luego!")
            else:
                print("Opción no válida.")

    def _crear_habito(self):
        print("\n¿Qué tipo de hábito?")
        print("1. Check (sí/no)")
        print("2. Cantidad (con objetivo)")
        tipo = input("Tipo: ")

        id = input("ID del hábito: ")
        nombre = input("Nombre: ")
        frecuencia = input("Frecuencia (diario/semanal/mensual): ")

        if tipo == "1":
            habito = HabitoCheck(id, nombre, frecuencia)
        elif tipo == "2":
            objetivo = float(input("Objetivo: "))
            habito = HabitoCantidad(id, nombre, frecuencia, objetivo)
        else:
            print("Tipo no válido.")
            return

        self._servicios.agregar_habito(habito)
        print(f"Hábito '{nombre}' creado correctamente.")

    def _ver_habitos(self):
        print("\n=== HÁBITOS ===")
        habitos = self._repo.obtener_todos()
        if not habitos:
            print("No hay hábitos todavía.")
        else:
            self._servicios.listar_todos()

    def _eliminar_habito(self):
        id = input("ID del hábito a eliminar: ")
        self._servicios.eliminar_habito(id)
        print("Hábito eliminado.")