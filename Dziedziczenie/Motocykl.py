from Pojazd import Pojazd

class Motocykl(Pojazd):

    # nadpisujemy konstruktor
    def __init__(self, marka, model):
        super().__init__(marka, model)
        self.liczba_kół = 2

    # dodajemy metody, które będą działały tylko przy motocyklach
    def podaj_liczbę_kół(self):
        print(f"{self.liczba_kół} kół")
    
    def jedź(self):
        print("ŁUTUTUTUTUTU")

motocykl1 = Motocykl("Honda", "Shadow")

motocykl1.podaj_liczbę_kół()

motocykl1.jedź()