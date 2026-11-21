def calculator():
    a = int(input("Enter the first number: "))
    b = str(input("Enter the operation: "))
    c = int(input("Enter the second number: "))

    if b == "+":
        result = a + c
    elif b == "-":
        result = a - c
    elif b == "*":
        result = a * c
    elif b == "/":
        result = a / c
        
    print(f"Result: {result}")