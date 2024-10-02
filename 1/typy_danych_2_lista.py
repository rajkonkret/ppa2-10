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

# wyświetlanie fragmentu listy (slicowanie)
print(lista[0:3])  # ['Radek', 'Zenek', 'Tomek'], tylko indeksy 012
print(lista[:3])  # ['Radek', 'Zenek', 'Tomek']
print(lista[2:])  # ['Tomek', 'Marek', 'Magda', 'Ania'], indeksy 2,3,4,5
print(lista[2:5])  # ['Tomek', 'Marek', 'Magda']
print(lista[2:6])  # ['Tomek', 'Marek', 'Magda', 'Ania']
print(lista[10:20])  # []
print(lista[:])  # ['Radek', 'Zenek', 'Tomek', 'Marek', 'Magda', 'Ania']

print(lista[-2:0])  # -> [4:0] # []
print(lista[0:-2])  # ['Radek', 'Zenek', 'Tomek', 'Marek']
print(lista[2:3])  # ['Tomek']
print(lista[0:5:2])  # ['Radek', 'Tomek', 'Magda']
# [start:stop:krok]

# nadpisanie elementu w liście
lista[3] = "Mikołaj"
print(lista)  # ['Radek', 'Zenek', 'Tomek', 'Mikołaj', 'Magda', 'Ania']

# insert() - wstawienie elementu we wskazany indeks
lista.insert(1, "Karol")
print(lista)  # ['Radek', 'Karol', 'Zenek', 'Tomek', 'Mikołaj', 'Magda', 'Ania']

# spraawdzenie indeksu dla danego elementu
print(lista.index("Mikołaj"))  # indeks numer 4
lista.append("Mikołaj")
lista.append("Mikołaj")
print(lista)  # ['Radek', 'Karol', 'Zenek', 'Tomek', 'Mikołaj', 'Magda', 'Ania', 'Mikołaj']
print(lista.index("Mikołaj"))  # index zwraca pierwszy element, 4
# ['Radek', 'Karol', 'Zenek', 'Tomek', 'Mikołaj', 'Magda', 'Ania', 'Mikołaj', 'Mikołaj']

# usunięcie elementu z listy, usunie pierwsze wystąpienie elementu
lista.remove("Mikołaj")
print(lista)  # ['Radek', 'Karol', 'Zenek', 'Tomek', 'Magda', 'Ania', 'Mikołaj', 'Mikołaj']

# usunięcie po indeksie, pokaże co usunął
print(lista.pop(5))  # Ania
print(lista)  # ['Radek', 'Karol', 'Zenek', 'Tomek', 'Magda', 'Mikołaj', 'Mikołaj']
print(lista.pop(-2))  # Mikołaj
print(lista)  # ['Radek', 'Karol', 'Zenek', 'Tomek', 'Magda', 'Mikołaj']
print(lista.pop())  # Mikołaj, usunie ostatni element z listy
