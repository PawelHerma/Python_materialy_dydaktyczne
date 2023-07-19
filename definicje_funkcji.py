#definicja funkcji

def dodaj():
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    wynik = a + b
    print(wynik)

#wywołanie funkcji

dodaj()

#funkcja z parametrem - musi zwracać wartość

def dodaj(a, b):
    print(a + b)

liczba1 = int(input("Podaj liczbę1: "))
liczba2 = int(input("Podaj liczbę2: "))
dodaj(liczba1, liczba2) 

