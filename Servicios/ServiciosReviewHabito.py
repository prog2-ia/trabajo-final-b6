from Entidades import ReviewHabito
class ServiciosReviewHabito:
    def __init__(self, repositorio):
        self._repositorio = repositorio

    def mostrar_reviews(self):
        return self._repositorio.mostrar_reviews()


    def nota_media_reviews(self):
        reviews = self._repositorio.mostrar_reviews()

        if len(reviews) == 0:
            return 0


        else:
            total=0
            for review in reviews:
                total+= review._nota

            return total/len(reviews)


    def buscar_review(self,fecha):

        resultados=[]

        for review in self._repositorio.mostrar_reviews():
            if review.fecha==fecha:
                resultados.append(review)


        return resultados

    def review_por_nota(self,nota):

        resultados=[]

        for review in self._repositorio.mostrar_reviews():
            if review.nota>=nota:
                resultados.append(review)

        return resultados