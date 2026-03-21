class RepositorioReviewHabito:
    """Gestiona el almacenamiento de reviews de hábitos."""
    def __init__(self):
        self._reviews = []

    def anadir_review(self, review):
        self._reviews.append(review)

    def mostrar_reviews(self):
        return self._reviews

    def eliminar_review(self, review):
        if review in self._reviews:
            self._reviews.remove(review)

    def total_reviews(self):
        return len(self._reviews)
