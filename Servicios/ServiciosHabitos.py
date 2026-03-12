"""
Clase ServiciosHabitos - Lógica de negocio
Demuestra: Encapsulamiento, abstracción, operaciones sobre hábitos
"""

from typing import List, Optional
from entidades.Hábito import Habito
from entidades.HabitoCheck import HabitoCheck
from entidades.HabitoCantidad import HabitoCantidad
from entidades.Validador import Validador
from entidades.Excepciones import HabitoInvalidoError, RepositorioError
from persistencia.RepositorioHabito import RepositorioHabito


class ServiciosHabitos:
    """
    Servicio de lógica de negocio para hábitos
    Encapsula operaciones complejas sobre hábitos
    """
    
    def __init__(self, repositorio: RepositorioHabito):
        """
        Inicializa el servicio
        
        Args:
            repositorio: Instancia de RepositorioHabito para persistencia
        """
        self._repositorio = repositorio
    
    def crear_habito_check(self, identificador: str, nombre: str, frecuencia: str) -> HabitoCheck:
        """
        Crear un nuevo hábito de tipo check
        
        Args:
            identificador: ID único
            nombre: Nombre del hábito
            frecuencia: 'diario', 'semanal' o 'mensual'
        
        Returns:
            Objeto HabitoCheck creado
        
        Raises:
            HabitoInvalidoError: Si los datos son inválidos
        """
        try:
            Validador.validar_habito_completo(identificador, nombre, frecuencia)
            
            if self._repositorio.existe(identificador):
                raise HabitoInvalidoError(f"ID {identificador} ya existe")
            
            habito = HabitoCheck(identificador, nombre, frecuencia)
            self._repositorio.agregar(habito)
            return habito
        
        except Exception as e:
            raise HabitoInvalidoError(f"Error al crear hábito check: {str(e)}")
    
    def crear_habito_cantidad(self, identificador: str, nombre: str, 
                            frecuencia: str, objetivo: float) -> HabitoCantidad:
        """
        Crear un nuevo hábito de cantidad
        
        Args:
            identificador: ID único
            nombre: Nombre del hábito
            frecuencia: 'diario', 'semanal' o 'mensual'
            objetivo: Cantidad objetivo
        
        Returns:
            Objeto HabitoCantidad creado
        
        Raises:
            HabitoInvalidoError: Si los datos son inválidos
        """
        try:
            Validador.validar_habito_completo(identificador, nombre, frecuencia)
            Validador.validar_objetivo(objetivo)
            
            if self._repositorio.existe(identificador):
                raise HabitoInvalidoError(f"ID {identificador} ya existe")
            
            habito = HabitoCantidad(identificador, nombre, frecuencia, objetivo=objetivo)
            self._repositorio.agregar(habito)
            return habito
        
        except Exception as e:
            raise HabitoInvalidoError(f"Error al crear hábito cantidad: {str(e)}")
    
    def obtener_habito(self, identificador: str) -> Optional[Habito]:
        """Obtener un hábito por ID"""
        return self._repositorio.obtener(identificador)
    
    def obtener_todos(self) -> List[Habito]:
        """Obtener todos los hábitos"""
        return self._repositorio.obtener_todos()
    
    def obtener_activos(self) -> List[Habito]:
        """Obtener solo hábitos activos"""
        return self._repositorio.obtener_activos()
    
    def obtener_por_frecuencia(self, frecuencia: str) -> List[Habito]:
        """
        Obtener hábitos por frecuencia
        
        Args:
            frecuencia: 'diario', 'semanal' o 'mensual'
        
        Returns:
            Lista de hábitos con esa frecuencia
        """
        try:
            Validador.validar_frecuencia(frecuencia)
            return [h for h in self._repositorio.obtener_todos() 
                    if h.frecuencia == frecuencia.lower()]
        except Exception:
            return []
    
    def obtener_por_tipo(self, tipo: str) -> List[Habito]:
        """
        Obtener hábitos por tipo
        
        Args:
            tipo: 'check' o 'cantidad'
        
        Returns:
            Lista de hábitos del tipo especificado
        """
        return self._repositorio.obtener_por_tipo(tipo)
    
    def marcar_completado(self, identificador: str) -> bool:
        """
        Marcar un hábito check como completado
        
        Args:
            identificador: ID del hábito
        
        Returns:
            True si se marcó exitosamente
        """
        habito = self._repositorio.obtener(identificador)
        if not habito or not isinstance(habito, HabitoCheck):
            return False
        
        try:
            habito.marcar_completado()
            self._repositorio.actualizar(habito)
            return True
        except Exception:
            return False
    
    def agregar_cantidad(self, identificador: str, cantidad: float) -> bool:
        """
        Agregar cantidad a un hábito de cantidad
        
        Args:
            identificador: ID del hábito
            cantidad: Cantidad a agregar
        
        Returns:
            True si se agregó exitosamente
        """
        habito = self._repositorio.obtener(identificador)
        if not habito or not isinstance(habito, HabitoCantidad):
            return False
        
        try:
            habito.agregar_cantidad(cantidad)
            self._repositorio.actualizar(habito)
            return True
        except Exception:
            return False
    
    def activar_habito(self, identificador: str) -> bool:
        """Activar un hábito pausado"""
        habito = self._repositorio.obtener(identificador)
        if not habito:
            return False
        
        habito.activar()
        self._repositorio.actualizar(habito)
        return True
    
    def pausar_habito(self, identificador: str) -> bool:
        """Pausar un hábito activo"""
        habito = self._repositorio.obtener(identificador)
        if not habito:
            return False
        
        habito.pausar()
        self._repositorio.actualizar(habito)
        return True
    
    def eliminar_habito(self, identificador: str) -> bool:
        """Eliminar un hábito"""
        return self._repositorio.eliminar(identificador)
    
    def reiniciar_habito(self, identificador: str) -> bool:
        """
        Reiniciar un hábito (para un nuevo período)
        
        Args:
            identificador: ID del hábito
        
        Returns:
            True si se reinició
        """
        habito = self._repositorio.obtener(identificador)
        if not habito:
            return False
        
        habito.reiniciar()
        self._repositorio.actualizar(habito)
        return True
    
    def obtener_estadisticas_rapidas(self) -> dict:
        """
        Obtener estadísticas rápidas del usuario
        
        Returns:
            Diccionario con estadísticas
        """
        todos = self._repositorio.obtener_todos()
        activos = self._repositorio.obtener_activos()
        checks = self._repositorio.obtener_por_tipo("check")
        cantidades = self._repositorio.obtener_por_tipo("cantidad")
        
        # Contar completados
        checks_completados = sum(1 for h in checks if isinstance(h, HabitoCheck) and h.completado)
        cantidades_cumplidas = sum(1 for h in cantidades if isinstance(h, HabitoCantidad) and h.cumplido())
        
        return {
            "total_habitos": len(todos),
            "habitos_activos": len(activos),
            "habitos_pausados": len(todos) - len(activos),
            "checks_totales": len(checks),
            "checks_completados": checks_completados,
            "cantidades_totales": len(cantidades),
            "cantidades_cumplidas": cantidades_cumplidas
        }
    
    def obtener_resumen_completo(self) -> str:
        """
        Obtener un resumen textual completo
        
        Returns:
            String con resumen formateado
        """
        stats = self.obtener_estadisticas_rapidas()
        todos = self._repositorio.obtener_todos()
        
        resumen = "="*60 + "\n"
        resumen += "📊 RESUMEN DE HÁBITOS\n"
        resumen += "="*60 + "\n\n"
        
        resumen += f"📈 Estadísticas Generales:\n"
        resumen += f"  • Total de hábitos: {stats['total_habitos']}\n"
        resumen += f"  • Activos: {stats['habitos_activos']} ✓\n"
        resumen += f"  • Pausados: {stats['habitos_pausados']} ⏸\n\n"
        
        resumen += f"✓ Hábitos Check:\n"
        resumen += f"  • Total: {stats['checks_totales']}\n"
        resumen += f"  • Completados: {stats['checks_completados']}\n\n"
        
        resumen += f"📊 Hábitos de Cantidad:\n"
        resumen += f"  • Total: {stats['cantidades_totales']}\n"
        resumen += f"  • Cumplidos: {stats['cantidades_cumplidas']}\n\n"
        
        resumen += "Listado de Hábitos:\n"
        resumen += "-"*60 + "\n"
        
        if not todos:
            resumen += "No hay hábitos creados\n"
        else:
            for habito in todos:
                resumen += f"  {habito}\n"
        
        resumen += "="*60 + "\n"
        return resumen
