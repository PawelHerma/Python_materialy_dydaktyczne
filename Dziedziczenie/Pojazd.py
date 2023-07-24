# tworzymy klasę nadrzędną Samochód
class Pojazd:

    # deklarujemy metody, które są uniwersalne dla każdej klasy podrzędnej

    # konstruktor
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
    
    # metoda wypisująca informacje o pojeździe
    def __str__(self):
        return f"To jest {self.marka} {self.model}"