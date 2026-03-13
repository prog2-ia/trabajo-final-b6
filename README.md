# Sistema de Gestión de Hábitos

## Descripción

Un sistema completo de gestión de hábitos desarrollado en Python que permite crear, monitorear y analizar hábitos personales. Implementa principios de Programación Orientada a Objetos (POO) con clases abstractas, herencia, polimorfismo y encapsulamiento.

## Características

- ✅ **Gestión de Hábitos Binarios**: Hábitos que se marcan como completados o no (ej. meditar, hacer ejercicio).
- ✅ **Gestión de Hábitos Medibles**: Hábitos con objetivos cuantitativos (ej. beber 2L de agua, leer 30 páginas).
- ✅ **Persistencia de Datos**: Almacenamiento en archivos JSON.
- ✅ **Estadísticas y Análisis**: Cálculo de rachas, porcentajes de cumplimiento y tendencias.
- ✅ **Sistema de Notificaciones**: Soporte para notificaciones por consola, email y SMS.
- ✅ **Validación de Datos**: Validación centralizada con excepciones personalizadas.
- ✅ **Interfaz de Usuario**: Interfaz de consola para interactuar con el sistema.



## Ejemplo de Código
```python
from entidades.HabitoCheck import HabitoCheck
from entidades.HabitoCantidad import HabitoCantidad

# Crear un hábito binario
habito_check = HabitoCheck("med1", "Meditar", "diario")
habito_check.marcar_completado()
print(habito_check.cumplido())  # True

# Crear un hábito medible
habito_cantidad = HabitoCantidad("agua1", "Beber agua", "diario", objetivo=2.0)
habito_cantidad.agregar_cantidad(1.5)
print(habito_cantidad.cumplido())  # False
habito_cantidad.agregar_cantidad(0.5)
print(habito_cantidad.cumplido())  # True
```

## Estructura del Proyecto

```
trabajo-final-b6/
├── entidades/
│   ├── Hábito.py              # Clase abstracta base para hábitos
│   ├── HabitoCheck.py         # Hábito binario
│   ├── HabitoCantidad.py      # Hábito medible
│   └── rutina.py              # Definición de rutinas
├── persistencia/
│   └── RepositorioHabito.py   # Almacena hábitos en memoria
├── servicios/
│   └── ServiciosHabitos.py    # Operaciones sobre la lista de hábitos del repositorio.
├── ui/
│   └── PantallaHabitos.py     # Interfaz de usuario
├── main.py                    # Punto de entrada principal
└── README.md                  # Documentación original
```

