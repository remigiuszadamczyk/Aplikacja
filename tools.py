def Calculator(a,b,c):
    if b == "+" or b == "-" or b == "*" or b == "/":
        if b == "+":
            return a + c
        elif b == "-":
            return a - c
        elif b == "*":
            return a * c
        elif b == "/":
            return a / c
    else: 
        print("Invalid operation. Please use +, -, *, or /.")