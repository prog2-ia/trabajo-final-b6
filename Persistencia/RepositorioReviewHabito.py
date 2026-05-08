from Entidades.ReviewHabito import Review

class RepositorioReviewHabito:
    """Gestiona el almacenamiento de reviews de hábitos."""
    def __init__(self)->None:
        self._reviews: list[Review] = []

    def anadir_review(self, review: Review)-> None:

        if not isinstance(review, Review):
            raise TypeError("Solo se pueden añadir objetos de tipo Review")

        self._reviews.append(review)


    def mostrar_reviews(self) -> list[Review]:
        return self._reviews

    def eliminar_review(self, review: Review)-> None:

        if not isinstance(review, Review):
            raise TypeError("Solo se pueden añadir objetos de tipo Review")

        if review in self._reviews:
            self._reviews.remove(review)

    def total_reviews(self)-> int:
        return len(self._reviews)
