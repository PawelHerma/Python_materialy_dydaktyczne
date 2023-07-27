# funkcje mogą wykonywać czynności i/lub zwracać pewną wartość

# podział funkcji ze względu na wykonywane czynności

# deklaracja funkcji wykonującej pewne działanie
def nazwa_funkcji():
    print("Działanie funckji")

# wywołanie funkcji
nazwa_funkcji()

# deklaracja funkcji która będzie zwacać wartość
def nazwa_funkcji():
    return "Wartość funkcji"

wartość = nazwa_funkcji() # funkcja zwraca wartość którą możemy przypisać do zmiennej

print(wartość)

# podział funkcji ze względu na przyjmowany parametr

# funkcja bez parametru
def przywitaj_się():
    print("Cześć")

przywitaj_się()

# funkcja z parametrem
def powiedz(słowo):
    print(słowo)

powiedz("Witaj!")

# funkcja z nieznaną ilością podawanych parametrów/argumentów
def przedstaw(*osoby):
    for osoba in osoby:
        print(f"To jest {osoba}")

przedstaw("Roksana", "Paweł", "Przemek")

# kluczowy argument
def powiedz(imie, nazwisko):
    print(f"To jest {imie} {nazwisko}")

powiedz("Paweł", "Herma") # musimy się trzymać kolejności podawanych argumentów

powiedz(nazwisko = "Herma", imie = "Paweł") # argumenty są od razu ustawiane, kolejność nie ma znaczenia

# wartość domyślna parametru

def pojazd(ilość_kół = 4):
    print(f"Ten pojazd ma {ilość_kół} kół/koła")

pojazd(6)

pojazd() # funkcja przyjmie podany wcześniej domyślny argument

# a co jeśli zadeklarujemy funkcję ale jeszcze nie wiemy co w niej będzie?

def funkcja():
    pass

# rekurencja

def fibonacci(n):
    if n < 0:
        print("Podano złe dane!")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) # funkcja wywołuje samą siebie wewnątrz

print(fibonacci(7))