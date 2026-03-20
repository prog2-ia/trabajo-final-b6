from Entidades.HabitoCheck import HabitoCheck
from Entidades.HabitoCantidad import HabitoCantidad
from Entidades.Rutina import Rutina
from Entidades.ReviewHabito import Review

from Persistencia.RepositorioHabito import RepositorioHabito
from Servicios.ServiciosHabitos import ServiciosHabitos


class PantallaHabitos:

    def __init__(self):
        self._repo = RepositorioHabito()
        self._servicios = ServiciosHabitos(self._repo)
        self._rutinas = []

    def iniciar(self):
        opcion = ""
        while opcion != "8":
            print("\n---[MENÚ DE HÁBITOS]---")
            print("1. Crear hábito")
            print("2. Ver todos los hábitos")
            print("3. Eliminar hábito")
            print("4. Crear Rutina")
            print("6. Ver rutinas")
            print("5. Añadir hábito a rutina")
            print("7. Añadir review a hábito")
            print("8. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.crear_habito()
            elif opcion == "2":
                self.ver_habitos()
            elif opcion == "3":
                self.eliminar_habito()
            elif opcion == "4":
                self.crear_rutina()
            elif opcion == "5":
                self.habito_a_rutina()
            elif opcion == "6":
                self.ver_rutinas()
            elif opcion == "7":
                self.agregar_review()
            elif opcion == "8":
                print("¡Hasta luego!")
            else:
                print("Opción no válida.")

    def crear_habito(self):
        print("\n¿Qué tipo de hábito?")
        print("1. Check (sí/no)")
        print("2. Cantidad (con objetivo)")
        tipo = input("Tipo: ")

        hab_id = input("ID del hábito: ")
        nombre = input("Nombre: ")
        frecuencia = input("Frecuencia (diario/semanal/mensual): ")
        importancia = int(input("Nivel de importancia: "))

        while importancia < 1 or importancia > 5:
            print("Error: la importancia debe estar entre 1 y 5")
            importancia = int(input("Nivel de importancia: "))

        if tipo == "1":
            habito = HabitoCheck(hab_id, nombre, frecuencia, importancia)
        elif tipo == "2":
            objetivo = float(input("Objetivo: "))
            habito = HabitoCantidad(hab_id, nombre, frecuencia, importancia, objetivo)
        else:
            print("Tipo no válido.")
            return

        while importancia < 1 or importancia > 5:
            print("Error: la importancia debe estar entre 1 y 5")
            importancia = int(input("Nivel de importancia: "))

        self._servicios.agregar_habito(habito)
        print(f"Hábito '{nombre}' creado correctamente.")

    def ver_habitos(self):
        print("\n---[HÁBITOS]---")
        habitos = self._servicios.listar_todos()
        if not habitos:
            print("No hay hábitos todavía.")
        else:
            for habito in habitos:
                print(habito)

    def eliminar_habito(self):
        hab_id = input("ID del hábito a eliminar: ")
        exito= self._servicios.eliminar_habito(hab_id)

        if exito:
            print("Hábito eliminado con éxito")

        else:
            print("Error: el ID introducido no se corresponde con ningún hábito")

    def crear_rutina(self):
        nombre= str(input("Introduce el nombre de la rutina: "))
        rutina = Rutina(nombre)
        self._rutinas.append(rutina)
        print(f"Rutina {nombre} creada satisfactoriamente.")
    def habito_a_rutina(self, habito_exito=None):
        nombre= str(input("Introduce el nombre de la rutina: "))
        ident= input("ID del hábito a añadir")

        #Aqui comprobamos si el nombre y el id existen para poder realizar la operación

        rutina_exito= None
        for rutina in self._rutinas:
            if rutina.nombre == nombre:
                rutina_exito = rutina

        if rutina_exito == None:
            print("No existe esa rutina")

        habito_exito= None
        for habito in self._repo.obtener_todos():
            if habito.identificador == ident:
                habito_exito = habito

        if habito_exito== None:
            print("No existe ese habito")
            return

        rutina_exito.agregar_habito(habito_exito)
        print(f"Hábito {habito_exito}  añadido a la rutina {rutina_exito}")

    def ver_rutinas(self):
        print("\n---[RUTINAS]---")
        if not self._rutinas:
            print("No hay rutinas")
        else:
            for rutina in self._rutinas:
                rutina.resumen()

    def agregar_review(self):
        ident= input("ID del hábito: ")
        habito_exito = None
        for habito in self._repo.obtener_todos():
            if habito.identificador == ident:
                habito_exito = habito

        if habito_exito == None:
            print("No existe el habito")
            return

        fecha = input("Fecha: ")
        nota=float(input("Nota: "))
        comentario= str(input("Commentario: "))
        review= Review(fecha, nota, comentario)
        habito.poner_review(review)
        print("Review agregada satisfactoriamente.")


