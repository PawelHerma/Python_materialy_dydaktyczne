class Pojazd:

    def __init__(self, nazwa):
        self.nazwa = nazwa
    
    def porusz_się(self):
        print(f"{self.nazwa} rusza się")

class Auto(Pojazd):
    pass

class Samolot(Pojazd):

    def porusz_się(self):
        print(f"{self.nazwa} leci")

auto = Auto("Auto")
samolot = Samolot("Samolot")

for pojazd in (auto, samolot):
    pojazd.porusz_się()