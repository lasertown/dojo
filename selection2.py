#!/usr/bin/python

from random import randint

x = 1
arr = []

while x <= 10000:
	arr.append(randint(0, 10000))
	x += 1

for max_position in range(len(arr)-1, 0, -1):
	max_index = 0
	min_index = 0
	min_position = 0
	for position in range(1, max_position + 1):
		if arr[position] > arr[max_index]:
			max_index = position
		elif arr[position] < arr[min_index]:
			min_index = position
	(arr[max_index], arr[max_position]) = (arr[max_position], arr[max_index])
	(arr[min_index], arr[min_position]) = (arr[min_position], arr[min_index])
	min_position += 1
	if max_position == min_position:
		break
	break

print arr
