# Sistema de Gestión de Hábitos

Aplicación de consola para gestionar hábitos, rutinas y valoraciones, con separación por capas (`Entidades`, `Servicios`, `Persistencia`, `UI`) y uso de Programación Orientada a Objetos.

---

# Objetivo del proyecto

Este proyecto implementa un sistema académico de gestión de hábitos y bienestar con foco en:

- modelado orientado a objetos y encapsulación
- uso de herencia mediante la clase abstracta `Habito` y sus variantes
- polimorfismo en métodos como `cumplido()` y `notificar()`
- separación de responsabilidades mediante arquitectura en 4 capas
- validación de datos y gestión de excepciones propias
- uso de repositorios para gestionar los datos de la aplicación
- interacción con el usuario mediante una interfaz de consola

El proyecto se basa en la propuesta 21, **Hábitos y bienestar**, cuyo objetivo es realizar un seguimiento de rutinas, metas y tipos de hábitos con reglas diferenciadas.

---

# Requisitos

- Python 3.12 o superior
- Entorno virtual recomendado

---

# Instalación rápida

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
```

Si existe el archivo `requirements.txt`, se pueden instalar las dependencias con:

```bash
python -m pip install -r requirements.txt
```

---

# Cómo ejecutar la aplicación

```bash
python main.py
```

`main.py` construye los repositorios, servicios y lanza la interfaz de consola definida en `UI/PantallaHabitos.py`.

---

# Estructura del proyecto

```text
trabajo-final-b6/
│
├── Entidades/
│   ├── Habito.py
│   ├── HabitoCheck.py
│   ├── HabitoCantidad.py
│   ├── Rutina.py
│   ├── ReviewHabito.py
│   └── Notificable.py
│
├── Persistencia/
│   ├── RepositorioHabito.py
│   └── RepositorioReviewHabito.py
│
├── Servicios/
│   ├── ServiciosHabitos.py
│   └── ServiciosReviewHabito.py
│
├── UI/
│   └── PantallaHabitos.py
│
├── main.py
├── README.md
└── requirements.txt
```

---

# Responsabilidades por capa

Regla arquitectónica principal:

```text
UI -> Servicios -> Persistencia / Entidades
```

## Entidades

Contienen las clases principales del dominio:

- hábitos
- rutinas
- reviews
- validaciones internas
- herencia
- polimorfismo
- encapsulación

## Servicios

Actúan como intermediarios entre la interfaz y los datos. Incluyen la lógica de aplicación para:

- crear hábitos
- listar hábitos
- eliminar hábitos
- gestionar reviews
- calcular información derivada

## Persistencia

Contiene los repositorios encargados de almacenar y recuperar los objetos de la aplicación.

Actualmente, se utilizan repositorios en memoria, dejando la estructura preparada para añadir persistencia en ficheros.

## UI

Contiene la interfaz de consola. Su responsabilidad es pedir datos al usuario, mostrar mensajes y llamar a los servicios correspondientes.

---

# Funcionalidades

La aplicación permite:

- crear hábitos de tipo check
- crear hábitos de tipo cantidad
- consultar todos los hábitos registrados
- eliminar hábitos
- crear rutinas y agrupar hábitos
- añadir reviews a los hábitos
- consultar las reviews almacenadas
- activar y pausar hábitos
- comprobar el cumplimiento de un hábito

---

# Reglas de dominio principales

- `Habito` es una clase abstracta que define la estructura común de todos los hábitos.
- `HabitoCheck` representa hábitos que se cumplen o no se cumplen.
- `HabitoCantidad` representa hábitos con un objetivo numérico.
- `Rutina` permite agrupar varios hábitos.
- `Review` permite valorar un hábito con fecha, nota y comentario.
- La importancia de un hábito debe estar entre 1 y 5.
- La frecuencia solo puede ser `diario`, `semanal` o `mensual`.
- La nota de una review debe estar entre 0 y 10.
- No se permiten nombres, fechas o comentarios vacíos.

---

# Conceptos de Programación Orientada a Objetos utilizados

## Clases y objetos

El sistema se organiza mediante clases como `Habito`, `HabitoCheck`, `HabitoCantidad`, `Rutina` y `Review`.

## Encapsulación

Se usan atributos protegidos y privados para controlar el acceso a los datos:

```text
_identificador
_activo
__comentario
```

## Herencia

`HabitoCheck` y `HabitoCantidad` heredan de `Habito`.

```text
Habito
├── HabitoCheck
└── HabitoCantidad
```

## Polimorfismo

Cada tipo de hábito puede implementar el método `cumplido()` según sus propias reglas.

## Clases abstractas

La clase `Habito` utiliza `ABC` y `@abstractmethod` para obligar a las clases hijas a implementar ciertos métodos.

## Sobrecarga de operadores

Se utiliza sobrecarga para comparar hábitos, por ejemplo mediante `__lt__`, comparando su importancia.

---

# Gestión de excepciones

El proyecto incluye validaciones y excepciones para controlar errores como:

- importancia fuera de rango
- frecuencia inválida
- nombre vacío
- nota inválida
- comentario vacío
- fecha inválida
- tipo de dato incorrecto

Esto evita que se creen objetos con estados incoherentes.

---

# Ejemplo rápido de uso

```python
from Entidades.HabitoCheck import HabitoCheck

