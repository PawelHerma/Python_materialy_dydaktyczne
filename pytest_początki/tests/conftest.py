import pytest
from main.accumulator import Accumulator

# funkcja szuka fixture do parametru o tej samej nazwie
@pytest.fixture
def accum(scope = "function"):
    yield Accumulator() # przygotowanie
    print("Testy zakończone") # zakończenie