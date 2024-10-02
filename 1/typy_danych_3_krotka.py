# krotka (tupla) - kolekcja niemutowalna
# pozwala efektywniej zarządzac pamięcią
# tupla jednoelementowa - stała - zmienna

tupla = ("Radek")
print(type(tupla))  # <class 'str'>

tupla_2 = "Radek",
print(type(tupla_2))
print(tupla_2)  # ('Radek',)

# PEP8 - zaleca by tuple jedonelementową tworzyc z nawiasami
tupla_3 = ('Radek',)
print(type(tupla_3))  # <class 'tuple'>
print(tupla_3)  # ('Radek',)

tupla_liczby = 43, 55, 22.34, 11, 200
print(type(tupla_liczby))  # <class 'tuple'>
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)
