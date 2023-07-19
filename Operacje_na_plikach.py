# operacje na plikach

# tryby otwierania pliku
# r - plik do odczytu
# a - plik do dołączania
# w - plik do zapisu
# x - utwórz plik

# określenie typu danych w pliku
# t - tekstowy
# b - binarny

# otwieranie pliku do odczytu
plik = open("plik.txt")
# alternatywy
plik = open("plik.txt", "r")
plik = open("plik.txt", "rt")

print(plik.read(3)) # odczytywanie tylko tylu znaków ile podaliśmy
print(plik.readline()) # odczytywanie pojedynczej linii tekstu z pliku
print(plik.read()) # odczytywanie pełnej zawartości pliku
print()

plik = open("plik.txt")
for x in plik:
    print(x)

# UWAGA pamiętać o zamykaniu plików
plik.close()

# pliki do dodawania vs do zapisu
# plik w trybie "w" usuwa wcześniejsze dane i pisze nowe
plik = open("wyniki.txt", "wt")
plik.write("Wynik to 2 \n")
plik.close()

plik = open("wyniki.txt", "wt")
plik.write("Wynik to 3 \n")
plik.close()

# plik w trybie "a" dopisuje dodatkowe dane bez usuwania poprzednich danych
plik = open("wyniki.txt", "at")
plik.write("Wynik to 2 \n")
plik.close()

plik = open("wyniki.txt", "at")
plik.write("Wynik to 3 \n")
plik.close()

# usuwanie plików - zazwyczaj wykorzystywane na początku kodu
import os
os.remove("wyniki.txt")

# tworzenie folderów
os.mkdir("pliki")

# usuwanie folderów
os.rmdir("pliki")