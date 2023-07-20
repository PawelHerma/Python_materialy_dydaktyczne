# pętla while - będzie się wykonywać "dopóki" określony warunek będzie prawdziwy

# while True:
#     print("Cześć")
# w przypaadku nieskończonej pętli użyć ctrl+c

# licznik/iterator
i = 0
while i < 10:
    print("Cześć")
    i += 1 # to samo co i = i + 1
print("Koniec")

# break - zatrzymuje wykonywanie pętli i wychodzi z niej
i = 0
while i < 10:
    if i == 5:
        print("Przerwanie")
        break
    print("Cześć")
    i += 1
print("Koniec")

# continue - zatrzymuje aktualną iterację i rozpoczyna kolejną
i = 0
while i < 10:
    print("Cześć")
    i += 1
    if i == 5:
        print("Przerwanie")
        continue
else: # opcjonalne
    print("Koniec")

# pętla for - bardziej elastyczna, ma więcej możliwości

imiona = ["Roksana", "Przemek", "Paweł"]
# wypisanie wszystkich elementów tablicy
print(imiona)
#iterator przechodzi przez każdy kolejny element tablicy
for imie in imiona:
    print(imie)

zdanie = "Letnia Akademia Programowania"
for litera in zdanie:
    print(litera)
print("Koniec")

# w pętlach for też możemy wykorzystać break i continue
imiona = ["Roksana", "Przemek", "Paweł"]
for imie in imiona:
    if imie == "Przemek":
        break
    print(imie)
print("Koniec")

imiona = ["Roksana", "Przemek", "Paweł"]
for imie in imiona:
    if imie == "Przemek":
        continue
    print(imie)
print("Koniec")

# range - my określamy pewien zasięg działania
for i in range(10):
    print(i)
print("Koniec")

for i in range(5, 10):
    print(i)
print("Koniec")

# regulacja przeskoku
for i in range(1, 20, 2):
    print(i)
print("Koniec")

#pętla w pętli
opisy = ["mały", "średni", "duży"]
owoce = ["arbuz", "ananas", "pomidor"]
# ważna jest kolejność
for owoc in owoce:
    for opis in opisy:
        print(f"To jest {opis} {owoc}")