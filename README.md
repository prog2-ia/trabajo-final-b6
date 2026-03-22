# Sistema de Gestión de Hábitos

## Descripción

El proyecto está dividido en 4 capas para separar responsabilidades y hacer el código más claro y organizado.

---

## Estructura del Proyecto

```
id="8w1m4o"
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


* **Entidades**: contienen las clases principales del sistema (hábitos, rutinas y reviews).
* **Persistencia**: se encarga de almacenar los datos en memoria mediante repositorios.
* **Servicios**: incluye la lógica de negocio, actuando como intermediario entre la UI y los datos.
* **UI**: menú interactivo que permite al usuario utilizar la aplicación desde consola.

---

## Funcionalidades

* Crear hábitos de tipo check (completado o no) o de cantidad (con objetivo).
* Consultar todos los hábitos y eliminarlos si es necesario.
* Crear rutinas y agrupar hábitos dentro de ellas.
* Añadir reviews a los hábitos para valorar su progreso.
* Consultar las reviews almacenadas en el sistema.

---
 
## Ejecución
Para ejecutar el programa desde la terminal:
```bash
python main.py
```
Se mostrará un menú en consola desde el que se pueden usar todas las funcionalidades.

---
 
## Notas
* Se ha utilizado programación orientada a objetos para modelar el problema.
* Se aplican conceptos como herencia, encapsulación y clases abstractas.
* El código está organizado en capas para mejorar su mantenimiento.
* Se incluyen validaciones básicas para evitar errores en la entrada de datos.
 
---
 
## Estado
Primera versión funcional del proyecto, con todas las funcionalidades principales implementadas.
