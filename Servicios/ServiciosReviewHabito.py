from Entidades.ReviewHabito import Review
from Persistencia.RepositorioReviewHabito import RepositorioReviewHabito

class ServiciosReviewHabito:
    """Gestiona operaciones sobre las reviews almacenadas en el repositorio."""

    def __init__(self, repositorio: RepositorioReviewHabito) -> None:
        self._repositorio: RepositorioReviewHabito = repositorio

    def anadir_review(self, review)-> None:
        self._repositorio.anadir_review(review)

    def mostrar_reviews(self)-> list[Review]:
        return self._repositorio.mostrar_reviews()

    def nota_media_reviews(self)->float:
        reviews: list[Review] = self._repositorio.mostrar_reviews()

        if len(reviews) == 0:
            return 0.0

        else:
            total:float = 0.0
            for review in reviews:
                total += review.nota

            return total / len(reviews)

    def buscar_review(self, fecha:str)->list[Review]:

        resultados = []

        for review in self._repositorio.mostrar_reviews():
            if review.fecha == fecha:
                resultados.append(review)

        return resultados

    def review_por_nota(self, nota:float)->list[Review]:

        resultados: list[Review] = []

        for review in self._repositorio.mostrar_reviews():
            if review.nota >= nota:
                resultados.append(review)

        return resultados
