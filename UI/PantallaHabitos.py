from Entidades.HabitoCheck import HabitoCheck
from Entidades.HabitoCantidad import HabitoCantidad
from Entidades.Habito import Habito
from Entidades.Rutina import Rutina
from Entidades.ReviewHabito import Review
from Persistencia.RepositorioHabito import RepositorioHabito
from Servicios.ServiciosHabitos import ServiciosHabitos
from Persistencia.RepositorioReviewHabito import RepositorioReviewHabito
from Servicios.ServiciosReviewHabito import ServiciosReviewHabito

class PantallaHabitos:
    """
    Pantalla principal del programa,
    desde aquí el usuario controla el gestor de hábitos mediante distintas opciones
    """
    def __init__(self)->None:
        self._repo: RepositorioHabito = RepositorioHabito()
        self._servicios: ServiciosHabitos = ServiciosHabitos(self._repo)
        self._rutinas: list[Rutina] = []
        self._repo_review: RepositorioReviewHabito = RepositorioReviewHabito()
        self._servicios_review: ServiciosReviewHabito = ServiciosReviewHabito(self._repo_review)

    def iniciar(self)->None:
        opcion = ""
        while opcion != "9":
            print("\n---[MENÚ DE HÁBITOS]---")
            print("1. Crear hábito")
            print("2. Ver todos los hábitos")
            print("3. Eliminar hábito")
            print("4. Crear Rutina")
            print("5. Añadir hábito a rutina")
            print("6. Ver rutinas")
            print("7. Añadir review a hábito")
            print("8. Ver reviews")
            print("9. Salir")
            opcion = input("Elige una opción: ")

            habito: Habito
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
                self.ver_reviews()
            elif opcion == "9":
                print("¡Hasta luego!")
            else:
                print("Opción no válida.")

    def crear_habito(self)->None:
        print("\n¿Qué tipo de hábito?")
        print("1. Check (sí/no)")
        print("2. Cantidad (con objetivo)")

        while True:
            try:
                tipo = int(input("Tipo: "))
                if tipo in [1, 2]:
                    break
                else:
                    print("Dato erróneo: debe ser 1 o 2. Intenta de nuevo.")
            except ValueError:
                print("Dato erróneo: debe ser un número")

        while True:
            id_str = input("ID del hábito (número entero positivo): ")
            if not id_str.isdigit():
                print("Error: El ID debe ser un número entero positivo. Intenta de nuevo.")
                continue
            hab_id = int(id_str)
            if self._servicios._repositorio.obtener(hab_id) is not None:
                print(f"Error: Ya existe un hábito con el ID {hab_id}. Usa otro ID.")
                continue
            break



        nombre = input("Nombre: ")

        while True:
            frecuencia = input("Frecuencia (diario/semanal/mensual): ").strip().lower()
            if frecuencia in ['diario', 'semanal', 'mensual']:
                break
            else:
                print("Error: La frecuencia debe de ser 'diario', 'semanal' o 'mensual'.")

        while True:
            importancia_str = input("Nivel de importancia: ")
            if not importancia_str.isdigit():
                print("Error: Debes introducir un número entre 1 y 5. Intenta de nuevo.")
                continue
            importancia = int(importancia_str)
            if 1 <= importancia <= 5:
                break
            else:
                print("Error: La importancia debe ser un número entre 1 y 5. Intenta de nuevo.")


        if tipo == 1:
            habito = HabitoCheck(hab_id, nombre, frecuencia, importancia)
            self._servicios.agregar_habito(habito)
            print(f"Hábito '{nombre}' creado correctamente.")

        elif tipo == 2:
            while True:
                obj_str = input("Objetivo: ")
                if not obj_str.isdigit():
                    print("Error: Debes introducir un número válido.")
                    continue
                objetivo = int(obj_str)
                if objetivo > 0:
                    break
                else:
                    print("Error: El objetivo debe ser mayor que 0.")

            habito = HabitoCantidad(hab_id, nombre, frecuencia, importancia, objetivo)
            self._servicios.agregar_habito(habito)
            print(f"Hábito '{nombre}' creado correctamente.")

        else:
            print("Tipo no válido.")
            return


    def ver_habitos(self)->None:
        print("\n---[HÁBITOS]---")
        habitos:list[Habito] = self._servicios.listar_todos()
        if not habitos:
            print("No hay hábitos todavía.")
        else:
            for habito in habitos:
                print(habito)

    def eliminar_habito(self)->None:
        while True:
            try:
                hab_id = int(input("ID del hábito a eliminar: "))
                break
            except ValueError:
                print("Debes introducir un número válido")

        exito = self._servicios.eliminar_habito(hab_id)

        if exito:
            print("Hábito eliminado con éxito")

        else:
            print("Error: el ID introducido no se corresponde con ningún hábito")

    def crear_rutina(self)->None:
        while True:
            nombre= str(input("Introduce el nombre de la rutina: "))
            if nombre:
                break
            else:
                print('Error: El nombre no puede estar vacío')

        rutina = Rutina(nombre)
        self._rutinas.append(rutina)
        print(f"Rutina {nombre} creada satisfactoriamente.")

    def habito_a_rutina(self)->None:

        while True:
            nombre= str(input("Introduce el nombre de la rutina: "))
            if nombre:
                break
            else:
                print('Error: El nombre no puede estar vacío')
        while True:
            try:
                ident = int(input("ID del hábito a añadir: "))
                break
            except ValueError:
                print("Debes introducir un número válido")
            #Comprobamos si el nombre y el id existen para poder realizar la operación

        rutina_exito= None
        for rutina in self._rutinas:
            if rutina.nombre == nombre:
                rutina_exito = rutina

        if rutina_exito is None:
            print("No existe esa rutina")
            return

        habito_exito=self._repo.obtener(ident)

        if habito_exito is None:
            print("No existe ese habito")
            return

        try:
            rutina_exito.agregar_habito(habito_exito)
            print(f"Hábito '{habito_exito.nombre}' añadido a la rutina '{rutina_exito.nombre}'")
        except Exception as e:
            print(f"Error: {e}")

    def ver_rutinas(self)->None:
        print("\n---[RUTINAS]---")
        if not self._rutinas:
            print("No hay rutinas")
        else:
            for rutina in self._rutinas:
                try:
                    rutina.resumen()
                except Exception as e:
                    print(f"Error al mostrar la rutina '{rutina.nombre}': {e}")

    #Buscamos un hábito por su ID para asociarle una review
    def agregar_review(self)->None:
        while True:
            try:
                ident = int(input("ID del hábito a añadir: "))
                break
            except ValueError:
                print("Debes introducir un número válido")

        habito_exito = self._repo.obtener(ident)

        if habito_exito is None:
            print("No existe el habito")
            return

        while True:
            fecha = input("Fecha (ej: 2024-01-15): ").strip()
            if fecha:
                break
            else:
                print("Error: La fecha no puede estar vacía. Intenta de nuevo.")

        #Comprobaciones de tipo de los datos introducidos
        while True:
            try:
                nota = float(input("Nota: "))
                if 0<= nota <=10:
                    break
                else:
                    print('Error: La nota debe de estar entre 0 y 10')
            except ValueError:
                print("Introduce un número válido")

        while True:
            comentario = input("Comentario: ").strip()
            if comentario:
                break
            else:
                print("Error: El comentario no puede estar vacío. Intenta de nuevo.")

        try:
            review = Review(fecha, nota, comentario, habito_exito)
            habito_exito.poner_review(review)
            self._servicios_review.anadir_review(review)
            print("Review agregada satisfactoriamente")
        except Exception as e:
            print(f"Error al crear la review: {e}")

    def ver_reviews(self)->None:
        print("\n---[REVIEWS]---")
        reviews: list[Review] = self._servicios_review.mostrar_reviews()

        if not reviews:
            print("No hay reviews todavía.")
        else:
            for review in reviews:
                print(review)

