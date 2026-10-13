# Lab 01 – Zadanie 4 (☆, dodatkowe): Kategoria BMI
#
# Rozbuduj kalkulator BMI: po obliczeniu wypisz także kategorię (wg WHO):
#     BMI < 18.5          -> niedowaga
#     18.5 <= BMI < 25    -> waga prawidłowa
#     25 <= BMI < 30      -> nadwaga
#     BMI >= 30           -> otyłość
#
# To zadanie wymaga instrukcji if / elif / else, którą dokładnie poznasz
# w labie 03. Spróbuj już teraz – składnię znajdziesz na slajdach.

# TODO: Twój kod poniżej
waga = float(input("Podaj swoją wage w kilogramach : "))
wzrost = float(input("Podaj swój wzrost w metrach : "))
BMI = waga/(wzrost **2 )
print(f"Twoje BMI wynosi {BMI:.2f}")
if BMI < 18.5:
        print("Masz niedowage")
if 18.5 <= BMI < 25:
    print("Twoja waga jest prawidlowa")
if 25 <= BMI < 30:
      print("Masz delikatna niedowage")
if BMI >= 30:
      print("Jestes otyly") 