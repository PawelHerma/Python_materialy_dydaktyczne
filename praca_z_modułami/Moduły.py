import Metody

print(Metody.słabnia_r(5)) # wywołanie metody z innego pliku
print(Metody.silnia_r(5))

# importowanie tylko jednej metody

from Metody import silnia_i

print(silnia_i(6))

# importowanie zmiennych, tablic z innych modułów

import Tablice

print(Tablice.goście)
print(Tablice.goście[2])

from Tablice import osoba1

print(osoba1)
print(osoba1["wiek"])

# podczas importowania modułu możemy zmienić jego nazwę lokalną

import Metody as m

print(m.silnia_r(7))

# wypisanie listy wszystkich dostępnych metod z danego modułu

import math

lista_metod = dir(math)
print(lista_metod)

