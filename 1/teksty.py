tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))
# Witaj Świecie
# <class 'str'>

# teksty są niemutowalne
tekst.upper()  # zmienia tekst na duże litery,  """ Return a copy of the string converted to uppercase. """
print(tekst)  # Witaj Świecie
print(tekst.upper())  # WITAJ ŚWIECIE
tekst_upper = tekst.upper()
print(tekst_upper)

# zamienic na male litery
print(tekst.lower())  # witaj świecie

print(tekst)  # Witaj Świecie,  zachowało  oryginalny wygląd
# Witaj Świecie
# 0123456789.... indeksowanie od zera
print(tekst.index("j"))  # indeks 4 (miejsce 5)
print(tekst.count("i"))  # występuje 3 razy
print(tekst.count("j", 0, 4))  # występuje 0 razy, z prawej zbiór otwarty, sprawdza tylko indeksy 0123

print(tekst.removeprefix("Witaj"))  # " Świecie", dostaliśmy kopię
print(tekst.removesuffix("Świecie"))  # "Witaj "
print(tekst.removesuffix("Świecie").strip())  # "Witaj"
# strip() - usunie biłae znaki, wiodące i końcowe spacje

tekst_zamiana = "Witaj dobry Świecie"
print(tekst_zamiana.replace("dobry", ""))  # "Witaj  Świecie"
print(tekst_zamiana.replace("dobry ", ""))  # "Witaj Świecie"

print(tekst[4])  # "j" - litera o indeksie 4 (pozycja 5)

imie = "Radek"
# f - string, czyli sformatowany string
tekst_format = f"\tMam na imię {imie}\n i lubię pythona.\b"
print(tekst_format)
# "	Mam na imię Radek
#  i lubię pythona"
# \t tabulator
# \n nowy wiersz
# \b backspace

starszy = "Witaj %s!"  # %s - łańcuch znaków (string),  w to miejsce wwsatwimy tekst
print(starszy % imie)  # tu podstawiamy tekst w miejsce %s
# Witaj Radek!

print("Witaj {}!".format(imie))  # Witaj Radek!

# tekst wielolinijkowy
print("""Tekst
    wielolinijkowy""")

# "Tekst
#     wielolinijkowy"

"""Komentarz
    wielolinijkowy"""

'''Komentarz 
    wielolinijkowy'''
