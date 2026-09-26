class Plant:
	def grow(self):
		self.height += 0.8
	def age(self):
		self.age_days += 1
	def show(self):
		print(self.name + ": " + format(round(self.height, 1)) + "cm, " + str(self.age_days) + " days old")

rose = Plant()
rose.name = "Rose"
rose.height = 25.0
rose.age_days = 30

initial_height = rose.height

print("=== Garden Plant Growth ===")
rose.show()

for day in range(1, 8):
	rose.grow()
	rose.age()
	print("=== Day", day, "===")
	rose.show()

print("Growth this week:", round(rose.height - initial_height, 1),"cm")
