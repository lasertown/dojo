#!/usr/bin/python

from random import randint

x = 1
arr = []

while x <= 10000:
	arr.append(randint(0, 10000))
	x += 1

for max_position in range(len(arr)-1, 0, -1):
	max_index = 0
	for position in range(1, max_position + 1):
		if arr[position] > arr[max_index]:
			max_index = position
	(arr[max_index], arr[max_position]) = (arr[max_position], arr[max_index])

print arr
