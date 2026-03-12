"""
Clases de Estadísticas - Análisis de progreso de hábitos
Demuestra: ABC, herencia, métodos abstractos, encapsulamiento
"""

from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import List, Dict


class Estadistica(ABC):
    """
    Clase abstracta base para estadísticas
    Define la estructura para calcular diferentes tipos de análisis
    """
    
    def __init__(self, habito):
        """
        Inicializa estadística
        
        Args:
            habito: Objeto hábito a analizar
        """
        self._habito = habito
        self._fecha_calculo = datetime.now()
    
    @property
    def habito(self):
        """Obtener hábito asociado"""
        return self._habito
    
    @property
    def fecha_calculo(self):
        """Obtener fecha del último cálculo"""
        return self._fecha_calculo
    
    @abstractmethod
    def calcular(self) -> float:
        """
        Calcular la estadística
        
        Returns:
            Valor numérico de la estadística
        """
        pass
    
    @abstractmethod
    def obtener_resumen(self) -> str:
        """
        Obtener resumen en texto de la estadística
        
        Returns:
            String con la interpretación de la estadística
        """
        pass


class RachaConsecutiva(Estadistica):
    """Calcula la racha de días consecutivos completados"""
    
    def __init__(self, habito, historial_completados: List[datetime]):
        """
        Inicializa racha
        
        Args:
            habito: Objeto hábito
            historial_completados: Lista de fechas de completación
        """
        super().__init__(habito)
        self._historial_completados = sorted(historial_completados, reverse=True)
        self._racha_actual = 0
        self._racha_maxima = 0
    
    def calcular(self) -> int:
        """
        Calcular racha consecutiva actual
        
        Returns:
            Número de días consecutivos
        """
        if not self._historial_completados:
            self._racha_actual = 0
            return 0
        
        racha = 0
        fecha_esperada = datetime.now().date()
        
        for fecha in self._historial_completados:
            fecha_completacion = fecha.date() if isinstance(fecha, datetime) else fecha
            
            if fecha_completacion == fecha_esperada:
                racha += 1
                fecha_esperada -= timedelta(days=1)
            else:
                break
        
        self._racha_actual = racha
        return racha
    
    def obtener_resumen(self) -> str:
        """Obtener resumen de racha"""
        racha = self.calcular()
        if racha == 0:
            return "Sin racha activa"
        elif racha == 1:
            return "¡Racha de 1 día! Sigue así 🔥"
        elif racha < 7:
            return f"¡Racha de {racha} días! Buen progreso 👍"
        elif racha < 30:
            return f"🔥 ¡Racha de {racha} días! ¡Excelente! 🔥"
        else:
            return f"🏆 ¡INCREÍBLE! {racha} días consecutivos 🏆"


class PorcentajeCumplimiento(Estadistica):
    """Calcula el porcentaje de cumplimiento"""
    
    def __init__(self, habito, total_dias: int, dias_completados: int):
        """
        Inicializa porcentaje
        
        Args:
            habito: Objeto hábito
            total_dias: Total de días en el período
            dias_completados: Días que se completó
        """
        super().__init__(habito)
        self._total_dias = total_dias
        self._dias_completados = dias_completados
    
    def calcular(self) -> float:
        """
        Calcular porcentaje de cumplimiento
        
        Returns:
            Porcentaje (0-100)
        """
        if self._total_dias == 0:
            return 0.0
        
        return (self._dias_completados / self._total_dias) * 100
    
    def obtener_resumen(self) -> str:
        """Obtener resumen de cumplimiento"""
        porcentaje = self.calcular()
        
        if porcentaje == 0:
            return f"Sin completaciones (0%) ❌"
        elif porcentaje < 25:
            return f"Bajo cumplimiento ({porcentaje:.1f}%) 📉"
        elif porcentaje < 50:
            return f"Cumplimiento medio ({porcentaje:.1f}%) 📊"
        elif porcentaje < 75:
            return f"Buen cumplimiento ({porcentaje:.1f}%) 📈"
        elif porcentaje < 100:
            return f"Muy buen cumplimiento ({porcentaje:.1f}%) ⭐"
        else:
            return f"¡Cumplimiento perfecto! (100%) 🏆"


class Tendencia(Estadistica):
    """Analiza la tendencia de cumplimiento (mejorando o empeorando)"""
    
    def __init__(self, habito, ultimos_7_dias: int, dias_anteriores_7: int):
        """
        Inicializa tendencia
        
        Args:
            habito: Objeto hábito
            ultimos_7_dias: Cumplimientos en últimos 7 días
            dias_anteriores_7: Cumplimientos en los 7 días anteriores
        """
        super().__init__(habito)
        self._ultimos_7 = ultimos_7_dias
        self._anteriores_7 = dias_anteriores_7
    
    def calcular(self) -> float:
        """
        Calcular tendencia
        
        Returns:
            Cambio porcentual (-100 a 100)
        """
        if self._anteriores_7 == 0:
            return 0.0 if self._ultimos_7 == 0 else 100.0
        
        return ((self._ultimos_7 - self._anteriores_7) / self._anteriores_7) * 100
    
    def obtener_resumen(self) -> str:
        """Obtener resumen de tendencia"""
        tendencia = self.calcular()
        
        if tendencia > 10:
            return f"📈 Tendencia positiva (+{tendencia:.1f}%) ¡Mejorando!"
        elif tendencia > 0:
            return f"↗️ Ligera mejora (+{tendencia:.1f}%)"
        elif tendencia == 0:
            return "→ Estable (sin cambios)"
        elif tendencia > -10:
            return f"↘️ Ligera caída ({tendencia:.1f}%)"
        else:
            return f"📉 Tendencia negativa ({tendencia:.1f}%) Necesita atención"


class AnalizadorHabitos:
    """Clase para analizar un hábito con múltiples estadísticas"""
    
    def __init__(self):
        """Inicializa analizador"""
        self._estadisticas: Dict[str, Estadistica] = {}
    
    def agregar_estadistica(self, nombre: str, estadistica: Estadistica):
        """Agregar una estadística"""
        self._estadisticas[nombre] = estadistica
    
    def obtener_estadistica(self, nombre: str) -> Estadistica:
        """Obtener una estadística específica"""
        return self._estadisticas.get(nombre)
    
    def calcular_todas(self) -> Dict[str, float]:
        """
        Calcular todas las estadísticas
        
        Returns:
            Diccionario con resultados
        """
        resultados = {}
        for nombre, estadistica in self._estadisticas.items():
            resultados[nombre] = estadistica.calcular()
        return resultados
    
    def obtener_resumen_completo(self) -> str:
        """
        Obtener resumen completo de todas las estadísticas
        
        Returns:
            String con resumen formateado
        """
        resumen = "="*50 + "\n"
        resumen += "📊 ANÁLISIS COMPLETO DEL HÁBITO\n"
        resumen += "="*50 + "\n"
        
        for nombre, estadistica in self._estadisticas.items():
            resumen += f"\n{nombre}:\n"
            resumen += f"  → {estadistica.obtener_resumen()}\n"
        
        resumen += "\n" + "="*50 + "\n"
        return resumen

