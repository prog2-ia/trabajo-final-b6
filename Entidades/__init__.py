"""
Módulo entidades - Contiene todas las clases de negocio
"""

from entidades.Hábito import Habito
from entidades.HabitoCheck import HabitoCheck
from entidades.HabitoCantidad import HabitoCantidad
from entidades.Recordatorio import Recordatorio
from entidades.Notificador import Notificador, NotificadorConsola, NotificadorEmail, NotificadorSMS, GestorNotificadores
from entidades.Estadisticas import Estadistica, RachaConsecutiva, PorcentajeCumplimiento, Tendencia, AnalizadorHabitos
from entidades.Validador import Validador
from entidades.Excepciones import (
    HabitoException, HabitoInvalidoError, HabitoYaExisteError,
    FrecuenciaInvalidaError, RepositorioError, NotificadorError
)

__all__ = [
    'Habito', 'HabitoCheck', 'HabitoCantidad',
    'Recordatorio',
    'Notificador', 'NotificadorConsola', 'NotificadorEmail', 'NotificadorSMS', 'GestorNotificadores',
    'Estadistica', 'RachaConsecutiva', 'PorcentajeCumplimiento', 'Tendencia', 'AnalizadorHabitos',
    'Validador',
    'HabitoException', 'HabitoInvalidoError', 'HabitoYaExisteError',
    'FrecuenciaInvalidaError', 'RepositorioError', 'NotificadorError'
]

