# Zadanie 2:
# Utwórz w nim klasę o dowolnej, sensownej nazwie. Klasa powinna zawierać pole counter, możliwe do ustawienia dla każdej instancji przy tworzeniu obiektu (jako argument w funkcji __init__()).
# Klasa powinna implementować bezargumentową metodę raise_counter(), która zwiększa pole counter w obiekcie o jeden.
# W script02.py napisz funkcję (nie metodę) przyjmującą dwa argumenty. Wewnątrz funkcji stwórz obiekt klasy utworzonej w punkcie drugim, o początkowej wartości pola counter równej pierwszemu argumentowi funkcji. W funkcji podnieś counter obiektu do wysokości wartości drugiego argumentu funkcji, przez wielokrotne wywołanie metody raise_counter. Po każdym wywołaniu metody raise_counter wyprintuj wartość pola counter dla obiektu. Zastosuj do tego odpowiednią pętlę. Dla uproszczenia możemy założyć, że argumenty funkcji są zawsze liczbowe i pierwszy jest zawsze co najmniej o jeden mniejszy od drugiego.


class Herd:
    def __init__(self, counter):
        self.counter = counter

    def raise_counter(self):
        self.counter += 1


def count_sheep(x, y):
    sheep = Herd(x)
    while sheep.counter < y:
        sheep.raise_counter()
        print(sheep.counter)

count_sheep(1, 5)

