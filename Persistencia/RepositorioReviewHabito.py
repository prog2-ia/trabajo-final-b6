from Entidades.ReviewHabito import Review
import os

class RepositorioReviewHabito:
    """Gestiona el almacenamiento de reviews de hábitos."""
    ARCHIVO = "data/reviews.txt"
    def __init__(self)->None:
        self._reviews: list[Review] = []
        self._cargar()

    def _cargar(self) -> None:
        """Carga las reviews desde el archivo"""
        if not os.path.exists(self.ARCHIVO):
            return

        try:
            with open(self.ARCHIVO, "r", encoding="utf-8") as f:
                contenido = f.read()
                if contenido.strip():
                    for linea in contenido.strip().split("\n"):
                        if linea:
                            # Cada línea es un repr(Review)
                            review = eval(linea)
                            self._reviews.append(review)
        except Exception as e:
            print(f"Error al cargar reviews: {e}")

    def _guardar(self) -> None:
        """Guarda todas las reviews"""
        os.makedirs("data", exist_ok=True)

        try:
            with open(self.ARCHIVO, "w", encoding="utf-8") as f:
                for review in self._reviews:
                    f.write(repr(review) + "\n")
        except Exception as e:
            print(f"Error al guardar reviews: {e}")

    def anadir_review(self, review: Review)-> None:

        if not isinstance(review, Review):
            raise TypeError("Solo se pueden añadir objetos de tipo Review")

        self._reviews.append(review)
        self._guardar()


    def mostrar_reviews(self) -> list[Review]:
        return self._reviews

    def eliminar_review(self, review: Review)-> None:

        if not isinstance(review, Review):
            raise TypeError("Solo se pueden añadir objetos de tipo Review")

        if review in self._reviews:
            self._reviews.remove(review)
            self._guardar()

    def total_reviews(self)-> int:
        return len(self._reviews)
