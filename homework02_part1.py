# Zadanie 1:
# Utwórz klasę (o dowolnej, sensownej nazwie), która będzie implementowała metodę foo(), która będzie printować komunikat “Jestem w klasie nadrzędnej”.
# Utwórz dwie klasy podrzędne, dziedziczące po klasie z punktu 2. Jedną z nich nazwij dowolnie, drugą Liar. Liar przy wywołaniu foo() powinien printować komunikat “Jestem w klasie nadrzędnej”. Druga klasa ma pisać “Jestem w podklasie”.
# Utwórz po dwie instancję każdej z klas i na wszystkich po kolei wywołaj metodę foo(). Zastosuj do tego pętlę.


class Guard:
    def foo(self):
        print("Jestem w klasie nadrzędnej")


class Liar(Guard):
    pass


class Knight(Guard):
    def foo(self):
        print("Jestem w podklasie")


dudes = [Guard(), Liar(), Knight(), Liar(), Guard(), Knight()]
for dude in dudes:
    dude.foo()

