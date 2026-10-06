class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(self.name + ": " + str(self.height) + "cm, "
              + str(self.age) + " days old")


print("=== Garden Plant Registry ===")
rose = Plant("Rose", 25.0, 30)

sunflower = Plant("Sunflower", 80, 45)

cactus = Plant("Cactus", 15, 120)

rose.show()
sunflower.show()
cactus.show()
