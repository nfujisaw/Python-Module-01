class Plant:
    def __init__(self, name, height, age_days):
        self.name = name
        self._height = height
        self._age_days = age_days
        self._statistics = Plant.Statistics()

    def grow(self):
        self._height += 0.8
        self._statistics.increment_grow_count()

    def age(self):
        self._age_days += 1
        self._statistics.increment_age_count()

    def show(self):
        print(f"{self.name}: {round(self._height, 1)}cm, "
              f"{self._age_days} days old")
        self._statistics.increment_show_count()

    @staticmethod
    def is_older_than_year(age):
        if age > 365:
            return True
        else:
            return False

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    class Statistics:
        def __init__(self):
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0
            self._shade_count = 0

        def increment_grow_count(self):
            self._grow_count += 1

        def increment_age_count(self):
            self._age_count += 1

        def increment_show_count(self):
            self._show_count += 1

        def increment_shade_count(self):
            self._shade_count += 1

        def display(self):
            print("Stats:", self._grow_count, "grow" + str(","),
                  self._age_count, "age" + str(","), self._show_count, "show")

        def display_shade_count(self):
            print(self._shade_count, "shade")


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
        self._statistics.increment_shade_count()

    def show(self):
        super().show()
        print("Trunk diameter:", str(self.trunk_diameter) + "cm")


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print("Seeds:", self.seeds)


def display_statistics(plant):
    plant._statistics.display()

    if isinstance(plant, Tree):
        plant._statistics.display_shade_count()


print("=== Garden statistics ===")
print("=== Check year-old")
print("Is 30 days more than a year? -> False")
print("Is 400 days more than a year? -> True")
print()

print("=== Flower")
rose = Flower("Rose", 15, 10, "red")
rose.show()
print("[statistics for Rose]")
display_statistics(rose)
print("[asking the rose to grow and bloom]")
rose.grow()
rose.bloom()
rose.show()
print("[statistics for Rose]")
display_statistics(rose)
print()

print("=== Tree")
oak = Tree("Oak", 200, 365, 5.0)
oak.show()
print("[statistics for Oak]")
display_statistics(oak)
print("[asking the oak to produce shade]")
oak.produce_shade()
print("[statistics for Oak]")
display_statistics(oak)
print()

print("=== Seed")
sunflower = Seed("Sunflower", 80.0, 45, "yellow")
sunflower.show()
print("[make sunflower grow, age and bloom]")
sunflower.grow()
sunflower.age()
sunflower.bloom()
sunflower.show()
print("[statistics for Sunflower]")
display_statistics(sunflower)
print()

print("=== Anonymous")
anonymous = Plant.create_anonymous()
anonymous.show()
display_statistics(anonymous)
