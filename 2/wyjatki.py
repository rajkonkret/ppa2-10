# wyjątki - błedy podczas wykonywania programu
# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\ppa2-10\2\wyjatki.py", line 2, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
try:
    # print(5 / 0)
    # print("A" + 9)
    # print(int("A"))
    # raise KeyError("Błąd klucza")  # raise - rzucenie wyjatku
    wynik = 90 / 33
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Błąd typu")
except ValueError:
    print("Błąd wartości")
except Exception as e:
    print("Błąd", e)
else:  # tylko gdy nie ma błędu
    print(f"Wynik działąnia {wynik}")
finally:  # wykonuje sie zawsze, musi byc na końcu jeśli jest
    print("kolejne działanie")

print("Program nadal działa")
# try  except [else finally]
# Nie dziel przez zero
# Program nadal działa
# Błąd typu
# Program nadal działa
# Błąd wartości
# Program nadal działa
# Błąd 'Błąd klucza'
# Program nadal działa
# Wynik działąnia 2.727272727272727
# Program nadal działa
# Wynik działąnia 2.727272727272727
# kolejne działanie
# Program nadal działa
# Błąd 'Błąd klucza'
# kolejne działanie
# Program nadal działa
