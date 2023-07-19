# warunki matematyczne
# równość - a == b
# nierównośc - a != b
# mniejsze od - a < b
# większe do - a > b
# mniejsze lub równe - a <= b
# większe lub równe - a >= b

# warunki logiczne
# if zmienna is
# if zmienna is not

# deklaracja warunku

a = 5
b = 5

if a == b:
    print("liczby są takie same")

if a < b:
    print("a mniejsze od b")

# "w przeciwnym wypadku" - else

a = 3
b = 3

if a > b:
    print(f"{a} jest większe od {b}") # alternatywne formatowanie
else:
    print(f"{b} jest większe lub równe {a}")

# więcej alternatywnych wyjść - elif (skrót od else if)

a = 2
b = 2

if a > b:
    print(f"{a} jest większe od {b}") # alternatywne formatowanie
elif a < b:
    print(f"{a} jest mniejsze od {b}")
else:
    print(f"{a} jest takie samo jak {b}")

# wiele warunków do spełnienia jednocześnie

miesiąc = ["styczeń", 33]

if miesiąc[0] == "styczeń" and miesiąc[1] <= 31:
    print("podane informacje są prawidłowe")
else:
    print("dane są niepoprawne")

# warunek alternatywny

a = 5
b = 3
c = 9

if a > b or a > c:
    print(f"{a} jest większe od {b} albo od {c}")


p = True
q = False

if p and q:
    print(True)
else:
    print(False)

if p or q:
    print(True)
else:
    print(False)

a = 3
b = 5

if a > b:
    print("a > b")

if not a > b:
    print("a < b")

# przepuszczanie programu dalej jeśli jeszcze nie mamy gotowego ifa
# ignorowanie instrukcji

a = 1
b = 5

if a > b:
    pass # kod przepuszcza mimo wszystko
