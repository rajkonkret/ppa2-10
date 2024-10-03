# warunki - instrukcje sterowania przepływem programu
# w zależności od warunku (True False) wykona jeden lub drugi blok programu
# if

odp = True
print(bool(odp))  # True
odp = False
# odp = "a"
print(bool(odp))

if odp:  # sprawdzamy co zwraca bool(odp)
    # jesli warunek True wykona się ten blok kodu
    # wcięcie 4 spacje
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza część programu")
# True
# Brawo
# Brawo
# Brawo
# Brawo
# Dalsza część programu
# dla False tylko wyświetli:
# Dalsza część programu

odp = "Radek"  # -> True
if odp:
    print("Radek")  # Radek

if odp == "Radek":
    print("Nadal Radek")  # Nadal Radek

if odp == "Tomek":
    print("Tomek")
else:  # w przeciwnym przypadku
    print("To nie jest Tomek")  # To nie jest Tomek

# wypisz długosć tekstu gdy tekst dłuższy niz 3
n = len(odp)
if n > 3:
    print("Długosc", n)
else:
    print(odp)
# Długosc 5

# walrus operator, operator morsa
if (n := len(odp)) > 3:
    print("Długość", n)
else:
    print(odp)
# Długość 5

podatek = 0
zarobki = int(input("Podaj zarobki"))
# pierwszy spełniony warunek -> wyjście z drzewka
# kolejnosc warunków ma znaczenie
if zarobki < 10_000:
    podatek = 0
elif zarobki < 30_000:  # zakres od 10000 do 29999
    podatek = 0.2
elif zarobki < 100_000:
    podatek = 0.4
else:
    podatek = 0.9

print(f"Podatek wynosi {podatek * zarobki} pln")
# dodaj podatek 0.2 dla przedziału od 10000 do 29999
