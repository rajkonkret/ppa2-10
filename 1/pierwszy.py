import sys

print()  # wypisz/wydrukuj

print("Nazywam się Radek")
# ctrl d - powielenie elementów
print('Nazywam się Radek')
#
# Nazywam się Radek
# Nazywam się Radek
# print('Nazywam się Radek")
#   File "C:\Users\CSComarch\PycharmProjects\ppa2-10\1\pierwszy.py", line 9
#     print('Nazywam się Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 9)
print("Nazywam sie 'Radek'")  # Nazywam sie 'Radek'
# dane tekstowe - string
# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'> dane tekstowe
print("39")
print(type("39"))  # <class 'str'>

# dane liczbowe
print(39)
print(type(39))  # <class 'int'>, liczby calkowite
# print("39" + 39)# TypeError: can only concatenate str (not "int") to str

print("39" + "39")  # 3939, łączenie stringów, konkatenacja, silne typowanie
print(39 + 39)  # 78

print(168 * "35")
# 353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535353535
print(168 * 35)  # 5880

print(168 + int("35"))  # 203, int() - rzutowanie zamiana na liczbę całkowitą
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)
# ctrl shift insert - Column selection mode
print(8 + 8 + 8)  # 24
print("8" + "8" + "8")  # 888

print("Radek" + str(39))  # str() - rzutowanie, zamiana liczby na tekst, Radek39
# Process finished with exit code 0 - program skończyl się bez błędu
# Process finished with exit code 1 - -oznacza błąd podczas wykonywania programu
