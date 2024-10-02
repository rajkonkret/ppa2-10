import sys

wiek = 47
rok = 2024
temp = 36.6  # float

print(temp)
print(type(temp))
# 36.6
# <class 'float'>

print(wiek + rok)  # 2071
print(wiek - rok)  # -1977
print(wiek * rok)  # 95128
print(rok / wiek)  # 43.06382978723404, float
print(rok // wiek)  # 43, cześć calkowita dzielenia
print(rok % wiek)  # reszta z dzielenia, modulo, reszta 3, jak na patyczkach
print(10 % 3)  # r = 1

print(wiek ** rok)  # potęgowanie
print(len(str(wiek ** rok)))  # długość 3385
# print(wiek ** rok ** 2)
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0

# w przypadku liczb float występuje bład zaokroglęnia
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
#   For example, in a floating-point arithmetic with five base-ten digits of precision,
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# decimal - preferowany do obliczen na pieniadzach
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308,
#                max_exp=1024,
#                max_10_exp=308,
#                min=2.2250738585072014e-308,
#                min_exp=-1021,
#                min_10_exp=-307,
#                dig=15,
#                mant_dig=53,
#                epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(f"Sprawdzenie zmiennej {temp} {wiek}")
print(f"""
{wiek}
    {temp}""")
# Sprawdzenie zmiennej 36.6 47
#
# 47
#     36.6

# typ logiczny
# prawda, fałsz
# True, False
# 1 - prawda, 0 - fałsz
czy_znasz_pythona = True
print(czy_znasz_pythona)  # True
print(type(czy_znasz_pythona))  # <class 'bool'>

print(int(czy_znasz_pythona))  # 1
print(int(False))  # 0

print(bool(1))  # bool() - rzutowanie na bool(), na typ logiczny, True
print(bool(100))  # True
print(bool(-10))  # True
print(bool(-6.8))  # True
print(bool("radek"))  # True

print(bool(0))  # False
print(bool(""))  # False
print(bool(None))  # False, stan nieokreslony, odpowiednik null w innych językach

# Expression    Evaluates to
# True and True    True
# True and False    False
# False and True    False
# False and False    False
# The or Operator’s Truth Table:
#
# Expression    Evaluates to
# True or True    True
# True or False    True
# False or True    True
# False or False    False
# The not Operator’s Truth Table:
#
# Expression    Evaluates to
# not True    False
# not False   True

print(True and False)  # and -> i -> False
print(True or False)  # or -> lub -> True

a = 6
b = 8
# wynik porównania zwraca typ boolean
print(f"Porównanie {a} > {b} = {a > b}")  # Porównanie 6 > 8 = False
print(f"Porównanie {a} < {b} = {a < b}")  # Porównanie 6 < 8 = True
print(f"Porównanie {a <= b=}")  # Porównanie a <= b=True
print(f"Porównanie {a >= b=}")  # Porównanie a >= b=False
print(f"Porównanie {a} == {b} = {a == b}")  # Porównanie 6 == 8 = False, == porównanie
print(f"Porównanie {a} != {b} = {a != b}")  # Porównanie 6 != 8 = True, czy różne
