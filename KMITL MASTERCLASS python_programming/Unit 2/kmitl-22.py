def discount():
    N = 500
    P = 1000

    cashier = int(input("Total price: "))

    if cashier == N:
        result = N * 0.90
        operation = "off 10%"
    elif cashier == P:
        result = P * 0.80
        operation = "off 20%"
    else:
        print("Invalid input. Please enter either 500 or 1000.")
        return

    print(f"The result of the {operation} of {cashier} is: {result}")

discount()
