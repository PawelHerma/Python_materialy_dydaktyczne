# deklaracja klasy
class Samochód:
    liczba_kół = 4
    liczba_drzwi = 5

# stworzenie obiektu klasy
fiat_punto = Samochód()

# wykorzystanie właściwości obiektu
print(f"liczba drzwi w fiacie punto: {fiat_punto.liczba_drzwi}")
print(f"liczba kół w fiacie punto: {fiat_punto.liczba_kół}")

class Osoba:

    # konstruktor z parametrami
    def __init__(self, imię, nazwisko, wiek):
        self.imię = imię
        self.nazwisko = nazwisko
        self.wiek = wiek
    
    # jeśli chcemy wydrukować cały obiekt możemy zadeklarować metodę __str__
    def __str__(self):
        return f"To jest {self.imię} {self.nazwisko}. \n{self.imię} ma {self.wiek} lat"
    
    # deklarowanie metod w klasie
    def przywitanie(self):
        print(f"Cześć, jestem {self.imię} :D")

# tworzenie obiektów klasy
paweł = Osoba("Paweł", "Herma", 20)
maciek = Osoba("Maciek", "Kowalski", 25)

# wywołanie metod
print(paweł)
paweł.przywitanie()

print(maciek)
maciek.przywitanie()

# usuwanie obiektów klasy
del maciek
# sprawdzenie
# maciek.przywitanie()

# jeśli nie mamy gotowej definicji klasy zawsze można użyć słówka pass
class Przedmiot:
    pass

print("dalszy kod")