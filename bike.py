#!/usr/bin/python

class bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def displayinfo(self):
		print "Price:", self.price
		print "Max Speed:", self.max_speed
		print "Miles:", self.miles

	def ride(self, x):
		print "Riding"
		self.miles += 10 * x

	def reverse(self, x):
		print "Reversing"
		self.miles -= 5 * x
		if self.miles < 0:
			self.miles = 0
					
bike1 = bike(5, 25)
bike2 = bike(5, 25)
bike3 = bike(5, 25)

bike1.ride(3)
bike1.displayinfo()

bike2.ride(2)
bike2.displayinfo()

bike3.reverse(3)
bike3.displayinfo()
