# włączenie testu w terminalu "python -m pytest"
import pytest

# definicja testu
def test_one_plus_one():
    assert 1 + 1 == 2 # sprawdzenie czy 1 plus 1 to 2


# test błędny
def test_one_plus_two():
    a = 1
    b = 2
    c = 0
    assert a + b == c

# test z wyjątkami
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert "division by zero" in str(e.value) # sprawdzenie czy test wywołuje błąd dzielenia przez zero
    # test będzie pozytywny

# testy parametryzowane

# tabela przypadków testowych
test_cases = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 90, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75)
]

@pytest.mark.parametrize("a, b, result", test_cases)
def test_multiplication(a, b, result):
    assert a * b == result

# napisaliśmy 4 testy, wykonało się 9 testów
# .F.......