a = 10
b = 10


def dodaj():
    a = 7  # to są zmienne o zasięgu lokalnym
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a  # użyj globalne a
    a = 9  # wartość globalnego a zostanie zmieniona
    b = 34
    print(a + b)


print(f"Wartość a globalna {a=}")  # Wartość a globalna a=10
dodaj()  # 15
print(f"Wartość a globalna {a=}")  # Wartość a globalna a=10
# shift alt strzałka w dół - przesunięcie lini w dół
dodaj2()  # 20 - uzywa globalnych argumentów
print(f"Wartość a globalna {a=}")  # Wartość a globalna a=10
dodaj3()  # 43
print(f"Wartość a globalna {a=}")  # Wartość a globalna a=9
print(a, b)
dodaj2()
# 9 10
# 19
