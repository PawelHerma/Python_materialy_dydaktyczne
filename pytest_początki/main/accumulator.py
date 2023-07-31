class Accumulator:
    def __init__(self) -> None:
        self._count = 0 # prywatna zmienna _count
    
    @property # dzięki temu użytkownik nie może stworzyć obiektu klasy Accumulator i ustawić wartości, może jedynie sprawdzić tą wartość albo coś do niej dodać
    def count(self) -> int:
        return self._count
    
    def add(self, more = 1) -> None: # domyślna wartość dodawania to 1
        self._count += more