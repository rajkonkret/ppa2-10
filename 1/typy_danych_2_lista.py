# kolekcje  - wiele danych w jednym pudełku
# lista - przechowuje wiele danych, różnego typu na raz
# zachowuje kolejność przy dodawaniu elementów
# względnie cięzka dla systemu

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# append()
lista.append("Radek")
lista.append("Zenek")
lista.append("Tomek")
lista.append("Marek")
lista.append("Magda")
lista.append("Ania")
print(lista)  # ['Radek', 'Zenek', 'Tomek', 'Marek', 'Magda', 'Ania']
# ['Radek', 'Zenek', 'Tomek', 'Marek', 'Magda', 'Ania']
#       0      1         2       3        4        5
#       -6     -5       -4      -3        -2      -1
print(lista[0])  # Radek
print(lista[2])  # Tomek
print(lista[4])  # Magda

# print(lista[6])  # IndexError: list index out of range
print(len(lista))  # 6, długosc listy
print(lista[len(lista) - 1])  # Ania
print(lista[-1])  # Ania, ostatni element
print(lista[-2])
print(lista[-3])  # Marek

