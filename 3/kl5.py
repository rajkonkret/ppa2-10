from abc import ABC, abstractmethod


# klasa abstrakcyjna

class Ptak(ABC):
    """
    Klasa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca
        :param gatunek:
        :param szybkosc:
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # dekorator
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("Ko ko ko ko ko koo")


class Orzel(Ptak):
    """
    Klasa orzeł
    """

    def wydaj_odglos(self):
        print("Kier kir kier")


# po oznaczeniu klasy Ptak jako abstrakcyjna
# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzeł", 45)
# or1.latam()  # Tu Orzeł Lecę z szybkością 45
# kur1 = Ptak("Kura domowa", 0)
# kur1.latam()  # Tu Kura domowa Lecę z szybkością 0

kur2 = Kura("Kura Domowa")
kur2.latam()  # Tu Kura Domowa Ja nie latam
kur2.wydaj_odglos()  # Ko ko ko ko ko koo
or2 = Orzel("Orzeł Bielik", 50)
or2.wydaj_odglos()
or2.latam()
# Kier kir kier
# Tu Orzeł Bielik Lecę z szybkością 50

# polimorfizm - wspolne cechy dla obiektów różnych klas
lista = [or2, kur2]
for i in lista:
    i.wydaj_odglos()
# Kier kir kier
# Ko ko ko ko ko koo
