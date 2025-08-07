import random  # Importa la librería para generar valores aleatorios

# Listas de caracteres posibles
letters = ['a', 'b', ..., 'Z']
numbers = ['0', '1', ..., '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Solicita al usuario la cantidad de caracteres de cada tipo
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Lista vacía donde se construirá la contraseña
password = []

# Añade letras aleatorias
for _ in range(nr_letters):
    password.append(random.choice(letters))

# Añade números aleatorios
for _ in range(nr_numbers):
    password.append(random.choice(numbers))

# Añade símbolos aleatorios
for _ in range(nr_symbols):
    password.append(random.choice(symbols))

# Mezcla el orden de los caracteres en la lista
random.shuffle(password)

# Convierte la lista de caracteres en un string
password = "".join(password)

# Imprime la contraseña generada
print(password)
