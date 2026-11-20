def start_menu():
    list_of_tools = ["Calculator"]

    print("""
    ███████████████████████████████████
    ██                               ██
    ██             Tools             ██
    ██                               ██
    ███████████████████████████████████
    """)
    for i in range(1, len(list_of_tools) + 1):
        print(f"{i}. {list_of_tools[i-1]}")
        choice = int(input("Select a tool: "))

        return choice

def calculator_menu(choice):
    if choice == 1:
        from tools import Calculator

        a = int(input("Enter the first number: "))
        b = str(input("Enter the operation: "))
        c = int(input("Enter the second number: "))

        print(f"Result: {Calculator(a, b, c)}")
    
    