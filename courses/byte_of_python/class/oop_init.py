class Person:
	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print("Hello, my name is", self.name)

p = Person("Rahul")
p.say_hi()

# The previous two lines can also be written as Parent("Rahul").say_hi()
