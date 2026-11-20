from menu import start_menu
from menu import calculator_menu
from menu import nwd_menu

choice = start_menu()
if choice == 1:
    calculator_menu()
elif choice == 2:
    nwd_menu()