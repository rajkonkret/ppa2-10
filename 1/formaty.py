user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001  # float, liczby zmiennoprzecinkowe
print(type(wersja))  # <class 'float'>
liczba = 456123789345  # int
print(type(liczba))  # <class 'int'>

print("Witaj %s, masz teraz %d lat." % (user, wiek))  # Witaj Tomek, masz teraz 39 lat.
# print("Witaj %s, masz teraz %d lat." % (wiek, user))  # TypeError: %d format: a real number is required, not str
# %s - łańcuch znaków (string)
# %r - reprezentacja obiektu (repr)
# %d - liczba całkowita (integer)
# %i - liczba całkowita (integer)

print("Witaj {}, masz teraz {} lat ".format(user, wiek))  # Witaj Tomek, masz teraz 39 lat

print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat.
# f - fstring, sformatowany tekst

print("Uzywamy wersji pythona %i" % 3)  # Uzywamy wersji pythona 3
print("Uzywamy wersji pythona %f" % 3)  # Uzywamy wersji pythona 3.000000
print("Uzywamy wersji pythona %f" % 3.9)  # Uzywamy wersji pythona 3.900000
print("Uzywamy wersji pythona %.2f" % 3.9)  # Uzywamy wersji pythona 3.90
print("Uzywamy wersji pythona %.1f" % 3.9)  # Uzywamy wersji pythona 3.9
print("Uzywamy wersji pythona %.0f" % 3.9)  # Uzywamy wersji pythona 4
print("Uzywamy wersji pythona %.f" % 3.9)  # Uzywamy wersji pythona 4

x = 3.99999
print("Zmienna %.f" % x)  # Zmienna 4
print("Zmienna", x)  # Zmienna 3.99999

print(f"Uzywamy wersji pythona {wersja}")
print(f"Uzywamy wersji pythona {wersja:.1f}")
print(f"Uzywamy wersji pythona {wersja:.2f}")
print(f"Uzywamy wersji pythona {wersja:.0f}")
# Uzywamy wersji pythona 3.900001
# Uzywamy wersji pythona 3.9
# Uzywamy wersji pythona 3.90
# Uzywamy wersji pythona 4

print(f'{user:>10}')  # "     Tomek"
print(f"{user:<15}")  # "Tomek          "
print(f"{user:^20}")  # "       Tomek        "

print(liczba)  # 456123789345
print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 456,123,789,345
print(f"Nasza duża liczba {liczba:_}")  # Nasza duża liczba 456_123_789_345
print(f"Nasza duża liczba {liczba:_}".replace("_", " "))  # Nasza duża liczba 456 123 789 345
print(f"Nasza duża liczba {liczba:_}".replace("_", "."))  # Nasza duża liczba 456.123.789.345

# liczba_2 = 15000000
liczba_2 = 15_000_000
print(liczba_2)  # 15000000
print(type(liczba))  # <class 'int'>
