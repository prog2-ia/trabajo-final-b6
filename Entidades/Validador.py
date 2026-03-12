"""
Clase Validador - Validación centralizada de datos
Demuestra: Encapsulamiento, métodos estáticos, responsabilidad única
"""

from entidades.Excepciones import FrecuenciaInvalidaError, HabitoInvalidoError


class Validador:
    """Clase utilitaria para validar datos del sistema de hábitos"""
    
    FRECUENCIAS_VALIDAS = {"diario", "semanal", "mensual"}
    LONGITUD_MINIMA_NOMBRE = 3
    LONGITUD_MAXIMA_NOMBRE = 50
    
    @staticmethod
    def validar_nombre(nombre: str) -> bool:
        """
        Valida que el nombre sea válido
        
        Args:
            nombre: Nombre a validar
        
        Returns:
            True si es válido
        
        Raises:
            HabitoInvalidoError: Si el nombre no es válido
        """
        if not isinstance(nombre, str):
            raise HabitoInvalidoError("El nombre debe ser texto")
        
        if len(nombre.strip()) < Validador.LONGITUD_MINIMA_NOMBRE:
            raise HabitoInvalidoError(
                f"El nombre debe tener al menos {Validador.LONGITUD_MINIMA_NOMBRE} caracteres"
            )
        
        if len(nombre) > Validador.LONGITUD_MAXIMA_NOMBRE:
            raise HabitoInvalidoError(
                f"El nombre no puede exceder {Validador.LONGITUD_MAXIMA_NOMBRE} caracteres"
            )
        
        return True
    
    @staticmethod
    def validar_frecuencia(frecuencia: str) -> bool:
        """
        Valida que la frecuencia sea válida
        
        Args:
            frecuencia: Frecuencia a validar
        
        Returns:
            True si es válido
        
        Raises:
            FrecuenciaInvalidaError: Si la frecuencia no es válida
        """
        if frecuencia.lower() not in Validador.FRECUENCIAS_VALIDAS:
            raise FrecuenciaInvalidaError(frecuencia)
        
        return True
    
    @staticmethod
    def validar_identificador(identificador) -> bool:
        """
        Valida que el identificador sea válido
        
        Args:
            identificador: ID a validar
        
        Returns:
            True si es válido
        
        Raises:
            HabitoInvalidoError: Si el ID no es válido
        """
        if not identificador:
            raise HabitoInvalidoError("El identificador no puede estar vacío")
        
        return True
    
    @staticmethod
    def validar_objetivo(objetivo: float) -> bool:
        """
        Valida que el objetivo sea un número positivo
        
        Args:
            objetivo: Objetivo a validar
        
        Returns:
            True si es válido
        
        Raises:
            HabitoInvalidoError: Si el objetivo no es válido
        """
        if not isinstance(objetivo, (int, float)) or objetivo <= 0:
            raise HabitoInvalidoError("El objetivo debe ser un número positivo")
        
        return True
    
    @staticmethod
    def validar_habito_completo(identificador, nombre: str, frecuencia: str) -> bool:
        """
        Valida todos los campos de un hábito
        
        Args:
            identificador: ID del hábito
            nombre: Nombre del hábito
            frecuencia: Frecuencia del hábito
        
        Returns:
            True si todos son válidos
        
        Raises:
            Diversas excepciones si algo no es válido
        """
        Validador.validar_identificador(identificador)
        Validador.validar_nombre(nombre)
        Validador.validar_frecuencia(frecuencia)
        return True

