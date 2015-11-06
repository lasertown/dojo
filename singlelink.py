#!/usr/bin/python

class Node(object):
	def __init__(self, data, next):
		self.data = data
		self.next = next

class SingleLink(object):
	head = None
	tail = None

	def add(self, data):
		node = Node(data, None)
		if self.head == None:
			self.head = node
		else:
			self.tail.next = node
		self.tail = node
	def list(self):
		node = self.head
		while node != None:
			print node.data
			node = node.next
	def remove(self, node_data):
		node = self.head
		previous_node = None
		while node != None:
			if node_data == node.data:
				if previous_node != None:
					previous_node.next = node.next
				else:
					self.head = node.next
			previous_node = node
			node = node.next

sl = SingleLink()
sl.add(5)
sl.add(8)
sl.add(82)
sl.add(39)
sl.list()
sl.remove(82)
sl.list()
sl.remove(8)
sl.list()
