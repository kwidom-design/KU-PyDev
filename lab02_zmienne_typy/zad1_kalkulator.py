# Lab 02 – Zadanie 1 (★): Kalkulator konsolowy
#
# Program wczytuje dwie liczby (float) i wypisuje wynik WSZYSTKICH działań,
# każde w osobnej linii, np. dla 7 i 2:
#     7.0 + 2.0 = 9.0
#     7.0 - 2.0 = 5.0
#     7.0 * 2.0 = 14.0
#     7.0 / 2.0 = 3.5
#     7.0 // 2.0 = 3.0     (dzielenie całkowite)
#     7.0 % 2.0 = 1.0      (reszta z dzielenia)
#     7.0 ** 2.0 = 49.0    (potęgowanie)
#
# Załóż, że druga liczba nie jest zerem (obsługę zera dodasz w labie 03).

# TODO: Twój kod poniżej
liczba_1 = float(input("Podaj pierwszą liczbe : "))
liczba_2 = float(input("Podaj drugą liczbe : "))
if liczba_2 != 0:
    print(f"""Dodawanie : {liczba_1 + liczba_2}
Odejmowanie: {liczba_1 - liczba_2}
Mnozenie: {liczba_1 * liczba_2}
Dzielenie: {liczba_1 * liczba_2}
Reszta z dzielenia: {liczba_1 % liczba_2}
Potęgowanie: {liczba_1 ** liczba_2} """)


