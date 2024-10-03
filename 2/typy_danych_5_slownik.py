# słownik - para klucz-wartosc
# {'user' : 'Radek', 'wiek' : 78}
# odpowiednik jsona w pythonie
# klucze nie mogą się powtórzyć

# pusty słownik
dictionary = dict()
print(type(dictionary))  # <class 'dict'>
print(dictionary)  # {}

# puste klamerki to słownik
dictionary_1 = {}
print(type(dictionary_1))  # <class 'dict'>

# dodawanie elementów do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 38
print(dictionary)  # {'imie': 'Radek', 'wiek': 38}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 38])
# dict_items([('imie', 'Radek'), ('wiek', 38)])
# [('imie', 'Radek'), ('wiek', 38)] -> lista krotek

# nadpisanie elemntu
dictionary['imie'] = "Wiktor"
print(dictionary)  # {'imie': 'Wiktor', 'wiek': 38}

# wypisanie wartośc dla danego klucza
print(dictionary['imie'])  # Wiktor
# print(dictionary['Imie'])# KeyError: 'Imie' brak takiego klucza
print(dictionary.get("Imie"))  # None
print(dictionary.get("Imie", "Default"))  # Default

# # input()
# tekst = input("Podaj imię")
# print(tekst)
# print(type(tekst))  # <class 'str'> zwraca str

# napisac aplikacje kalkulator
# podaj dwie liczby -> input x 2
# wyswietl wynik -> print
# a = float(input("Podaj pierwszą  liczbę"))
# # a = input("Podaj pierwszą  liczbę")
# b = input("Podaj drugą  liczbę")
# print(a + int(b))  # 6.0
# # print(a + b)
# ctrl /

# napisac aplikacje słownik pol-ang
# wypisac zasób słów -> klucze
# pobrac od użytkownika słowo do przetłumaczenia
# wypisac tłumaczenie
# zdefiniowac słownik
pol_ang = {'kot': 'cat', 'pies': 'dog', 'roof': 'dach'}
print(f"Mamy w słowniku {pol_ang.keys()}")
odp = input("Podaj słówko do przetłumaczenia")
# print(pol_ang[odp.lower().strip()])
print(pol_ang.get(odp, "nie mo"))
# cat
# nie mo
