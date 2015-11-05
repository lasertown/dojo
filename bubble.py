#!/usr/bin/python

from random import randint

x = 1
y = []

while x <= 100:
	y.append(randint(0, 10000))
	x += 1

for i in range(len(y)-1,0,-1):
	for z in range(i):
		if y[z] > y[z + 1]:
			(y[z], y[z+1]) = (y[z + 1], y[z])

print y
