# Lab 03 – Zadanie 5 (☆, dodatkowe): Jaki to trójkąt?
#
# Program wczytuje trzy długości boków (float) i wypisuje:
#   - "Nie da się zbudować trójkąta", jeśli nie spełniają nierówności trójkąta
#     (każdy bok musi być krótszy od sumy dwóch pozostałych),
#   - w przeciwnym razie rodzaj: "równoboczny", "równoramienny" albo "różnoboczny",
#   - dodatkowo "prostokątny", jeśli a² + b² = c² dla najdłuższego boku c
#     (porównuj z tolerancją: abs(x - y) < 1e-9).

# TODO: Twój kod poniżej
a = float(input("Podaj swoj pierwszy bok"))
b = float(input("Podaj swoj drugi bok"))
c = float(input("Podaj swoj trzeci bok"))
if a + b > c and a + c > b and c + b > a:
    if a == b == c:
        print("Trojkat rownoboczny")
    elif a == b or a == c or b == c:
        print("Trojkat rownoramienny")
    elif a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
        print("Trojkat prostokatny")
        