habito = HabitoCheck(
    identificador=1,
    nombre="Hacer ejercicio",
    frecuencia="diario",
    importancia=5
)

print(habito)
```

---

# Ejemplo de review

```python
from Entidades.HabitoCheck import HabitoCheck
from Entidades.ReviewHabito import Review

habito = HabitoCheck(
    identificador=1,
    nombre="Hacer ejercicio",
    frecuencia="diario",
    importancia=5
)

review = Review(
    fecha="2026-05-15",
    nota=9,
    comentario="Buen progreso durante la semana",
    habito=habito
)

habito.poner_review(review)
```

---

# Notas

- El código está organizado siguiendo una arquitectura por capas.
- Las entidades contienen las reglas principales del dominio.
- Los servicios coordinan las operaciones de la aplicación.
- La UI se limita a interactuar con el usuario.
- El proyecto aplica conceptos vistos en Programación II: clases, objetos, herencia, encapsulación, polimorfismo, clases abstractas, excepciones y sobrecarga de operadores.

---

# Diagrama UML de clases (Mermaid)

```mermaid
classDiagram
direction LR

class Habito {
  <<abstract>>
  +total_habitos
  -int _identificador
  -str _nombre
  -str _frecuencia
  -bool _activo
  -int _importancia
  -list~str~ _fecha
  -list~Review~ _reviews
  +identificador int
  +nombre str
  +frecuencia str
  +activo bool
  +importancia int
  +poner_review(review) void
  +activar() void
  +pausar() void
  +total() int
  +cumplido()* bool
  +__lt__(other) bool
}

class HabitoCheck {
  -bool _completado
  +completado bool
  +marcar_completado() void
  +reiniciar() void
  +cumplido() bool
  +notificar() void
}

class HabitoCantidad {
  -int _objetivo
  -int _cantidad_actual
  +objetivo int
  +cantidad_actual int
  +agregar_cantidad(cantidad) void
  +reiniciar() void
  +cumplido() bool
  +notificar() void
}

class Notificable {
  +notificar(mensaje, cumplido) void
  +mensaje_alerta() str
}

class Review {
  -str _fecha
  -int _nota
  -str __comentario
  -Habito _habito
  +comentario str
  +nota int
  +fecha str
  +habito Habito
}

class Rutina {
  -str _nombre
  -list~Habito~ _habitos
  +nombre str
  +habitos list~Habito~
  +agregar_habito(habito) void
  +resumen() void
}

class RepositorioHabito {
  +ARCHIVO
  -dict~int, Habito~ _habitos
  -_cargar() void
  -_guardar() void
  +agregar(habito) void
  +eliminar(identificador) bool
  +obtener(identificador) Habito
  +obtener_todos() list~Habito~
}

