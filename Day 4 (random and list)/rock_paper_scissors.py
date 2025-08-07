import random

# Representaciones gráficas de las opciones
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Lista de opciones para acceder fácilmente por índice
options = [rock, paper, scissors]

# La computadora elige una opción al azar (0 = rock, 1 = paper, 2 = scissors)
pc_option = random.randint(0, 2)

# El usuario ingresa su elección (espera un número entre 0 y 2)
usr_option = int(input("Please insert a number to select the following -> Rock = 0, Paper = 1, Scissors = 2: "))

# Muestra los valores numéricos elegidos (útil para depuración)
print("PC option = " + str(pc_option) + " USR = " + str(usr_option))

# Validación del input del usuario
if usr_option > 2 or usr_option < 0:
    print("Is not a valid option")
else:
    # Muestra visualmente la elección del usuario y la computadora
    print("User option:")
    print(options[usr_option])
    print("Computer option:")
    print(options[pc_option])

    # Comparación de resultados
    if usr_option == pc_option:
        print("Tie")
    elif usr_option == 2 and pc_option == 1:
        print("User Wins")
    elif usr_option == 1 and pc_option == 0:
        print("User Wins")
    elif usr_option == 0 and pc_option == 2:
        print("User Wins")
    else:
        print("PC Wins")
