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

# tupla jest niemutowalna
# tupla_liczby[2] = 123  # TypeError: 'tuple' object does not support item assignment

# usunięcie całej tupli
del tupla_liczby

tupla_imiona = "Radek", "Tomek", "Zenek", "Olek", "Robert", 'Michał'
print(type(tupla_imiona))  # <class 'tuple'>
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Olek', 'Robert', 'Michał')

print(tupla_imiona.index("Radek"))  # numer indeksu 0
print(tupla_imiona.count("Zenek"))  # występuje 1 raz

tup = 1, 2
print(type(tup))  # <class 'tuple'>
a, b = 1, 2
print(a, b)

# rozpakowanie tupli
x, y = tup
print(x, y)  # 1 2

tup_1 = 1, 2, 3
# a, b = tup_1# ValueError: too many values to unpack (expected 2)
a, *b = tup_1  # * worek na dane
print(a, b)  # 1 [2, 3]
print(type(b))  # <class 'list'>

print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Olek', 'Robert', 'Michał')
# name1, name2, name3
name1, name2, *name3 = tupla_imiona
print(name1, name2, name3)  # Radek Tomek ['Zenek', 'Olek', 'Robert', 'Michał']

name1, *name2, name3 = tupla_imiona
print(name1, name2, name3)  # Radek ['Tomek', 'Zenek', 'Olek', 'Robert'] Michał

lista = list(tupla_imiona)
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Olek', 'Robert', 'Michał']
print(type(lista))  # <class 'list'>
lista.append("Zbyszek")

tupla_imiona = tuple(lista)
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Olek', 'Robert', 'Michał', 'Zbyszek')
