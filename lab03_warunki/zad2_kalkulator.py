# Lab 03 – Zadanie 2 (★): Kalkulator z wyborem działania
#
# Program wczytuje kolejno: liczbę, operator (+, -, *, /) i drugą liczbę,
# a potem wypisuje wynik, np.:  8.0 * 2.0 = 16.0
#
# Obsłuż przypadki szczególne instrukcją if:
#   - dzielenie przez zero  -> "Nie można dzielić przez zero"
#   - inny operator         -> "Nieznany operator"

# TODO: Twój kod poniżej
pierwsz = int(input("Podaj swoja pierwsza liczbe:"))
oper = input("Podaj operator do swojego dzialania: ")
druga = int(input("Podaj swoja druga liczbe: "))
if oper == "+":
    suma = pierwsz + druga
    print(f"Suma twoich liczb to {suma}")
elif oper == "-":
    odej = pierwsz - druga
    print(f"Wynik po odjeciu: {odej}")
elif oper == "*":
    mnoz = pierwsz * druga
    print(f"Wynik po mnozeniu: {mnoz}")
elif oper == "/" and druga != 0:
    dziel = pierwsz / druga
    print(f"Wynik dzielenia : {dziel}")
else:
    print("Nieznany operator")
