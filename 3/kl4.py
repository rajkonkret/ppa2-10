class Car:
    """
    Samochód w pythonie
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        # hermetyzacja
        self.__predkosc = 0  # pole prywatne

    # enkapsulacja - hermetyzacja pol i wystawienie dedykowanych metod do odczytu i zapisu tych pól
    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Jadę z szybkością {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10
        self.__zmien_bieg()

    def __zmien_bieg(self):  # metoda prywatna
        print("Zmiana biegu")


car = Car('Opel', 2024)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
# po oznaczeniu jako pole prywatne
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(car.__predkosc)  # 50
car.licznik()  # Jadę z szybkością 50 km/h
# car.__predkosc = 0
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.licznik()
# Jadę z szybkością 50 km/h
# Jadę z szybkością 0 km/h
# Jadę z szybkością 50 km/h
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Jadę z szybkością 0 km/h
