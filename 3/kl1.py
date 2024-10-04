# klasa - element programowania obiektowego
# klasa - szablon, przepis
# wskazuje minimum cech
# obiekt (instancja) jest zbudowany wg szablonu
# definicja klasy nie wykonuje klasy
# budowanie obiektu uruchmia odpowiednią funkcje w klasie
# paradygmaty programowania obiektowego
# hermetyzacja, dziedziczenie, polimorfizm, abstrakcja
# pola (stan obiektu -> zmienne)
# metody -> (funkcje)

# deklaracja klasy
# PEP8 zaleca nazwy klas z duzej litery
class Human:
    """
    Klasa opisująca człowieka w pythonie
    """
    imie = ""
    plec = "k"


print(Human.__doc__)  # Klasa opisująca człowieka w pythonie
# print(print.__doc__)
# help(Human)
# cd 3 - wejscie do katalogu o nazwie 3
# cd .. - wyjście w górę
#  pydoc -w kl1 wygenerowanie pliku html z dokumentacją
# tworzymy obiekt tej klasy
cz1 = Human()
print(cz1.plec)
print(cz1.imie)
cz1.imie = "Anna"
print(cz1.plec)
print(cz1.imie)
# k
# Anna
