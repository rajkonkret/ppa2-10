# while - pętla sterowana warunkiem

# pętla nieskończona
# while True:
#     print("Kominikat 1 !")

licznik = 0
while True:
    licznik += 1  # licznik = licznik  + 1
    print("Kominikat 2 !!")
    if licznik > 10:
        break  # przerywa pętlę

print(licznik)
licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!!")
# 11
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!

lista = []
lista_int = []
while True:
    wej = input("Podaj liczbę")
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))

print(lista)
print(lista_int)
# ['1', '2', '3', '7', '89']
# [1, 2, 3, 7, 89]
#  A string is numeric if all characters in the string are numeric

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
element_to_remove = 5
while element_to_remove in my_list:
    my_list.remove(element_to_remove)

print(my_list)  # [1, 2, 3, 4, 6]
