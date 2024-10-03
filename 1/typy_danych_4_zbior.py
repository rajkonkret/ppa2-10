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
