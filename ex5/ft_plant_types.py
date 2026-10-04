class Plant:
    def __init__(self, name, height, age_days):
        self.name = name
        self._height = height
        self._age_days = age_days

    def grow(self):
        self._height += 0.8

    def age(self):
        self._age_days += 1

    def show(self):
        print(f"{self.name}: {round(self._height, 1)}cm, "
              f"{self._age_days} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print("Color:", self.color)
        if self.bloomed:
            print(self.name, "is blooming beautifully!")
        else:
            print(self.name, "has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print("Tree", self.name, "now produces a shade of", self._height,
              "cm long and", self.trunk_diameter, "cm wide")

    def show(self):
        super().show()
        print("Trunk diameter:", str(self.trunk_diameter) + "cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self):
        super().grow()

    def age(self):
        super().age()
        self.nutritional_value += 1

    def show(self):
        super().show()
        print("Harvest season:", self.harvest_season)
        print("Nutritional value:", self.nutritional_value)


print("=== Garden Plant Types ===")
print("=== Flower")
rose = Flower("Rose", 15.0, 10, "red")
rose.show()
print("[asking the rose to bloom]")
rose.bloom()
rose.show()
print()

print("=== Tree")
oak = Tree("Oak", 200.0, 365, 5.0)
oak.show()
print("[asking the oak to produce shade]")
oak.produce_shade()
print()

print("=== Vegetable")
tomato = Vegetable("Tomato", 5.0, 10, "April")
tomato.show()
print("[make tomato grow and age for 20 days]")
for day in range(20):
    tomato.grow()
    tomato.age()
tomato.show()
