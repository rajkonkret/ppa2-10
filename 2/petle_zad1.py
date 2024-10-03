# pętle - dają możłiwość wykonannai tego samego kodu wielokrotnie
# for - pętlą iteracyjna
import random

for i in range(5):  # 0 do 4
    print(i)
# 0
# 1
# 2
# 3
# 4

for i in range(10):
    pass  # nic nie rób

for _ in range(10):  # _ niema zmienna
    print("Test podłoga")
    print(_)
# Test podłoga
# 8
# Test podłoga
# 9

for i in range(10):
    print(i * 2)

# z poprzedniego zadania (random)
# wykorzstac pętlę i w petli wylosowac 6 liczb uzywajac bloku , który miał się powtarzać
lista_wyn = []
lista_kul = list(range(1, 50))
for _ in range(6):  # 0 do 5
    wyn = random.choice(lista_kul)
    lista_kul.remove(wyn)
    print(wyn)
    lista_wyn.append(wyn)

print(lista_wyn)  # [5, 1, 17, 8, 45, 27]
# 23
# 42
# 6
# 30
# 36
# 1

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

print(lista_wyn)
for c in lista_wyn:
    if c > 10:
        print("Większe od 10", c)
    else:
        print("Mniejsze od 10", c)
# Większe od 10 31
# Mniejsze od 10 1
# Większe od 10 49
# Większe od 10 24
# Mniejsze od 10 2
# Większe od 10 46

for i in range(0, 10, 2):  # start, stop, krok
    print(i)

for i in range(10, 0, -2):  # krok ujemny, odliczamy w dół
    print(i)
# 10
# 8
# 6
# 4
# 2
for i in range(-10, 0):
    print(i)

imiona = ['Radek', "Tomek", "Zenek", 'Marta']

for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Marta

# 0 Radek
# enumerate()
for p in enumerate(imiona):
    print(p)

# krotka
# (0, 'Radek') -> 0 Radek
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Marta')
a, b = (3, 'Marta')
print(a, b)  # 3 Marta
for i, p in enumerate(imiona):
    print(i, p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Marta

for i, p in enumerate(imiona, start=1):
    print(i, p)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Marta

wiek = [34, 45, 23, 29]
# Radek 34
# zip() - łaczy kolekcje
for i in zip(imiona, wiek):
    print(i)
# ('Radek', 34)
# ('Tomek', 45)
# ('Zenek', 23)
# ('Marta', 29)
for i, w in zip(imiona, wiek):
    print(i, w)
# Radek 34
# Tomek 45
# Zenek 23
# Marta 29
