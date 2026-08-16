import os 
from _calculator import print_calculator_banner

def addtion(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: Both inputs must be numbers."
    return a + b

def subtraction(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: Both inputs must be numbers."
    return a - b

def multiplication(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: Both inputs must be numbers."
    return a * b

def division(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: Both inputs must be numbers."
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def calculator(num1, num2, operation):
    if operation == "+":
        return addtion(num1, num2)
    elif operation == "-":
        return subtraction(num1, num2)
    elif operation == "*":
        return multiplication(num1, num2)
    elif operation == "/":
        return division(num1, num2)
         
    else:
        return "Invalid operation. Please choose +, -, *, or /."


def main(): 
    num1 = None
    while True:
        try:
            if num1 is None:
                num1 = float(input("Enter the first number: "))
            operation = input("Enter the operation (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))
            result = calculator(num1, num2, operation)
            print(f"{num1} {operation} {num2} = {result}")
            cont = input(f"Do you want to continue making calculations with {result}? (yes/no): ")
            if cont.strip().lower() in ["no", "n"]:
                os.system('cls || clear')
                num1 = None
                print("Starting a new calculation.")
            else:
                if isinstance(result, (int, float)):
                    num1 = result
                else: 
                    print("Cannot continue with the result of an invalid operation. Starting a new calculation.")
                    num1 = None

        except ValueError:
            print("Invalid input. Please enter numeric values for the numbers.")

if __name__ == "__main__":
    print_calculator_banner()
    print("Welcome to the calculator program.")
    main()