#!/usr/bin/python

class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def displayHealth(self):
		print "Name:", self.name
		print "Health:", self.health
		return self

class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health = 150


	def pet(self):
		self.health += 5
		return self

class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health = 170

	def fly(self):
		self.health -= 10
		return self

	def displayHealth(self):
		print "this is a dragon!"
		super(Dragon, self).displayHealth()
		return self

animal = Animal("animal")
animal.walk().walk().walk().run().run().displayHealth()

spot = Dog("spot")
spot.walk().walk().walk().run().run().pet().displayHealth()

sparky = Dragon("sparky")
sparky.walk().walk().walk().run().run().fly().fly().displayHealth()
