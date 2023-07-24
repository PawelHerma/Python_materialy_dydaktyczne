class Człowiek:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
    
    def __str__(self):
        return f"To jest {self.imie} {self.nazwisko}. {self.imie} ma {self.wiek} lat"
    
osoba1 = Człowiek("Paweł", "Herma", 23)

print(osoba1)

class Student(Człowiek):
    def __init__(self, imie, nazwisko, wiek):
        super().__init__(imie, nazwisko, wiek)
        self.rok_studiow = self.wiek - 19

    def podaj_rok_studiow(self):
        print(self.rok_studiow)

osoba2 = Student("PAweł", "Herma", 23)

print(osoba2)

osoba2.podaj_rok_studiow()