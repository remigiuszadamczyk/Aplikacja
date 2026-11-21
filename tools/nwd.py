def nwd():

    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    while b != 0:
        a, b = b, a % b

    print(f"Result: {a}")