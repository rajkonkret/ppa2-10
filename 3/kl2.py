# self - reprezentuje obiekt klasy, na nim klasa wykonuje czynności
class Human:
    """
    Klasa opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def powitanie(self):
        print("Nazywam się", self.imie)

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")

    # mam_wiek()
    def mam_wiek(self):
        print(f"Mam {self.wiek} lat.")


cz1 = Human("Anna", "29")
print(cz1.wiek)
print(cz1.imie)
print(cz1.plec)
# 29
# Anna
# k
cz2 = Human("Radek", 38, "m")
print(cz2.wiek)
print(cz2.imie)
print(cz2.plec)
# 38
# Radek
# m
# wywołanie metody powitanie na obiekcie cz1 i cz2
cz1.powitanie()
cz2.powitanie()
# Nazywam się Anna
# Nazywam się Radek
cz1.ruszaj()
cz2.ruszaj()
# Ruszyłam w drogę
# Ruszyłem w drogę
