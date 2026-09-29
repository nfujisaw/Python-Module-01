class Plant:
	def __init__(self, name ,height, age_days):
		self.name = name
		self._height = height
		self._age_days = age_days
	def	grow(self):
		self._height += 0.8
	def	age(self):
		self._age_days += 1
	def show(self):
		print(self.name + ": " + format(round(self._height, 1)) + "cm, " + str(self._age_days) + " days old")


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
		if	self.bloomed:
			print(self.name, "is blooming beautifully!")
		else:
			print(self.name, "has not bloomed yet")

class Tree(Plant):
	def __init__(self, name, height, age, trunk_diameter):
		super().__init__(name, height, age)
		self.trunk_diameter = trunk_diameter
	def produce_shade(self):
		print("Tree", self.name, "now produces a shade of", self._height, "cm long and", self.trunk_diameter,"cm wide")
	def show(self):
		super().show()
		print("Trunk diameter:", str(self.trunk_diameter) + "cm")


class Seed(Flower)
