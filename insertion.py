#!/usr/bin/python

from random import randint

x = 1
arr = []

while x <= 100:
	arr.append(randint(0, 10000))
	x += 1

for mark in range(1,len(arr)):
	star = arr[mark]
	while mark > 0 and star < arr[mark-1]:
		arr[mark]=arr[mark-1]
		mark = mark-1
 	arr[mark]=star

print arr
