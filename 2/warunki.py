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

# podatek = 0
# zarobki = int(input("Podaj zarobki"))
# # pierwszy spełniony warunek -> wyjście z drzewka
# # kolejnosc warunków ma znaczenie
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 30_000:  # zakres od 10000 do 29999
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi {podatek * zarobki} pln")
# # dodaj podatek 0.2 dla przedziału od 10000 do 29999

suma_zam = 150
if suma_zam > 100:
    rabacik = 25
else:
    rabacik = 0
print(f"Rabat wynosi {rabacik}")

rabat = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi {rabat}")
# Rabat wynosi 25
# Rabat wynosi 25

# zasymulujemy system zbierania logów
# zmienna - jaki system wysłał logi
# email, console, inny (else)
# dla console wypiszemy: "Stało się coś strasznego"
# dla email: "System email"
# jezeli system jest email:
# do listy błedów wpisać opis tego błedu np.: dla error -> Błąd krytyczny
# error, medium, inny (else)
lista_b = []
alert_system = "email"
error = "medium"

if alert_system == "console":  # == - porównanie
    print("Stało się coś strasznego")
elif alert_system == 'email':
    print("System email")
    if error == 'error':
        lista_b.append("Bład krytyczny")
    elif error == 'medium':
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("Inny")
else:
    print("Inny system")

print(lista_b)
# ['Ostrzeżenie']
