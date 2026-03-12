"""
Clase HabitoCheck - Hábito de tipo "Sí/No" o "Completado/No Completado"
Demuestra: Herencia, encapsulamiento, polimorfismo
"""
from entidades.Hábito import Habito


#definimos la clase hija HabitoCheck

class HabitoCheck(Habito): #marca si el habito está hecho o no
    def __init__(self, identificador, nombre, frecuencia, activo):
        super().__init__(identificador, nombre, frecuencia,  activo)
        self.completado= False

    def marcar_completado(self):
        """Marcar el hábito como completado"""
        if not self._activo:
            raise ValueError("No se puede completar un hábito pausado")
        self._completado = True
    
    def desmarcar_completado(self):
        """Desmarcar el hábito (no completado)"""
        self._completado = False
    
    def reiniciar(self):
        """Reiniciar el hábito para un nuevo período"""
        self._completado = False
    
    def cumplido(self) -> bool:
        """Verificar si está cumplido (implementación de método abstracto)"""
        return self._completado
    
    def verificar_regla(self) -> bool:
        """
        Verificar si se cumple la regla del hábito (implementación de método abstracto)
        Para HabitoCheck: es cumplido si está marcado como completado
        """
        return self._completado
    
    def obtener_progreso_texto(self) -> str:
        """Obtener descripción del progreso"""
        return "✓ Completado" if self._completado else "✗ No completado"
    
    def __str__(self) -> str:
        """Representación en string mejorada"""
        estado_habito = "✓ Activo" if self._activo else "✗ Pausado"
        progreso = "✓ Hecho" if self._completado else "○ Pendiente"
        return f"[CHECK] {self._nombre} ({self._frecuencia}) [{estado_habito}] {progreso}"
    
    def __repr__(self) -> str:
        """Representación técnica"""
        return f"HabitoCheck(id={self._identificador}, nombre={self._nombre}, completado={self._completado})"
