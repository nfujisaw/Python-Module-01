class Plant:
    def __init__(self, name ,height, age_days):
        self.name = name
        self.height = height
        self.age_days = age_days
    def show(self):
        print(self.name + ": " + format(round(self.height, 1)) + "cm, " + str(self.age_days) + " days old")

rose = Plant("Rose", 25.0, 30)
oak =  Plant("Oak", 200.0, 365)
cactus = Plant("Cactus", 5.0, 90)
sunflower = Plant("Sunflower", 80.0, 45)
fern = Plant("Fern", 15.0, 120)

print("=== Plant Factory Output ===")
print("Created:", end=" ")
rose.show()
print("Created:", end=" ")
oak.show()
print("Created:", end=" ")
cactus.show()
print("Created:", end=" ")
sunflower.show()
print("Created:", end=" ")
fern.show()