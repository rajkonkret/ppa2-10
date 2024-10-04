# funkcja zwracająca wynik
# kończy się komendą return

def dodaj(a, b):
    return a + b


def odejmij(a=0, b=0, c=0):
    return a - b - c


print(dodaj(6, 90))
wyn = dodaj(23, 78)
print("Wynik:", wyn)
# 96
# Wynik: 101
print(odejmij())
print(odejmij(1, 2, 5))
print(odejmij(1, b=8))
# 96
# Wynik: 101
# 0
# -6
# -7
print(odejmij(6, 90))

print(dodaj(5, 10) + odejmij(5, 89))
# -84
# -69
