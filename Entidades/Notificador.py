"""
Clases Notificador - Sistema de notificaciones polimórfico
Demuestra: ABC, herencia, polimorfismo, encapsulamiento
"""

from abc import ABC, abstractmethod
from datetime import datetime


class Notificador(ABC):
    """
    Clase abstracta base para notificadores
    Permite diferentes formas de enviar notificaciones
    """
    
    def __init__(self, nombre: str):
        """Inicializa el notificador"""
        self._nombre = nombre
        self._activo = True
        self._historial_notificaciones = []
    
    @property
    def nombre(self) -> str:
        """Obtener nombre del notificador"""
        return self._nombre
    
    @property
    def activo(self) -> bool:
        """Obtener estado del notificador"""
        return self._activo
    
    def activar(self):
        """Activar el notificador"""
        self._activo = True
    
    def desactivar(self):
        """Desactivar el notificador"""
        self._activo = False
    
    def obtener_historial(self) -> list:
        """Obtener historial de notificaciones"""
        return self._historial_notificaciones.copy()
    
    def limpiar_historial(self):
        """Limpiar historial de notificaciones"""
        self._historial_notificaciones.clear()
    
    @abstractmethod
    def enviar(self, asunto: str, mensaje: str) -> bool:
        """
        Enviar notificación
        
        Args:
            asunto: Asunto de la notificación
            mensaje: Cuerpo del mensaje
        
        Returns:
            True si se envió correctamente
        """
        pass
    
    def _registrar_notificacion(self, asunto: str, mensaje: str):
        """Registrar notificación en el historial (método protegido)"""
        registro = {
            "fecha": datetime.now(),
            "asunto": asunto,
            "mensaje": mensaje,
            "tipo": self.__class__.__name__
        }
        self._historial_notificaciones.append(registro)


class NotificadorConsola(Notificador):
    """Notificador que envía mensajes por consola"""
    
    def __init__(self):
        super().__init__("Consola")
    
    def enviar(self, asunto: str, mensaje: str) -> bool:
        """
        Enviar notificación a consola
        
        Args:
            asunto: Asunto de la notificación
            mensaje: Cuerpo del mensaje
        
        Returns:
            True siempre (éxito garantizado)
        """
        if not self._activo:
            return False
        
        print("\n" + "="*50)
        print(f"📢 NOTIFICACIÓN - {asunto}")
        print("="*50)
        print(f"{mensaje}")
        print("="*50 + "\n")
        
        self._registrar_notificacion(asunto, mensaje)
        return True


class NotificadorEmail(Notificador):
    """Notificador que simula envío por email"""
    
    def __init__(self, servidor_smtp: str = "smtp.ejemplo.com"):
        super().__init__("Email")
        self._servidor_smtp = servidor_smtp
        self._destinatarios = []
    
    def agregar_destinatario(self, email: str):
        """Agregar email destinatario"""
        if "@" in email and "." in email:
            self._destinatarios.append(email)
    
    def obtener_destinatarios(self) -> list:
        """Obtener lista de destinatarios"""
        return self._destinatarios.copy()
    
    def enviar(self, asunto: str, mensaje: str) -> bool:
        """
        Enviar notificación por email (simulado)
        
        Args:
            asunto: Asunto del email
            mensaje: Cuerpo del email
        
        Returns:
            True si se envió correctamente
        """
        if not self._activo or not self._destinatarios:
            return False
        
        print(f"\n📧 EMAIL ENVIADO")
        print(f"Servidor: {self._servidor_smtp}")
        print(f"Para: {', '.join(self._destinatarios)}")
        print(f"Asunto: {asunto}")
        print(f"Mensaje: {mensaje}\n")
        
        self._registrar_notificacion(asunto, mensaje)
        return True


class NotificadorSMS(Notificador):
    """Notificador que simula envío por SMS"""
    
    def __init__(self, proveedor: str = "Twilio"):
        super().__init__("SMS")
        self._proveedor = proveedor
        self._numeros_telefonicos = []
    
    def agregar_numero(self, numero: str):
        """Agregar número telefónico"""
        # Validación simple
        if numero.replace("+", "").replace("-", "").isdigit():
            self._numeros_telefonicos.append(numero)
    
    def obtener_numeros(self) -> list:
        """Obtener lista de números"""
        return self._numeros_telefonicos.copy()
    
    def enviar(self, asunto: str, mensaje: str) -> bool:
        """
        Enviar notificación por SMS (simulado)
        
        Args:
            asunto: Título (se ignora para SMS)
            mensaje: Contenido del SMS (máx 160 caracteres)
        
        Returns:
            True si se envió correctamente
        """
        if not self._activo or not self._numeros_telefonicos:
            return False
        
        # Validar longitud de SMS
        if len(mensaje) > 160:
            print(f"⚠️ Mensaje truncado a 160 caracteres")
            mensaje = mensaje[:160]
        
        print(f"\n📱 SMS ENVIADO")
        print(f"Proveedor: {self._proveedor}")
        print(f"Para: {', '.join(self._numeros_telefonicos)}")
        print(f"Mensaje: {mensaje}\n")
        
        self._registrar_notificacion(asunto, mensaje)
        return True


class GestorNotificadores:
    """Gestor centralizado de notificadores (Patrón Manager)"""
    
    def __init__(self):
        """Inicializa el gestor"""
        self._notificadores = {}
    
    def registrar_notificador(self, notificador: Notificador):
        """Registrar un notificador"""
        self._notificadores[notificador.nombre] = notificador
    
    def eliminar_notificador(self, nombre: str):
        """Eliminar un notificador"""
        if nombre in self._notificadores:
            del self._notificadores[nombre]
    
    def obtener_notificador(self, nombre: str) -> Notificador:
        """Obtener un notificador específico"""
        return self._notificadores.get(nombre)
    
    def obtener_todos(self) -> dict:
        """Obtener todos los notificadores"""
        return self._notificadores.copy()
    
    def notificar_a_todos(self, asunto: str, mensaje: str) -> dict:
        """
        Enviar notificación a través de todos los notificadores activos
        
        Returns:
            Diccionario con resultados de cada notificador
        """
        resultados = {}
        for nombre, notificador in self._notificadores.items():
            if notificador.activo:
                resultados[nombre] = notificador.enviar(asunto, mensaje)
        return resultados

