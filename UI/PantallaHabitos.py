from Entidades.HabitoCheck import HabitoCheck
from Entidades.HabitoCantidad import HabitoCantidad
from Entidades.Habito import Habito
from Entidades.Rutina import Rutina
from Entidades.ReviewHabito import Review
from Persistencia.RepositorioHabito import RepositorioHabito
from Servicios.ServiciosHabitos import ServiciosHabitos
from Persistencia.RepositorioReviewHabito import RepositorioReviewHabito
from Servicios.ServiciosReviewHabito import ServiciosReviewHabito
from UI.Excepciones import *

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
        tipo = input("Tipo: ")

        try:
            hab_id = int(input("ID del hábito: "))
        except ValorInvalidoError:
            print("Debes introducir un número válido")
            return
        nombre = input("Nombre: ")
        frecuencia = input("Frecuencia (diario/semanal/mensual): ")

        try:
            importancia = int(input("Nivel de importancia: "))
            if importancia < 1 or importancia > 5:
                print("El número debe ser mayor que 1 y menor que 5")
                return
        except ValueError:
            print("Debes introducir un número válido")
            return

        if tipo == "1":
            habito = HabitoCheck(hab_id, nombre, frecuencia, importancia)
        elif tipo == "2":
            try:
                objetivo = int(input("Objetivo: "))
            except ValorInvalidoError:
                print("Error: el objetivo debe ser un número entero")
                return

            habito = HabitoCantidad(hab_id, nombre, frecuencia, importancia, objetivo)
        else:
            print("Tipo no válido.")
            return

        self._servicios.agregar_habito(habito)
        print(f"Hábito '{nombre}' creado correctamente.")

    def ver_habitos(self)->None:
        print("\n---[HÁBITOS]---")
        habitos:list[Habito] = self._servicios.listar_todos()
        if not habitos:
            print("No hay hábitos todavía.")
        else:
            for habito in habitos:
                print(habito)

    def eliminar_habito(self)->None:
        try:
            hab_id = int(input("ID del hábito a eliminar: "))
        except ValorInvalidoError:
            print("Debes introducir un número válido")
            return

        exito = self._servicios.eliminar_habito(hab_id)

        if exito:
            print("Hábito eliminado con éxito")

        else:
            print("Error: el ID introducido no se corresponde con ningún hábito")

    def crear_rutina(self)->None:
        nombre= str(input("Introduce el nombre de la rutina: "))
        rutina = Rutina(nombre)
        self._rutinas.append(rutina)
        print(f"Rutina {nombre} creada satisfactoriamente.")

    def habito_a_rutina(self)->None:
        nombre= str(input("Introduce el nombre de la rutina: "))
        try:
            ident = int(input("ID del hábito a añadir: "))
        except ValorInvalidoError:
            print("Debes introducir un número válido")
            return
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

        rutina_exito.agregar_habito(habito_exito)
        print(f"Hábito {habito_exito}  añadido a la rutina {rutina_exito.nombre}")

    def ver_rutinas(self)->None:
        print("\n---[RUTINAS]---")
        if not self._rutinas:
            print("No hay rutinas")
        else:
            for rutina in self._rutinas:
                rutina.resumen()

    #Buscamos un hábito por su ID para asociarle una review
    def agregar_review(self)->None:
        try:
            ident = int(input("ID del hábito a añadir: "))
        except ValorInvalidoError:
            print("Debes introducir un número válido")
            return

        habito_exito = self._repo.obtener(ident)

        if habito_exito is None:
            print("No existe el habito")
            return

        fecha = input("Fecha: ")

        #Comprobaciones de tipo de los datos introducidos
        try:
            nota = float(input("Nota: "))
        except ValorInvalidoError:
            print("Introduce un número válido")
            return

        if nota < 0 or nota > 10:
            print("La nota debe estar entre 0 y 10")
            return

        comentario = input("Comentario: ")
        while comentario == "":
            print("Error: el comentario no puede estar vacío")
            comentario = input("Comentario: ")

        review = Review(fecha, nota, comentario, habito_exito)
        habito_exito.poner_review(review)
        self._servicios_review.anadir_review(review)
        print("Review agregada satisfactoriamente")

    def ver_reviews(self)->None:
        print("\n---[REVIEWS]---")
        reviews: list[Review] = self._servicios_review.mostrar_reviews()

        if not reviews:
            print("No hay reviews todavía.")
        else:
            for review in reviews:
                print(review)

