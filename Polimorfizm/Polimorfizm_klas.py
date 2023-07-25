class Auto:
    
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def porusz_się(self):
        print(f"{self.nazwa} robi brum brum")

class Motorówka:

    def __init__(self, nazwa):
        self.nazwa = nazwa

    def porusz_się(self):
        print(f"{self.nazwa} robi wrruuuuuuum")

class Samolot:

    def __init__(self, nazwa):
        self.nazwa = nazwa

    def porusz_się(self):
        print(f"{self.nazwa} robi fiuuuuuuuuuu")

auto = Auto("Bugatti")
motorówka = Motorówka("Speedy 2000")
samolot = Samolot("Boeing 737")

for pojazd in (auto, motorówka, samolot):
    pojazd.porusz_się()