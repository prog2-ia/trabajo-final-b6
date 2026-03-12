"""
Clase HabitoCantidad - Hábito medible con cantidad objetivo
Demuestra: Herencia, encapsulamiento, propiedades, validación
"""
from entidades.Hábito import Habito
from entidades.Validador import Validador


class HabitoCantidad(Habito):
    """
    Hábito que se completa al alcanzar una cantidad/objetivo
    Ejemplo: "Beber 2 litros de agua", "Hacer 30 flexiones", "Leer 20 páginas"
    """
    
    def __init__(self, identificador, nombre: str, frecuencia: str, activo: bool = True, objetivo: float = 1):
        """
        Inicializa un hábito de cantidad
        
        Args:
            identificador: ID único
            nombre: Nombre del hábito
            frecuencia: 'diario', 'semanal' o 'mensual'
            activo: Si está activo (default: True)
            objetivo: Cantidad objetivo a alcanzar
        
        Raises:
            HabitoInvalidoError: Si objetivo no es válido
        """
        super().__init__(identificador, nombre, frecuencia, activo)
        
        # Validar objetivo
        Validador.validar_objetivo(objetivo)
        
        self._objetivo = objetivo
        self._cantidad_actual = 0
    
    @property
    def objetivo(self) -> float:
        """Obtener objetivo"""
        return self._objetivo
    
    @objetivo.setter
    def objetivo(self, valor: float):
        """Establecer objetivo con validación"""
        Validador.validar_objetivo(valor)
        self._objetivo = valor
    
    @property
    def cantidad_actual(self) -> float:
        """Obtener cantidad actual"""
        return self._cantidad_actual
    
    @property
    def progreso_porcentaje(self) -> float:
        """
        Calcular progreso como porcentaje
        
        Returns:
            Porcentaje completado (0-100)
        """
        if self._objetivo == 0:
            return 0
        porcentaje = (self._cantidad_actual / self._objetivo) * 100
        return min(porcentaje, 100)  # Máximo 100%
    
    def agregar_cantidad(self, cantidad: float):
        """
        Agregar cantidad al progreso
        
        Args:
            cantidad: Cantidad a agregar (debe ser positiva)
        
        Raises:
            ValueError: Si cantidad es negativa o no activo
        """
        if not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un número positivo")
        
        if not self._activo:
            raise ValueError("No se puede agregar cantidad a un hábito pausado")
        
        self._cantidad_actual += cantidad
    
    def restar_cantidad(self, cantidad: float):
        """
        Restar cantidad del progreso
        
        Args:
            cantidad: Cantidad a restar
        """
        if cantidad > self._cantidad_actual:
            self._cantidad_actual = 0
        else:
            self._cantidad_actual -= cantidad
    
    def establecer_cantidad(self, cantidad: float):
        """
        Establecer cantidad a un valor específico
        
        Args:
            cantidad: Nueva cantidad
        """
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._cantidad_actual = cantidad
    
    def reiniciar(self):
        """Reiniciar el progreso para un nuevo período"""
        self._cantidad_actual = 0
    
    def cumplido(self) -> bool:
        """Verificar si el objetivo se ha alcanzado (implementación de método abstracto)"""
        return self._cantidad_actual >= self._objetivo
    
    def verificar_regla(self) -> bool:
        """
        Verificar si se cumple la regla del hábito (implementación de método abstracto)
        Para HabitoCantidad: es cumplido si alcanza el objetivo
        """
        return self._cantidad_actual >= self._objetivo
    
    def obtener_progreso_texto(self) -> str:
        """Obtener descripción del progreso"""
        return f"{self._cantidad_actual}/{self._objetivo} ({self.progreso_porcentaje:.1f}%)"
    
    def __str__(self) -> str:
        """Representación en string mejorada"""
        estado_habito = "✓ Activo" if self._activo else "✗ Pausado"
        progreso = self.obtener_progreso_texto()
        cumplido = "✓" if self.cumplido() else "○"
        return f"[CANTIDAD] {self._nombre} ({self._frecuencia}) [{estado_habito}] {progreso} {cumplido}"
    
    def __repr__(self) -> str:
        """Representación técnica"""
        return f"HabitoCantidad(id={self._identificador}, nombre={self._nombre}, cantidad={self._cantidad_actual}/{self._objetivo})"
