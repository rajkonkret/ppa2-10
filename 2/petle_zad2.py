dictionary = {'imie': "Radek", 'nazwisko': "Kowalski"}
print(type(dictionary))  # <class 'dict'>
# klucz, wartość, para klucz-wartosć

# wypisuje klucze ze słownika
for i in dictionary:
    print(i)
# imie
# nazwisko

for i in dictionary.keys():
    print(i)
# imie
# nazwisko

# wypisuje wartości
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# wypisze pary
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')
for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski
#  sep=' '
for k, v in dictionary.items():
    print(k, v, sep="=>")
# imie=>Radek
# nazwisko=>Kowalski

# end='\n' przejscie do nowej lini
for k, v in dictionary.items():
    print(k, v, sep="=>", end="<=>")  # imie=>Radek<=>nazwisko=>Kowalski<=>
print()

pol_ang = {'kot': 'cat', 'pies': 'dog', 'dach': 'roof'}
ang_pol = {}
for k, v in pol_ang.items():
    ang_pol[v] = k
print(ang_pol)  # {'cat': 'kot', 'dog': 'pies', 'roof': 'dach'}

print({value: key for key, value in pol_ang.items()})
# {'cat': 'kot', 'dog': 'pies', 'roof': 'dach'}
