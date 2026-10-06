class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.age_days += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, "
              f"{self.age_days} days old")


rose = Plant("Rose", 25.0, 30)

initial_height = rose.height

print("=== Garden Plant Growth ===")
rose.show()

for day in range(1, 8):
    rose.grow()
    rose.age()
    print("=== Day", day, "===")
    rose.show()

print("Growth this week:", round(rose.height - initial_height, 1), "cm")
