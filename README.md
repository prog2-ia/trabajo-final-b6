# Sistema de Gestión de Hábitos

## Descripción

Un sistema completo de gestión de hábitos desarrollado en Python que permite crear, monitorear y analizar hábitos personales. Implementa principios de Programación Orientada a Objetos (POO) con clases abstractas, herencia, polimorfismo y encapsulamiento.

## Características

-  **Gestión de Hábitos Binarios**: Hábitos que se marcan como completados o no (ej. meditar, hacer ejercicio).
-  **Gestión de Hábitos Medibles**: Hábitos con objetivos cuantitativos (ej. beber 2L de agua, leer 30 páginas).
-  **Estadísticas y Análisis**: Cálculo de rachas, porcentajes de cumplimiento y tendencias.
-  **Sistema de Notificaciones**: Soporte para notificaciones por consola, email y SMS.
-  **Validación de Datos**: Validación centralizada con excepciones personalizadas.
-  **Interfaz de Usuario**: Interfaz de consola para interactuar con el sistema.


## Funcionalidades
 
- Crear hábitos de tipo **Check** (sí/no) o **Cantidad** (con objetivo numérico)
- Asignar un nivel de **importancia** del 1 al 5 a cada hábito
- Ver todos los hábitos ordenados por importancia
- Eliminar hábitos
- Agrupar hábitos en **rutinas**
- Añadir **reviews** con fecha, nota y comentario a un hábito

## Estructura del Proyecto

```
trabajo-final-b6/
├── Entidades/
│   ├── Hábito.py            # Clase abstracta base
│   ├── HabitoCheck.py       # Hábito de tipo sí/no
│   ├── HabitoCantidad.py    # Hábito con objetivo numérico
│   ├── ReviewHabito.py      # Reseña asociada a un hábito
│   └── Rutina.py            # Agrupación de hábitos
├── Persistencia/
│   ├── RepositorioHabito.py       # Almacena hábitos en memoria
│   └── RepositorioReviewHabito.py # Almacena reviews en memoria
├── Servicios/
│   ├── ServiciosHabitos.py        # Lógica sobre hábitos
│   └── ServiciosReviewHabito.py   # Lógica sobre reviews
├── UI/
│   └── PantallaHabitos.py   # Interfaz de consola
├── main.py                  # Punto de entrada
├── requirements.txt
└── README.md

```

