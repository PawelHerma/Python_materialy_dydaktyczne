import pytest

# test tworzenia nowego obiektu klasy
def test_accumulator_init(accum):
    assert accum.count == 0

# testy domyślnej wartości dodawanej
def test_accumulator_add_one(accum):
    accum.add()
    assert accum.count == 1

def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2

# test dodawania wartości do obiektu
def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3

# test sprawdzający czy możemy ustawić wartość count bez używania add()
def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match = "can't set attribute 'count'"):
        accum.count = 10