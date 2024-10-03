import random  # importowanie biblioteki do naszego programu

# generowanie liczb pseudolosowych

print(random.randint(1, 100))  # int, od 1 do 100
print(random.randrange(1, 100))  # int od 1 do 99
print(random.randrange(6))  # int 0 do 5
print(random.random())  # 0.8324249754599561 float od 0 do 0.9999999
print(random.random() * 50)  # 49.70615734711091 float od 0 do 49.999999

lista = [67, 45, 32, 68, 89, 90, 42]
print(random.choice(lista))  # 90 element z listy (na indeksie 5)

lista_kul = list(range(1, 50))  # 1 do 49
# wyn = random.choice(lista_kul)
# lista_kul.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kul)
# lista_kul.remove(wyn)
# print(wyn)
# wyn = random.choice(lista_kul)
# lista_kul.remove(wyn)
# print(wyn)

print(random.choices(lista_kul, k=6))  # [12, 1, 44, 9, 9, 26], losowanie z powtórzeniami
print(random.sample(lista_kul, k=6))  # [31, 5, 47, 48, 42, 13], bez powtórzeń
print(random.sample(lista_kul, 6))
# [17, 18, 26, 40, 31, 29]
# [48, 4, 26, 1, 35, 18]