class RepositorioReviewHabito {
  +ARCHIVO
  -list~Review~ _reviews
  -_cargar() void
  -_guardar() void
  +anadir_review(review) void
  +mostrar_reviews() list~Review~
  +eliminar_review(review) void
  +total_reviews() int
}

class ServiciosHabitos {
  -RepositorioHabito _repositorio
  +agregar_habito(habito) void
  +eliminar_habito(identificador) bool
  +listar_todos() list~Habito~
  +listar_cumplidos() list~Habito~
  +resumen() tuple
}

class ServiciosReviewHabito {
  -RepositorioReviewHabito _repositorio
  +anadir_review(review) void
  +mostrar_reviews() list~Review~
  +nota_media_reviews() float
  +buscar_review(fecha) list~Review~
  +review_por_nota(nota) list~Review~
}

class PantallaHabitos {
  -RepositorioHabito _repo
  -ServiciosHabitos _servicios
  -list~Rutina~ _rutinas
  -RepositorioReviewHabito _repo_review
  -ServiciosReviewHabito _servicios_review
  +iniciar() void
  +crear_habito() void
  +ver_habitos() void
  +eliminar_habito() void
  +crear_rutina() void
  +habito_a_rutina() void
  +ver_rutinas() void
  +agregar_review() void
  +ver_reviews() void
}

Habito <|-- HabitoCheck
Habito <|-- HabitoCantidad
Notificable <|.. HabitoCheck
Habito "1" o-- "0..*" Review : reviews
Review --> Habito : valora
Rutina "1" o-- "0..*" Habito : contiene
RepositorioHabito "1" o-- "0..*" Habito : almacena
RepositorioReviewHabito "1" o-- "0..*" Review : almacena
ServiciosHabitos --> RepositorioHabito : usa
ServiciosReviewHabito --> RepositorioReviewHabito : usa
PantallaHabitos --> ServiciosHabitos : usa
PantallaHabitos --> ServiciosReviewHabito : usa
PantallaHabitos --> RepositorioHabito : usa
PantallaHabitos --> RepositorioReviewHabito : usa
PantallaHabitos "1" o-- "0..*" Rutina : gestiona
```

---

# Diagrama de arquitectura C4 (Mermaid)

# Diagrama C4 — Nivel 1 (Contexto)

```mermaid
flowchart LR

    Usuario["Usuario"]

    Sistema["Sistema de Gestión de Hábitos"]

    Habitos[("habitos.json")]
    Reviews[("reviews.json")]

    Usuario -->|"Gestiona hábitos y rutinas"| Sistema

    Sistema -->|"Lee y escribe hábitos"| Habitos
    Sistema -->|"Lee y escribe reviews"| Reviews
```

---

# Diagrama C4 — Nivel 2 (Contenedores)

```mermaid
flowchart TB

    Usuario["Usuario"]

    subgraph Sistema["Sistema de Gestión de Hábitos"]

        Pantalla["PantallaHabitos<br>Interfaz de consola"]

        ServiciosHabitos["ServiciosHabitos<br>Lógica de hábitos"]

        ServiciosReviews["ServiciosReviewHabito<br>Lógica de reviews"]

        RepoHabitos["RepositorioHabito<br>Persistencia hábitos"]

        RepoReviews["RepositorioReviewHabito<br>Persistencia reviews"]

        Modelos["Modelos de Dominio<br>Habito<br>HabitoCheck<br>HabitoCantidad<br>Rutina<br>Review"]

    end

    Habitos[("habitos.json")]
    Reviews[("reviews.json")]

    Usuario --> Pantalla

    Pantalla --> ServiciosHabitos
    Pantalla --> ServiciosReviews

    ServiciosHabitos --> RepoHabitos
    ServiciosReviews --> RepoReviews

    ServiciosHabitos --> Modelos
    ServiciosReviews --> Modelos

    RepoHabitos --> Habitos
    RepoReviews --> Reviews
```