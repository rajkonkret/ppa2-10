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


# uruchomienie funkcji
# nazwa_funkcji i nawiasy ()
dodaj()  # 14
