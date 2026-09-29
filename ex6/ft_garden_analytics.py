class Plant:
	def __init__(self, name ,height, age_days):
		self.name = name
		self._height = height
		self._age_days = age_days
		self._statistics = Plant.statistics()
	def	grow(self):
		self._height += 0.8
		self._statistics.increment_grow_count()
	def	age(self):
		self._age_days += 1
		self._statistics.increment_age_count()
	def show(self):
		print(self.name + ": " + format(round(self._height, 1)) + "cm, " + str(self._age_days) + " days old")
		self._statistics.increment_show_count()
	@staticmethod
		def is_older_than_year():
	@classmethod
		def creat_anonumous():
	class Statistics:
		def __init__(self):
			self._grow_count = 0
			self._age_count = 0
			self._show_count = 0
		def increment_grow_count(self):
			self._grow_count += 1
		def increment_age_count(self):
			self._age_count += 1
		def increment_show_count(self):
			self._show_count += 1
		def display(self):
			print("stats:", self._grow_count, "grow", self._age_count, "age", self._show_count, "show")

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


class Seed(Flower):
	def __init__(self, name, height, age, color, bloom, show):
		super().__init__(name, height, age, color,bloom, show)
		self.seeds = 

def display_statistics():