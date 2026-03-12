# 📖 GUÍA RÁPIDA DE CLASES

Esta guía proporciona un resumen visual de cada clase, qué hace y cómo usarla.

---

## 📋 ÍNDICE RÁPIDO

1. [Habito](#1-habito-clase-abstracta)
2. [HabitoCheck](#2-habitocheck)
3. [HabitoCantidad](#3-habitocantidad)
4. [Recordatorio](#4-recordatorio)
5. [Validador](#5-validador)
6. [Excepciones](#6-excepciones)
7. [Estadisticas](#7-estadisticas)
8. [Notificador](#8-notificador)
9. [RepositorioHabito](#9-repositoriohabito)
10. [ServiciosHabitos](#10-servicioshabitos)

---

## 1️⃣ Habito (Clase Abstracta)

### 🎯 ¿Qué es?
La clase padre que define la estructura y comportamiento común de todos los hábitos.

### 📁 Archivo
`entidades/Hábito.py`

### 🏗️ Estructura
```python
class Habito(ABC):
    # Atributos
    identificador           # ID único
    _nombre                # Nombre (privado)
    _frecuencia            # Frecuencia (privado)
    _activo                # Estado (privado)
    _recordatorio          # Si tiene recordatorio
    _dia, _hora            # Día y hora del recordatorio
    __total_habitos        # Contador de clase
    
    # Métodos públicos
    activar()
    esta_activo() -> bool
    pausar()
    activar_recordatorio(dia, hora)
    desactivar_recordatorio()
    total_habito() -> str
    
    # Métodos abstractos (implementar en subclases)
    @abstractmethod cumplido() -> bool
    @abstractmethod verificar_regla() -> bool
    @abstractmethod reiniciar()
```

### 💡 Ejemplo
```python
# No se puede instanciar directamente (es abstracta)
# habito = Habito("h1", "Test", "diario")  ❌ Error

# Se usan las subclases
habito = HabitoCheck("h1", "Meditar", "diario")  ✅ OK
```

### 🔑 Características
- ✅ No se puede instanciar directamente
- ✅ Define el contrato para subclases
- ✅ Maneja recordatorios
- ✅ Cuenta total de hábitos creados

---

## 2️⃣ HabitoCheck

### 🎯 ¿Qué es?
Un hábito que se marca como "hecho" o "no hecho".

### 📁 Archivo
`entidades/HabitoCheck.py`

### 🏗️ Estructura
```python
class HabitoCheck(Habito):
    # Atributos adicionales
    completado -> bool              # ¿Está hecho?
    
    # Métodos
    marcar_completado()             # Marca como ✓
    desmarcar_completado()          # Marca como ✗
    cumplido() -> bool              # Retorna completado
    verificar_regla() -> bool       # Igual a cumplido()
    reiniciar()                     # Resetea a False
    obtener_progreso_texto() -> str # "✓ Completado" o "✗ No completado"
```

### 💡 Ejemplo
```python
# Crear
habito = HabitoCheck("med1", "Meditar", "diario", activo=True)

# Usar
habito.marcar_completado()
print(habito.completado)           # True
print(habito.cumplido())           # True
print(habito.obtener_progreso_texto())  # "✓ Completado"

# Reiniciar
habito.reiniciar()
print(habito.completado)           # False
```

### 🎬 Casos de Uso
- Meditar
- Hacer ejercicio
- Estudiar
- Escribir un diario
- Tomar vitaminas

---

## 3️⃣ HabitoCantidad

### 🎯 ¿Qué es?
Un hábito que se completa al alcanzar una cantidad/objetivo numérico.

### 📁 Archivo
`entidades/HabitoCantidad.py`

### 🏗️ Estructura
```python
class HabitoCantidad(Habito):
    # Atributos adicionales
    objetivo -> float               # Cantidad a alcanzar
    cantidad_actual -> float        # Cantidad registrada
    progreso_porcentaje -> float    # % de avance (0-100)
    
    # Métodos
    agregar_cantidad(cantidad)      # Suma a cantidad_actual
    restar_cantidad(cantidad)       # Resta de cantidad_actual
    establecer_cantidad(cantidad)   # Fija cantidad_actual
    cumplido() -> bool              # cantidad >= objetivo
    verificar_regla() -> bool       # Igual a cumplido()
    reiniciar()                     # Resetea cantidad a 0
    obtener_progreso_texto() -> str # "X/Y (Z%)"
```

### 💡 Ejemplo
```python
# Crear
habito = HabitoCantidad("agua", "Beber agua", "diario", objetivo=2.0)

# Usar
habito.agregar_cantidad(0.5)   # Añade 0.5L
habito.agregar_cantidad(1.5)   # Añade 1.5L (total 2.0L)

print(habito.cantidad_actual)        # 2.0
print(habito.progreso_porcentaje)    # 100.0
print(habito.cumplido())             # True
print(habito.obtener_progreso_texto())  # "2.0/2.0 (100.0%)"

# Reiniciar para mañana
habito.reiniciar()
print(habito.cantidad_actual)        # 0
```

### 🎬 Casos de Uso
- Beber 2L de agua
- Leer 30 páginas
- Hacer 50 flexiones
- Caminar 10km
- Meditar 20 minutos

---

## 4️⃣ Recordatorio

### 🎯 ¿Qué es?
Gestiona recordatorios con validación de día y hora.

### 📁 Archivo
`entidades/Recordatorio.py`

### 🏗️ Estructura
```python
class Recordatorio:
    # Atributos (privados)
    __dia -> int                    # 1-7 (Lunes-Domingo)
    __hora -> int                   # 0-23
    __activo -> bool                # ¿Está activo?
    
    # Métodos
    activar()                       # Activa recordatorio
    desactivar()                    # Desactiva recordatorio
    obtener_informacion() -> dict   # Info formateada
    
    # Propiedades
    @property dia
    @property hora
    @property activo
```

### 💡 Ejemplo
```python
# Crear recordatorio para lunes a las 8am
rec = Recordatorio(dia=1, hora=8)
rec.activar()

# Obtener info
info = rec.obtener_informacion()
print(info)  # {'dia': 'Lunes', 'hora': '08:00', 'activo': True}

# Usar con hábito
habito = HabitoCheck("h1", "Meditar", "diario")
habito.activar_recordatorio(dia=1, hora=8)
```

### 🎯 Días
```
1 = Lunes
2 = Martes
3 = Miércoles
4 = Jueves
5 = Viernes
6 = Sábado
7 = Domingo
```

---

## 5️⃣ Validador

### 🎯 ¿Qué es?
Clase utilitaria que centraliza toda la validación de datos.

### 📁 Archivo
`entidades/Validador.py`

### 🏗️ Estructura
```python
class Validador:
    # Constantes
    FRECUENCIAS_VALIDAS = {"diario", "semanal", "mensual"}
    LONGITUD_MINIMA_NOMBRE = 3
    LONGITUD_MAXIMA_NOMBRE = 50
    
    # Métodos estáticos
    @staticmethod
    validar_nombre(nombre: str) -> bool
    
    @staticmethod
    validar_frecuencia(frecuencia: str) -> bool
    
    @staticmethod
    validar_identificador(identificador) -> bool
    
    @staticmethod
    validar_objetivo(objetivo: float) -> bool
    
    @staticmethod
    validar_habito_completo(id, nombre, frecuencia) -> bool
```

### 💡 Ejemplo
```python
from entidades.Validador import Validador
from entidades.Excepciones import HabitoInvalidoError

try:
    Validador.validar_nombre("Meditar")     # ✅ OK (7 caracteres)
    Validador.validar_nombre("Xy")          # ❌ Error (muy corto)
    Validador.validar_frecuencia("diario")  # ✅ OK
    Validador.validar_frecuencia("mensualmente")  # ❌ Error
except HabitoInvalidoError as e:
    print(f"Error de validación: {e}")
```

### ✅ Reglas de Validación
- Nombre: 3-50 caracteres
- Frecuencia: "diario", "semanal", "mensual"
- ID: no puede estar vacío
- Objetivo: número > 0

---

## 6️⃣ Excepciones

### 🎯 ¿Qué es?
Sistema de excepciones personalizadas para errores del sistema.

### 📁 Archivo
`entidades/Excepciones.py`

### 🏗️ Estructura
```python
class HabitoException(Exception):          # Base
    pass

class HabitoInvalidoError(HabitoException):  # Datos inválidos
    pass

class HabitoYaExisteError(HabitoException):  # ID duplicado
    pass

class FrecuenciaInvalidaError(HabitoException):  # Frecuencia inválida
    def __init__(self, frecuencia):
        self.frecuencia = frecuencia

class RepositorioError(HabitoException):    # Error de persistencia
    pass

class NotificadorError(HabitoException):    # Error de notificador
    pass
```

### 💡 Ejemplo
```python
from entidades.Excepciones import HabitoInvalidoError, FrecuenciaInvalidaError

try:
    # Error de datos inválidos
    HabitoCheck("h1", "X", "diario")  # Nombre muy corto
except HabitoInvalidoError as e:
    print(f"Datos inválidos: {e}")

try:
    # Error de frecuencia
    HabitoCheck("h1", "Meditar", "mensualmente")
except FrecuenciaInvalidaError as e:
    print(f"Frecuencia inválida: {e.frecuencia}")
```

---

## 7️⃣ Estadisticas

### 🎯 ¿Qué es?
Sistema de análisis de hábitos con diferentes métricas.

### 📁 Archivo
`entidades/Estadisticas.py`

### 🏗️ Clases

#### **Estadistica (Abstracta)**
```python
class Estadistica(ABC):
    @abstractmethod
    calcular() -> float                 # Calcula valor
    
    @abstractmethod
    obtener_resumen() -> str            # Texto interpretativo
```

#### **RachaConsecutiva**
```python
class RachaConsecutiva(Estadistica):
    # Calcula días consecutivos completados
    calcular() -> int
    obtener_resumen() -> str  # "🔥 ¡Racha de X días!"
```

#### **PorcentajeCumplimiento**
```python
class PorcentajeCumplimiento(Estadistica):
    # Calcula % de cumplimiento
    calcular() -> float  # 0-100
    obtener_resumen() -> str  # "X% cumplimiento"
```

#### **Tendencia**
```python
class Tendencia(Estadistica):
    # Analiza mejora/empeoramiento
    calcular() -> float  # Cambio %
    obtener_resumen() -> str  # "📈 Tendencia positiva"
```

#### **AnalizadorHabitos**
```python
class AnalizadorHabitos:
    agregar_estadistica(nombre, estadistica)
    calcular_todas() -> dict
    obtener_resumen_completo() -> str
```

### 💡 Ejemplo
```python
from entidades.Estadisticas import RachaConsecutiva, AnalizadorHabitos
from datetime import datetime, timedelta

# Crear estadísticas
fechas = [
    datetime.now(),
    datetime.now() - timedelta(days=1),
    datetime.now() - timedelta(days=2),
]

racha = RachaConsecutiva(habito, fechas)
print(racha.calcular())  # 3
print(racha.obtener_resumen())  # "🔥 ¡Racha de 3 días!..."

# Usar analizador
analizador = AnalizadorHabitos()
analizador.agregar_estadistica("racha", racha)
print(analizador.obtener_resumen_completo())
```

---

## 8️⃣ Notificador

### 🎯 ¿Qué es?
Sistema polimórfico de notificaciones por diferentes canales.

### 📁 Archivo
`entidades/Notificador.py`

### 🏗️ Clases

#### **Notificador (Abstracta)**
```python
class Notificador(ABC):
    @abstractmethod
    enviar(asunto: str, mensaje: str) -> bool
    
    activar()
    desactivar()
    obtener_historial() -> list
    limpiar_historial()
    
    @property
    nombre -> str
    @property
    activo -> bool
```

#### **NotificadorConsola** (Subclase)
```python
class NotificadorConsola(Notificador):
    enviar(asunto, mensaje) -> bool
    # Imprime en consola
```

#### **NotificadorEmail** (Subclase)
```python
class NotificadorEmail(Notificador):
    agregar_destinatario(email)
    enviar(asunto, mensaje) -> bool
    # Simula envío por email
```

#### **NotificadorSMS** (Subclase)
```python
class NotificadorSMS(Notificador):
    agregar_numero(numero)
    enviar(asunto, mensaje) -> bool
    # Simula envío por SMS (máx 160 caracteres)
```

#### **GestorNotificadores** (Manager)
```python
class GestorNotificadores:
    registrar_notificador(notificador)
    eliminar_notificador(nombre)
    obtener_notificador(nombre) -> Notificador
    obtener_todos() -> dict
    notificar_a_todos(asunto, mensaje) -> dict
```

### 💡 Ejemplo
```python
from entidades.Notificador import (
    GestorNotificadores, NotificadorConsola, 
    NotificadorEmail, NotificadorSMS
)

# Crear gestor
gestor = GestorNotificadores()

# Registrar notificadores
gestor.registrar_notificador(NotificadorConsola())

email = NotificadorEmail()
email.agregar_destinatario("usuario@example.com")
gestor.registrar_notificador(email)

sms = NotificadorSMS()
sms.agregar_numero("+34600123456")
gestor.registrar_notificador(sms)

# Enviar a todos
resultados = gestor.notificar_a_todos(
    asunto="Recordatorio",
    mensaje="¡No olvides tu hábito!"
)
# {'Consola': True, 'Email': True, 'SMS': True}
```

---

## 9️⃣ RepositorioHabito

### 🎯 ¿Qué es?
Maneja la persistencia de hábitos en archivo JSON.

### 📁 Archivo
`persistencia/RepositorioHabito.py`

### 🏗️ Estructura
```python
class RepositorioHabito:
    # Métodos CRUD
    agregar(habito: Habito)
    actualizar(habito: Habito)
    obtener(id) -> Habito
    obtener_todos() -> List[Habito]
    obtener_activos() -> List[Habito]
    obtener_por_tipo(tipo) -> List[Habito]  # 'check' o 'cantidad'
    eliminar(id) -> bool
    existe(id) -> bool
    contar() -> int
    
    # Persistencia
    guardar()  # Guardar en JSON
    cargar()   # Cargar desde JSON
    limpiar()  # Borrar todo
```

### 💡 Ejemplo
```python
from persistencia.RepositorioHabito import RepositorioHabito
from entidades.HabitoCheck import HabitoCheck

# Crear repositorio
repo = RepositorioHabito("datos/habitos.json")

# Cargar hábitos previos
repo.cargar()

# Crear y agregar nuevo
habito = HabitoCheck("h1", "Meditar", "diario")
repo.agregar(habito)

# Obtener
habito = repo.obtener("h1")
todos = repo.obtener_todos()
activos = repo.obtener_activos()

# Guardar cambios
repo.guardar()
```

### 📁 Archivo JSON
```json
{
    "h1": {
        "tipo": "HabitoCheck",
        "identificador": "h1",
        "nombre": "Meditar",
        "frecuencia": "diario",
        "activo": true,
        "recordatorio": false,
        "dia_recordatorio": null,
        "hora_recordatorio": null,
        "completado": false
    },
    "h2": {
        "tipo": "HabitoCantidad",
        "identificador": "h2",
        "nombre": "Beber agua",
        "frecuencia": "diario",
        "activo": true,
        "recordatorio": false,
        "dia_recordatorio": null,
        "hora_recordatorio": null,
        "objetivo": 2.0,
        "cantidad_actual": 1.5
    }
}
```

---

## 🔟 ServiciosHabitos

### 🎯 ¿Qué es?
Capa de lógica de negocio que orquesta las operaciones sobre hábitos.

### 📁 Archivo
`servicios/ServiciosHabitos.py`

### 🏗️ Estructura
```python
class ServiciosHabitos:
    # Constructor
    __init__(repositorio: RepositorioHabito)
    
    # Creación
    crear_habito_check(id, nombre, frecuencia) -> HabitoCheck
    crear_habito_cantidad(id, nombre, frecuencia, objetivo) -> HabitoCantidad
    
    # Consulta
    obtener_habito(id) -> Habito
    obtener_todos() -> List[Habito]
    obtener_activos() -> List[Habito]
    obtener_por_frecuencia(frecuencia) -> List[Habito]
    obtener_por_tipo(tipo) -> List[Habito]
    
    # Operaciones
    marcar_completado(id) -> bool
    agregar_cantidad(id, cantidad) -> bool
    activar_habito(id) -> bool
    pausar_habito(id) -> bool
    eliminar_habito(id) -> bool
    reiniciar_habito(id) -> bool
    
    # Estadísticas
    obtener_estadisticas_rapidas() -> dict
    obtener_resumen_completo() -> str
```

### 💡 Ejemplo
```python
from persistencia.RepositorioHabito import RepositorioHabito
from servicios.ServiciosHabitos import ServiciosHabitos

# Crear servicios
repo = RepositorioHabito()
servicios = ServiciosHabitos(repo)

# Crear hábitos
h1 = servicios.crear_habito_check("ejercicio", "Hacer ejercicio", "diario")
h2 = servicios.crear_habito_cantidad("agua", "Beber 2L", "diario", objetivo=2.0)

# Usar hábitos
servicios.marcar_completado("ejercicio")
servicios.agregar_cantidad("agua", 2.0)

# Ver estadísticas
stats = servicios.obtener_estadisticas_rapidas()
print(f"Total: {stats['total_habitos']}")
print(f"Activos: {stats['habitos_activos']}")
print(f"Checks completados: {stats['checks_completados']}/{stats['checks_totales']}")

# Obtener resumen
print(servicios.obtener_resumen_completo())

# Guardar
repo.guardar()
```

### 📊 Estadísticas Rápidas
```python
{
    "total_habitos": 5,
    "habitos_activos": 4,
    "habitos_pausados": 1,
    "checks_totales": 3,
    "checks_completados": 2,
    "cantidades_totales": 2,
    "cantidades_cumplidas": 1
}
```

---

## 🎯 Flujo Completo de Uso

```
1. Inicializar
   ├── repo = RepositorioHabito("datos/habitos.json")
   ├── repo.cargar()  # Cargar hábitos previos
   └── servicios = ServiciosHabitos(repo)

2. Crear hábitos
   ├── servicios.crear_habito_check("h1", "Meditar", "diario")
   └── servicios.crear_habito_cantidad("h2", "Agua", "diario", objetivo=2.0)

3. Usar hábitos
   ├── servicios.marcar_completado("h1")
   ├── servicios.agregar_cantidad("h2", 1.5)
   └── servicios.agregar_cantidad("h2", 0.5)

4. Obtener información
   ├── stats = servicios.obtener_estadisticas_rapidas()
   ├── resumen = servicios.obtener_resumen_completo()
   └── activos = servicios.obtener_activos()

5. Notificar
   ├── gestor = GestorNotificadores()
   ├── gestor.registrar_notificador(NotificadorConsola())
   └── gestor.notificar_a_todos("Recordatorio", "¡Completa tu hábito!")

6. Guardar
   └── repo.guardar()
```

---

## 📝 Notas Importantes

- ✅ Todas las clases tienen docstrings completos
- ✅ Todos los métodos tienen type hints
- ✅ Las excepciones son específicas y útiles
- ✅ El código sigue principios SOLID
- ✅ La persistencia es automática
- ✅ Las validaciones son robustas

---

**¡Listo para usar! 🚀**

