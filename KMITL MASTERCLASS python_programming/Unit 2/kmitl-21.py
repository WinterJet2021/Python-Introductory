# CALCULATOR WITH INPUT PROBLEM

def calculator():
    a = 4
    b = 3

    print("Please choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        result = a + b
        operation = "addition"
    elif choice == '2':
        result = a - b
        operation = "subtraction"
    elif choice == '3':
        result = a * b
        operation = "multiplication"
    elif choice == '4':
        if b != 0:
            result = a / b
            operation = "division"
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid input")
        return

    print(f"The result of the {operation} of {a} and {b} is: {result}")

calculator()

# COURTESY OF CHAT GPT