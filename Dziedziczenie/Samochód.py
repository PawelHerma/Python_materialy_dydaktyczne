from Pojazd import Pojazd

# tworzymy klasę podrzędną, która dziedziczy metody z klasy nadrzędnej
class Samochód(Pojazd):
    pass # nie nadpisujemy żadnych metod ani nie tworzymy nowych

samochód1 = Samochód("Fiat", "Punto")

print(samochód1)