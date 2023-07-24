from abc import ABC, abstractmethod

class Pojazd(ABC):

    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
    
    def __str__(self):
        return f"To jest {self.marka} {self.model}"
    
    @abstractmethod
    def jedź(self):
        pass

class Samochód(Pojazd):
    def jedź(self):
        print("BRUM BRUM")

samochód1 = Samochód("Fiat", "Punto")

print(samochód1)

samochód1.jedź()
