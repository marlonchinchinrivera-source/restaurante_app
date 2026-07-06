# Sistema Restaurante App - POO Modulada

**Estudiante:** [Escribe aquí tu Nombre Completo]  
**Asignatura:** Programación Orientada a Objetos  
**Institución:** Universidad Estatal Amazónica (UEA)

## Descripción del Sistema
Este sistema simula la administración de un menú gastronómico en un restaurante mediante consolas modulares de Python independientes, aplicando los tres pilares fundamentales de la POO: herencia, encapsulación y polimorfismo.

## Estructura del Proyecto
El software está distribuido de forma modular bajo la siguiente estructura de carpetas:
* `modelos/`: Contiene la definición y lógica de datos de los objetos (`Producto`, `Platillo`, `Bebida`).
* `servicios/`: Contiene la clase `Restaurante` que administra las listas del menú.
* `main.py`: Archivo principal y punto de arranque del programa.

## Principios de POO Aplicados

### 1. Herencia
Las clases hijas `Platillo` y `Bebida` heredan las propiedades base (nombre, precio, disponibilidad) de la clase padre `Producto` utilizando la función `super()`.

### 2. Encapsulación
El atributo de costo se ha declarado privado (`self.__precio`) dentro de la clase `Producto`. Su acceso y modificación externa están restringidos y controlados mediante métodos públicos Getters y Setters que impiden la asignación de valores negativos o iguales a cero.

### 3. Polimorfismo
El método `mostrar_informacion()` fue sobrescrito de manera personalizada en las clases hijas. Al ejecutar el menú desde el servicio, el sistema recorre la lista unificada y muestra detalles específicos dependiendo de si el objeto es un platillo (calorías/tiempo) o una bebida (mililitros).

## Reflexión sobre la Modularidad en POO
Dividir un proyecto en módulos independientes en Python permite una arquitectura mucho más limpia, ordenada y fácil de mantener. Facilita el trabajo en equipo, evita la duplicación de código y permite escalar la aplicación de forma ágil sin afectar los componentes que ya funcionan correctamente.