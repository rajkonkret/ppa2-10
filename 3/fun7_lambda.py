# funkcja lambda
# skrócony zapis funkcji
# zwraca wynik (return)
# funkcja anonimowa, możliwość uzycia w miejscu deklaracji

def odejmij(a, b):
    return a - b


print(odejmij(100, 67))  # 33

odejmij2 = lambda a, b: a - b
print(odejmij2(245, 89))  # 156

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

lista = [1, 2, 3, 10, 20, 50, 70, 200, 300, 500]
lista_wyn = []
for i in lista:
    lista_wyn.append(i * 2)
print(lista_wyn)  # [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]
print([i * 2 for i in lista])  # [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]


# mapowanie danych
def zmien(x):
    return x * 2


lista_wyn_2 = []
for i in lista:
    lista_wyn_2.append(zmien(i))

print(lista_wyn_2)  # [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]
# map() - bierze kolejne lementy kolekcji, wykonuje na nich zadaną funkcję
print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]

# lambda jako funkcja anonimowa, deklaracja w mmiejscu wykonnia
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map(): [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 12, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x / 5, lista))}")
# Zastosowanie map(): [4, 8, 12, 40, 80, 200, 280, 800, 1200, 2000]
# Zastosowanie map(): [12, 24, 36, 120, 240, 600, 840, 2400, 3600, 6000]
# Zastosowanie map(): [0.2, 0.4, 0.6, 2.0, 4.0, 10.0, 14.0, 40.0, 60.0, 100.0]

# filtrowanie danych
print(lista)  # [1, 2, 3, 10, 20, 50, 70, 200, 300, 500]
l3 = []
for i in lista:
    if i < 20:
        l3.append(i)
print(l3)  # [1, 2, 3, 10]

# filter() - zwraca elelmenty spełniające warunek
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 20, lista))}")  # Zastosowanie filter(): [1, 2, 3, 10]
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 20, lista))}")  # Zastosowanie filter(): [50, 70, 200, 300, 500]
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 5 and x < 100, lista))}")  # Zastosowanie filter(): [10, 20, 50, 70]
print(f"Zastosowanie filter(): {list(filter(lambda x: 5 < x < 100, lista))}")  # Zastosowanie filter(): [10, 20, 50, 70]
# map(), filter()  - funkcje wyższego rzędu
