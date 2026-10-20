# Lab 02 – Zadanie 4 (★): Sekundy na godziny, minuty i sekundy
#
# Program wczytuje liczbę sekund (int) i wypisuje ją DOKŁADNIE w formacie:
#     1 h 2 min 5 s
# (dla 3725 sekund).
#
# Wskazówki:
#   - int(input(...)) – konwersja tekstu na liczbę całkowitą
#   - // dzielenie całkowite, % reszta z dzielenia
#   - 1 h = 3600 s, 1 min = 60 s

# TODO: Twój kod poniżej
sekundy = int(input("Wpisz liczbe sekund :"))
godziny = sekundy / 3600
reszta_g = sekundy % 3600
minuty = reszta_g / 60 
reszta_s = reszta_g % 60 
print(f"Twoj czas to :{godziny:.0f}h {minuty:.0f}m {reszta_s:.0f}s")
