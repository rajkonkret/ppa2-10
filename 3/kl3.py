class Pojazd:
    """
    klasa Pojazd
    """

    def __init__(self, kolor):
        """
        Metoda inicjalizująca
        :param kolor:
        """
        self.kolor = kolor

    def info(self):
        print("Kolor:", self.kolor)


class Samochod(Pojazd):  # dziedziczymy po klasie Pojazd
    """
    Samochod
    """

    def __init__(self, kolor, marka):
        super().__init__(kolor)  # musimy wywołąć konstruktor z klasy wyższej super()
        self.marka = marka

    def info(self):
        super().info()
        print("Marka", self.marka)


poj = Pojazd("czerwony")
poj.info()

car = Samochod("zielony", "Opel")
car.info()
# Kolor: czerwony
# Kolor: zielony
# Marka Opel
