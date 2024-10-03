# set (zbiór) - przechowuje unikalne wartości
# nie zachowuje kolejności przy dodawaniu
# nie posiada indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>

# tworzenie pustego seta
zb2 = set()  # <class 'set'>
print(zb2)  # set()

zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(18)
zbior.add(24)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55, 24}

# usunięcie elementu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 24}

# pop() - usunie pierwszy element
print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 44, 18, 22, 24}

zbior_copy = zbior.copy()
print(zbior)
print(id(zbior), id(zbior_copy))  # 2788340719776 2788340715296

zbior_2 = {667, 11, 44, 18, 52, 62, 999, 999, 12.34}
print(zbior_2)  # {999, 11, 44, 12.34, 18, 52, 667, 62}
print(type(zbior_2))  # <class 'set'>

# suma zbiorów
print(zbior | zbior_2)  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}
print(zbior.union(zbior_2))  # {66, 999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}

# częśc wspólna zbiorów
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# róznica
print(zbior - zbior_2)  # {24, 777, 66, 22}
print(zbior.difference(zbior_2))  # {24, 777, 66, 22}
print(zbior_2.difference(zbior))  # {999, 12.34, 52, 667, 62}

lista = list(zbior)
print(lista)  # [66, 777, 11, 44, 18, 22, 24]
print(type(lista))  # <class 'list'>

# sprawdzenie czy element istnieje w kolekcji
print(999 in zbior_2)  # True
