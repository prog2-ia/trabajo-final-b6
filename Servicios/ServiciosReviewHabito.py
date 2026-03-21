class ServiciosReviewHabito:
    """Gestiona operaciones sobre las reviews almacenadas en el repositorio."""

    def __init__(self, repositorio):
        self._repositorio = repositorio

    def anadir_review(self, review):
        self._repositorio.anadir_review(review)

    def mostrar_reviews(self):
        return self._repositorio.mostrar_reviews()

    def nota_media_reviews(self):
        reviews = self._repositorio.mostrar_reviews()

        if len(reviews) == 0:
            return 0

        else:
            total = 0
            for review in reviews:
                total += review.nota

            return total / len(reviews)

    def buscar_review(self, fecha):

        resultados = []

        for review in self._repositorio.mostrar_reviews():
            if review.fecha == fecha:
                resultados.append(review)

        return resultados

    def review_por_nota(self, nota):

        resultados = []

        for review in self._repositorio.mostrar_reviews():
            if review.nota >= nota:
                resultados.append(review)

        return resultados
