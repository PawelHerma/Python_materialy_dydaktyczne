# str - najbardziej złożony typ danych nie licząc tabel

# formy zapisu stringa:  "Cześć" lub 'Cześć'

print("Cześć")
print('Cześć')

# przypisywanie stringa do zmiennej

slowo = "Tabularaza"
print(slowo)

# ciągi znaków wielowierszowe

# wykorzystanie znaku ucieczki
wiersz = "Lorem ipsum dolor sit amet, \nconsectetur adipiscing elit, \nsed do eiusmod tempor incididunt \nut labore et dolore magna aliqua."
print(wiersz)

# potrójny cudzysłów
wiersz = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(wiersz)

# potrójny apostrof
wiersz = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(wiersz)

# stringi działają jak tablice

# każdy znak w stringu ma przydzielony index np. tekst[0] = "A", tekst[1] = "l" itd.
tekst = "Ala ma kota"
print(tekst[4]) # wypisze się "m"

# podanie ilości znaków w ciągu - len()
tekst = "Ala ma kota"
dlugosc = len(tekst)
print(dlugosc)

# sprawdzenie czy w ciągu występuje jakiś inny ciąg znaków (jakieś słowo)
wiersz = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print("dolor" in wiersz) # zwraca nam wartość logiczną True/False

# sprawdzenie czy w ciągu NIE występuje jakiś inny ciąg znaków
print("Pawel" not in wiersz)

# przycinanie ciągów znaków
tekst = "Ala ma kota"

# ucinamy Alę
print(tekst[4:]) # od elementu do końca

# ucinamy kota
print(tekst[:7]) # od początku do elementu

# ucinamy i Alę i kota
print(tekst[4:7])

# wszystko na duże litery
print(tekst.upper())

# wszystko z malej litery
print(tekst.lower())

# zamiana znaków w ciągu
print(tekst.replace("Ala", "Jacek"))

# rozdzielić zdanie na słowa
print(tekst.split(" ")) # w nawiasie zapisujemy "rozdzielacz"

# łączenie słów
imie = "Grzegorz"
nazwisko = "Brzęczyszczykiewicz"

godnosc = imie + " " + nazwisko
print(godnosc)

# łączenie ciągów znaków z liczbami - metoda format()
imie = "Paweł" # str
wiek = 23 # int

# sposób pierwszy - jedno przypisanie
przedstawienie1 = "Cześć, mam na imię " + imie + ", mam {} lata"
print(przedstawienie1.format(wiek))

# sposób drugi - wiele zmiennych
przedstawienie2 = "To jest {}. {} ma {} lata"
print(przedstawienie2.format(imie, imie, wiek))

# sposób trzeci - indexowanie zmiennych
przedstawienie3 = "To jest {0}. {0} ma {1} lata"
print(przedstawienie3.format(imie, wiek))