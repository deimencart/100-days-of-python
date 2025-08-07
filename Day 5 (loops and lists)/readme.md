# PyPassword Generator 🔐

Este proyecto es un generador simple de contraseñas aleatorias escrito en Python. Permite al usuario especificar la cantidad de letras, números y símbolos que desea en su contraseña final.

## 🚀 ¿Cómo funciona?

1. Se le pregunta al usuario cuántas **letras**, **números** y **símbolos** quiere en su contraseña.
2. El programa elige aleatoriamente los caracteres desde listas predeterminadas.
3. Combina todos los caracteres en una lista.
4. Mezcla el orden de los caracteres para mayor seguridad.
5. Convierte la lista en un solo string y lo imprime como la contraseña generada.

## 📦 Ejemplo de uso

```bash
$ python password_generator.py
Welcome to the PyPassword Generator!
How many letters would you like in your password?
> 4
How many symbols would you like?
> 2
How many numbers would you like?
> 3
rG@1a3+B9
```

## 🧠 Características

- Totalmente aleatorio.
- Longitud configurable.
- Mezcla caracteres de distintos tipos (letras, números, símbolos).
- Código simple, ideal para principiantes.

## 🛠 Requisitos

- Python 3
- No se requieren librerías externas.
