# Entrega: Patrones de Diseño y OOP 

Repositorio desarrollado para demostrar el dominio de la Programación Orientada a Objetos mediante la implementación de los patrones del Gang of Four. 

## Reflexión Teórica
En teoría, la Programación Orientada a Objetos permite estructurar el código de manera modular mediante clases y el uso del encapsulamiento. Sin embargo, al escalar los proyectos, las interdependencias aumentan y la mantenibilidad se ve comprometida.

Para resolver esto se aplican los **Patrones de Diseño**, que fungen como plantillas probadas para problemas arquitectónicos recurrentes. Su implementación favorece el desacoplamiento, respeta los principios SOLID (como Responsabilidad Única y Abierto/Cerrado) e incrementa sustancialmente la reusabilidad del código sin tener que refactorizar todo el sistema ante nuevos requerimientos.

---

## Explicación técnica de 5 patrones seleccionados

Aunque se anexaron ejemplos complementarios de los 23 patrones dentro del repositorio, a continuación se expone la justificación técnica de 5 patrones principales elegidos para esta evaluación:

### 1. Singleton (Carpeta creacionales)
* **Propósito:** Restringir la instanciación de una clase a un único objeto en todo el programa, creando un punto de acceso global.
* **Implementación:** En nuestro archivo `RegistroUnico`, se sobrescribe el método `__new__` nativo de Python para que actúe como un control de flujo. Si hay una instancia en memoria, se retorna la referencia preexistente en lugar de inicializar un bloque nuevo.

### 2. Factory Method (Carpeta creacionales)
* **Propósito:** Delegar el proceso de instanciación hacia las subclases mediante una interfaz creadora común.
* **Implementación:** En lugar de acoplar condicionales (`if-else`) en el código principal para crear diferentes tipos de notificaciones (Email, SMS), se invoca a una Interfaz Fábrica. El código principal ignora los detalles internos y solo procesa el método abstracto `.enviar()`.

### 3. Decorator (Carpeta estructurales)
* **Propósito:** Añadir funcionalidades dinámicas a un objeto en tiempo de ejecución, evitando la explosión de herencias rígidas.
* **Implementación:** Comenzando con un componente esencial como `CafeSolo`, la funcionalidad le permite "envolverse" iterativamente en decoradores secuenciales (extra leche, extra azúcar). Los atributos mutan en tiempo de ejecución sin haber programado múltiples subclases estáticas.

### 4. Observer (Carpeta comportamiento)
* **Propósito:** Definir una dependencia proactiva uno-a-muchos, en la que un publicador notifica automáticamente a los suscriptores suscritos.
* **Implementación:** En un sistema tipo YouTube, el núcleo guardará un array indexado de los espectadores conectados. Al desencadenar el evento de subir video, el publicador itera internamente la lista para emitir alertas sin sobrecargar la RAM ni hacer requests repetitivos ("polling").

### 5. Strategy (Carpeta comportamiento)
* **Propósito:** Encapsular una familia de algoritmos de manera que sean totalmente intercambiables desde el lado del cliente sin editar la clase receptora.
* **Implementación:** Dentro del sistema de un GPS virtual, la lógica pesada del viaje (Caminar, Conducir, Bici) se consolida en clases de "Estrategia" separadas. El programa principal las asume por parámetro polimórfico, cambiando el comportamiento base en caliente.
