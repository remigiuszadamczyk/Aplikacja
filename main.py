def menu():
    while(True):
        
        list_of_tools = ["Calculator", "NWD"]

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
        return(redirect(choice))

def redirect(choice):

    if choice == 1:
        from tools.calculator import calculator
        calculator()
    elif choice == 2:
        from tools.nwd import nwd
        nwd()

menu()