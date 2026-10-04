class Plant:
    def __init__(self, name, height, age_days):
        self.name = name
        self._height = height
        self._age_days = age_days

    def set_height(self, height):
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height

    def set_age(self, age_days):
        if age_days < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age_days = age_days

    def get_height(self):
        return (self._height)

    def get_age(self):
        return (self._age_days)

    def show(self):
        print(f"{self.name}: {round(self._height, 1)}cm, "
              f"{self._age_days} days old")


rose = Plant("Rose", 15.0, 10)

print("=== Garden Security System ===")
print("Plant created:", end=" ")
rose.show()

print()

rose.set_height(25.0)
rose.set_age(30)

print("Height updated:", str(rose.get_height()) + "cm")
print("Age updated:", rose.get_age(), "days")

print()

rose.set_height(-10)
rose.set_age(-5)

print()

print("Current state:", end=" ")
rose.show()
