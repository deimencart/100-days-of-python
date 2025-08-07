
# Piedra, Papel o Tijeras (Rock, Paper, Scissors)

Este es un sencillo juego de consola en Python basado en el clásico juego "Piedra, Papel o Tijeras" entre un usuario y la computadora.

## ¿Cómo funciona?

1. El usuario debe ingresar un número:
   - `0` para Piedra (Rock)
   - `1` para Papel (Paper)
   - `2` para Tijeras (Scissors)

2. La computadora elige aleatoriamente una opción usando `random.randint(0, 2)`.

3. Se comparan ambas elecciones y se imprime un resultado:
   - **Empate** si ambos eligen lo mismo.
   - **Gana el usuario** si su elección vence a la de la computadora.
   - **Gana la computadora** en cualquier otro caso.

4. También se imprime una representación visual de cada jugada en arte ASCII.

## Requisitos

- Python 3.x
- No se necesitan librerías externas.

## Ejemplo de ejecución
Please insert a number to select the following -> Rock = 0, Paper = 1, Scissors = 2: 1
User option:
_______
---' )
_____)
_____)
)
---.)

Computer option:
_______
---' )
()
()
()
---.(_)
## Mejoras posibles

- Agregar validación para entradas no numéricas.
- Permitir jugar múltiples rondas.
- Llevar un marcador de puntos (usuario vs PC).
