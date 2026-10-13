# Lab 01 – Zadanie 2 (★): Wizytówka
#
# Program pyta użytkownika kolejno o:
#   1. imię,
#   2. nazwisko,
#   3. rok urodzenia (liczba całkowita),
# a potem wypisuje jedno zdanie, np.:
#     Nazywam się Anna Kowalska i w 2026 roku kończę 20 lat.
#
# Wskazówki:
#   - input() zawsze zwraca tekst (str) – rok zamień na liczbę: int(...)
#   - użyj f-stringa: f"Nazywam się {first_name} ..."

CURRENT_YEAR = 2026

# TODO: Twój kod poniżej
Imie = input('Podaj imię :')
Nazwisko = input('Podaj nazwisko :')
Rok_urodzenia = int(input('Podaj rok urodzenia : '))
Aktualny_wiek = CURRENT_YEAR - Rok_urodzenia 
print(f"Mam na imię {Imie} {Nazwisko} i w {CURRENT_YEAR} roku konczę {Aktualny_wiek}")