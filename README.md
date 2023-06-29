# POO
Ejemplo de programación Orientada a Objetos. unas personas se ponen a jugar la ruleta rusa.


En este ejemplo, se está aplicando el concepto de programación orientada a objetos (POO) utilizando las siguientes características:

1. Clases: Se definen las clases `Moneda`, `Pistola`, `Persona` y `Arbitro`, que son objetos con propiedades y comportamientos relacionados.

2. Objetos: Se crean instancias de las clases `Moneda`, `Pistola`, `Persona` y `Arbitro` mediante la creación de objetos como `juan`, `pepe` y `arbitro`.

3. Atributos: Las clases tienen atributos que definen sus propiedades. Por ejemplo, la clase `Pistola` tiene el atributo `recamara` para almacenar las balas en la recámara.

4. Métodos: Las clases tienen métodos que definen su comportamiento. Por ejemplo, la clase `Pistola` tiene métodos como `recargar`, `girar_recamara`, `disparar`, `obtener_numero_tiros_restantes`, entre otros.

5. Constructor: Las clases `Pistola` y `Persona` tienen un método `__init__`, que se utiliza como constructor para inicializar los objetos cuando se crean instancias de esas clases.

6. Composición: La clase `Persona` tiene un atributo `pistola` que es un objeto de la clase `Pistola`. Esto muestra una relación de composición, donde una persona tiene una pistola.

7. Encapsulación: Los métodos y atributos están encapsulados dentro de las clases. Por ejemplo, los métodos `recargar_pistola`, `lanzar_volado` y `tomar_decision_disparo` de la clase `Persona` solo pueden ser accedidos a través de un objeto de esa clase.

8. Interacción entre objetos: Los objetos interactúan entre sí a través de llamadas a métodos. Por ejemplo, el árbitro llama al método `recargar_pistola` de la clase `Persona` para recargar las pistolas de los jugadores.

En resumen en este ejemplo en particular, se están aplicando conceptos fundamentales de la programación orientada a objetos como clases, objetos, atributos, métodos, encapsulación y composición.
