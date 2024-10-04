# funkcje - wydzielony fragment kodu, można go wykonac w dowolnym momencie
# funkcja musi zostac najpierw zadeklarowana
# w miejscu deklaracji nie jest wykonywana
# zeby funkcję wykonać należy ją wywołać

a = 6
b = 8


# deklaracja funkcji def nazwa i nawiasy ()
# PEP8 aby deklaracja funkcji była oddzielona dwoma pustymi linijkami od ciała programu
def dodaj():  # funkcja bez argumentów
    print(a + b)


def dodaj2(a, b):  # dwa obowiązkowe argumenty
    print(a + b)  # argumenty lokalne


def odejmij(a, b, c=0):  # c - argument z wartością domyślną
    print(a - b - c)


# uruchomienie funkcji
# nazwa_funkcji i nawiasy ()
dodaj()  # 14
# dodaj2()# TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'

# przekazywanie przez pozycję, argumenty pozycyjne
dodaj2(5, 9)  # 14
odejmij(1, 2)  # c=0, -1
odejmij(1, 2, 3)  # c=3, -4

# przekazania argumentów po nazwie,
odejmij(c=9, a=8, b=10)  # -11
odejmij(b=9, a=7)  # -2

# mieszane
odejmij(1, c=10, b=34)  # -43
# odejmij(a=10, 2, 3)  # SyntaxError: positional argument follows keyword argument

print(dodaj())  # None

# print(dodaj() + dodaj2())  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
