lista_narzędzi = ["Kalkulator"]

print("""
███████████████████████████████████
██                               ██
██           Narzędzia           ██
██                               ██
███████████████████████████████████
""")
for i in range(1, len(lista_narzędzi) + 1):
    print(f"{i}. {lista_narzędzi[i-1]}")

a = int(input("Wybierz z listy narzędzie: "))

def kalkukator(dzialanie):
    str(dzialanie)
    a = int(dzialanie[0])
    b = str(dzialanie[2])
    c = int(dzialanie[4])
    if b == "+":
        return a + c
    elif b == "-":
        return a - c
    elif b == "*":
        return a * c
    elif b == "/":
        return a / c

if a == 1:
    dzialanie = input("Podaj działanie do wykonania (2 + 2): ")
    print(f"Wynik: {kalkukator(dzialanie)}")