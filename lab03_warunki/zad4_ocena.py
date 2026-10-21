# Lab 03 – Zadanie 4 (★): Ocena z przedmiotu
#
# Program wczytuje liczbę punktów (0–100) i wypisuje ocenę według progów
# z sylabusa naszego przedmiotu:
#     > 91        -> 5
#     > 83 – 91   -> 4.5
#     > 75 – 83   -> 4
#     > 67 – 75   -> 3.5
#     > 60 – 67   -> 3
#     <= 60       -> 2
#
# Przykład:  Ocena: 4.5
# Uwaga: w zachęcie input() nie wypisuj liczb (np. „0-100”) – testy szukają liczb w wyjściu.

# TODO: Twój kod poniżej
pkt = int(input("Podaj swoja liczbe punktow"))
if pkt <= 60:
    print("Twoja ocena to 2")
elif 60 < pkt < 67:
    print("Twoja ocena to 3")
elif 67 <= pkt < 75:
    print("Twoja ocena to 3.5")
elif 75 <= pkt < 83:
    print("Twoja ocena to 4")
elif 83 <= pkt < 91:
    print("Twoja ocena to 4.5")
elif 91 <= pkt <= 100:
    print("Twoja ocena to 5")
else:
    print("Podaj wartosc punktowa w zakresie od 0-100")