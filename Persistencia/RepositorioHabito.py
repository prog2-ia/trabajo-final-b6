"""
Clase RepositorioHabito - Persistencia y gestión de datos
Demuestra: Patrón Repository, encapsulamiento, manejo de errores
"""

import json
import os
from typing import List, Optional
from entidades.Hábito import Habito
from entidades.HabitoCheck import HabitoCheck
from entidades.HabitoCantidad import HabitoCantidad
from entidades.Excepciones import RepositorioError, HabitoYaExisteError


class RepositorioHabito:
    """
    Repositorio para persistencia de hábitos
    Implementa el patrón Repository para abstraer el acceso a datos
    """
    
    def __init__(self, ruta_archivo: str = "datos/habitos.json"):
        """
        Inicializa el repositorio
        
        Args:
            ruta_archivo: Ruta del archivo JSON donde guardar datos
        """
        self._ruta_archivo = ruta_archivo
        self._habitos_cache: dict[str, Habito] = {}
        self._crear_directorio()
    
    def _crear_directorio(self):
        """Crear directorio si no existe"""
        directorio = os.path.dirname(self._ruta_archivo)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)
    
    def agregar(self, habito: Habito):
        """
        Agregar un nuevo hábito
        
        Args:
            habito: Objeto Habito a guardar
        
        Raises:
            HabitoYaExisteError: Si el hábito ya existe
        """
        if habito.identificador in self._habitos_cache:
            raise HabitoYaExisteError(f"Hábito con ID {habito.identificador} ya existe")
        
        self._habitos_cache[habito.identificador] = habito
        self.guardar()
    
    def actualizar(self, habito: Habito):
        """
        Actualizar un hábito existente
        
        Args:
            habito: Objeto Habito con datos actualizados
        
        Raises:
            RepositorioError: Si el hábito no existe
        """
        if habito.identificador not in self._habitos_cache:
            raise RepositorioError(f"Hábito con ID {habito.identificador} no encontrado")
        
        self._habitos_cache[habito.identificador] = habito
        self.guardar()
    
    def obtener(self, identificador) -> Optional[Habito]:
        """
        Obtener un hábito por ID
        
        Args:
            identificador: ID del hábito
        
        Returns:
            Objeto Habito o None si no existe
        """
        return self._habitos_cache.get(identificador)
    
    def obtener_todos(self) -> List[Habito]:
        """
        Obtener todos los hábitos
        
        Returns:
            Lista de hábitos
        """
        return list(self._habitos_cache.values())
    
    def obtener_activos(self) -> List[Habito]:
        """
        Obtener solo hábitos activos
        
        Returns:
            Lista de hábitos activos
        """
        return [h for h in self._habitos_cache.values() if h.activo]
    
    def obtener_por_tipo(self, tipo: str) -> List[Habito]:
        """
        Obtener hábitos de un tipo específico
        
        Args:
            tipo: 'check' o 'cantidad'
        
        Returns:
            Lista de hábitos del tipo especificado
        """
        if tipo.lower() == "check":
            return [h for h in self._habitos_cache.values() if isinstance(h, HabitoCheck)]
        elif tipo.lower() == "cantidad":
            return [h for h in self._habitos_cache.values() if isinstance(h, HabitoCantidad)]
        else:
            return []
    
    def eliminar(self, identificador) -> bool:
        """
        Eliminar un hábito
        
        Args:
            identificador: ID del hábito a eliminar
        
        Returns:
            True si se eliminó, False si no existía
        """
        if identificador in self._habitos_cache:
            del self._habitos_cache[identificador]
            self.guardar()
            return True
        return False
    
    def existe(self, identificador) -> bool:
        """
        Verificar si un hábito existe
        
        Args:
            identificador: ID del hábito
        
        Returns:
            True si existe
        """
        return identificador in self._habitos_cache
    
    def contar(self) -> int:
        """
        Contar total de hábitos
        
        Returns:
            Número de hábitos
        """
        return len(self._habitos_cache)
    
    def guardar(self):
        """
        Guardar todos los hábitos en archivo JSON
        
        Raises:
            RepositorioError: Si hay error al guardar
        """
        try:
            datos = {}
            for identificador, habito in self._habitos_cache.items():
                datos[identificador] = self._serializar_habito(habito)
            
            with open(self._ruta_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
        
        except Exception as e:
            raise RepositorioError(f"Error al guardar hábitos: {str(e)}")
    
    def cargar(self):
        """
        Cargar hábitos desde archivo JSON
        
        Raises:
            RepositorioError: Si hay error al cargar
        """
        try:
            if not os.path.exists(self._ruta_archivo):
                self._habitos_cache = {}
                return
            
            with open(self._ruta_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
            
            self._habitos_cache = {}
            for identificador, datos_habito in datos.items():
                habito = self._deserializar_habito(datos_habito)
                if habito:
                    self._habitos_cache[identificador] = habito
        
        except Exception as e:
            raise RepositorioError(f"Error al cargar hábitos: {str(e)}")
    
    def limpiar(self):
        """Limpiar todos los hábitos (útil para tests)"""
        self._habitos_cache.clear()
        self.guardar()
    
    @staticmethod
    def _serializar_habito(habito: Habito) -> dict:
        """Convertir hábito a diccionario para JSON"""
        datos_base = {
            "tipo": habito.__class__.__name__,
            "identificador": habito.identificador,
            "nombre": habito.nombre,
            "frecuencia": habito.frecuencia,
            "activo": habito.activo,
            "recordatorio": habito.tiene_recordatorio,
            "dia_recordatorio": habito.dia_recordatorio,
            "hora_recordatorio": habito.hora_recordatorio
        }
        
        if isinstance(habito, HabitoCheck):
            datos_base["completado"] = habito.completado
        
        elif isinstance(habito, HabitoCantidad):
            datos_base["objetivo"] = habito.objetivo
            datos_base["cantidad_actual"] = habito.cantidad_actual
        
        return datos_base
    
    @staticmethod
    def _deserializar_habito(datos: dict) -> Optional[Habito]:
        """Convertir diccionario JSON a objeto Habito"""
        try:
            tipo = datos.get("tipo")
            
            if tipo == "HabitoCheck":
                habito = HabitoCheck(
                    datos["identificador"],
                    datos["nombre"],
                    datos["frecuencia"],
                    datos["activo"]
                )
                if datos["completado"]:
                    habito.marcar_completado()
            
            elif tipo == "HabitoCantidad":
                habito = HabitoCantidad(
                    datos["identificador"],
                    datos["nombre"],
                    datos["frecuencia"],
                    datos["activo"],
                    datos["objetivo"]
                )
                habito.establecer_cantidad(datos["cantidad_actual"])
            
            else:
                return None
            
            # Restaurar recordatorio
            if datos.get("recordatorio") and datos.get("dia_recordatorio"):
                habito.activar_recordatorio(
                    datos["dia_recordatorio"],
                    datos["hora_recordatorio"]
                )
            
            return habito
        
        except Exception:
            return None
