def silnia_r(n):
    if n > 1:
        return n*silnia_r(n-1)
    else:
        return 1                   #podobno 0!=1


def silnia_i(n):
    Silnia = 1
    if n <= 1:
        return 1
    else:
        for x in range(2, n+1):
            Silnia *= x
        return Silnia


def słabnia_r(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return n + słabnia_r(n-1)

def słabnia_i(n):
    Słabnia = 0
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range(1, n+1):
            Słabnia += i
        return Słabnia
