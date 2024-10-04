# stworzyc funkcje obliczjącą średnią ocen
def liczby(name=None, *cyfry):  # * - dowolna ilość argumentów pozycyjnych
    print(cyfry)  # (3, 4, 5, 5) - tupla, krotka
    count = len(cyfry)  # sprawdzamy długość krotki, ile jest elementów
    suma_python = sum(cyfry)
    print(suma_python)
    suma = 0
    try:
        for c in cyfry:
            suma += c  # suma = suma + c
        avg = suma / count  # liczymy średnią
    except Exception as e:
        print("Błąd", e)
    else:
        print("Liczba ocen", count)
        print(f"Średnia dla ucznia {name} wynosi {avg}")  # wypisujemy średnią
    finally:
        print("Kolejny uczeń")


liczby()
liczby(3, 4, 5, 5)
liczby("Radek", 3, 4, 5, 5)
# "Radek", 3, 4, 5, 5 -> name, *cyfry
# ()
# Błąd division by zero
# Kolejny uczeń
# (3, 4, 5, 5)
# Średnia wynosi 4.25
# Kolejny uczeń
# Błąd division by zero
# Kolejny uczeń
# (4, 5, 5)
# Liczba ocen 3
# Średnia dla ucznia 3 wynosi 4.666666666666667
# Kolejny uczeń
# (3, 4, 5, 5)
# Liczba ocen 4
# Średnia dla ucznia Radek wynosi 4.25
# Kolejny uczeń
