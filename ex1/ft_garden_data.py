class Plant:
	def show(self):
		print(self.name + ": " + str(self.height) + "cm, " + str(self.age) + " days old")

print("=== Garden Plant Registry ===")
rose = Plant()

rose.name = "Rose"
rose.height = 25
rose.age = 30

sunflower = Plant()

sunflower.name = "Sunflower"
sunflower.height = 80
sunflower.age = 45

cactus = Plant()

cactus.name = "Cactus"
cactus.height = 15
cactus.age = 120

rose.show()
sunflower.show()
cactus.show()
