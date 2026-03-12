"""
Clase Recordatorio - Gestión de recordatorios con encapsulamiento
Demuestra: Encapsulamiento, atributos privados, propiedades
"""

class Recordatorio:
    """Clase para gestionar recordatorios con validación"""
    
    # Horas válidas
    HORAS_VALIDAS = set(range(0, 24))
    
    def __init__(self, dia: int, hora: int):
        """
        Inicializa un recordatorio
        
        Args:
            dia: Día de la semana (1-7: Lunes a Domingo)
            hora: Hora del día (0-23)
        
        Raises:
            ValueError: Si los valores no son válidos
        """
        self.__dia = None
        self.__hora = None
        self.__activo = False
        
        # Usar setters para validar
        self.dia = dia
        self.hora = hora
    
    @property
    def dia(self) -> int:
        """Obtener día del recordatorio"""
        return self.__dia
    
    @dia.setter
    def dia(self, valor: int):
        """Establecer día con validación (1-7)"""
        if not isinstance(valor, int) or valor < 1 or valor > 7:
            raise ValueError(f"Día debe estar entre 1 y 7, recibido: {valor}")
        self.__dia = valor
    
    @property
    def hora(self) -> int:
        """Obtener hora del recordatorio"""
        return self.__hora
    
    @hora.setter
    def hora(self, valor: int):
        """Establecer hora con validación (0-23)"""
        if not isinstance(valor, int) or valor not in self.HORAS_VALIDAS:
            raise ValueError(f"Hora debe estar entre 0 y 23, recibido: {valor}")
        self.__hora = valor
    
    @property
    def activo(self) -> bool:
        """Obtener estado del recordatorio"""
        return self.__activo
    
    def activar(self):
        """Activar el recordatorio"""
        self.__activo = True
    
    def desactivar(self):
        """Desactivar el recordatorio"""
        self.__activo = False
    
    def obtener_informacion(self) -> dict:
        """Obtener información del recordatorio como diccionario"""
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        return {
            "dia": dias_semana[self.__dia - 1],
            "hora": f"{self.__hora:02d}:00",
            "activo": self.__activo
        }
    
    def __str__(self) -> str:
        """Representación en string"""
        dias_semana = ["", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        estado = "✓ Activo" if self.__activo else "✗ Inactivo"
        return f"Recordatorio: {dias_semana[self.__dia]} a las {self.__hora:02d}:00 [{estado}]"
    
    def __eq__(self, otro) -> bool:
        """Comparar dos recordatorios"""
        if not isinstance(otro, Recordatorio):
            return False
        return self.__dia == otro.dia and self.__hora == otro.hora

