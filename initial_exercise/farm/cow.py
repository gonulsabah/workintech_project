from farm.animal import Animal

class Cow(Animal):
    def __init__(self):
        super().__init__()
        self.milk = 0

    def talk(self):
        return "moo"

    def feed(self):
        super().feed()
        self.milk += 2
