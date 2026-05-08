class ErrorHabitos(Exception):
    """Clase para errores de hábitos"""
    pass

class ErrorHabitoDuplicado(ErrorHabitos):
    """Lanza un error si ya existe un hábito con el  mismo identificador"""
    pass

class HabitoNoEncontradoError(ErrorHabitos):
    """Se lanza cuando no se encuentra un hábito."""
    pass


class RutinaNoEncontradaError(ErrorHabitos):
    """Se lanza cuando no se encuentra una rutina."""
    pass


class ValorInvalidoError(ErrorHabitos):
    """Se lanza cuando un dato introducido no es válido."""
    pass


class ReviewInvalidaError(ErrorHabitos):
    """Se lanza cuando una review tiene datos incorrectos."""
    pass