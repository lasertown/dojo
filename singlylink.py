#!/usr/bin/python

class node(object):
	def __init__(self,value):
		#self.prev = prev
		self.value = value
		self.next = None

class single_linked_list(object):
	def __init__(self):
		self.head = None
		#self.tail = None

	def traverse(self):
		print "Traversing..."
		if self.head != None:
			current_node = self.head
			print current_node.value
			while current_node.next != None:
				current_node = current_node.next
				print current_node.value
		else:
			print "NO OTHER NODES"
			return False

	def add_node(self, val):
		#creating new node from class node(object)
		new_node = node(val)
		# if there are no nodes yet set the head attribute to our new node
		if self.head == None:
			self.head = new_node
			# else we will have to traverse to the last node in the chain and
			#add our new node to the end
			print "NEW HEAD"
		else:
			current_node = self.head
			while current_node.next != None:
				current_node = current_node.next
			current_node.next = new_node
			print "ADDING NODE %s" %current_node.value
	
	def remove_node(self,search_val):
		search_node_val = search_val
		# this method prints the values of of all the nodes in the list
		print "Remove Node..."
		if self.head != None:
			# we will initialize our current node as the head node
			current_node = self.head
			#print the value of the head node
			print "Initial Node Value: %s" %current_node.value
			# this while loop moves us forward through the linked list
			temp_next = current_node.next
			while  temp_next != None:
				if current_node.value == search_node_val:
					prev_node.next = current_node.next
					temp_next = None
					print "###Removed Node###"
				else:
					print "DID NOT FIND NODE"	
				print "Current Node Value: %s" %current_node.value
				print "Search Value: %s" %search_node_val
				prev_node = current_node
				current_node = current_node.next
		# in the case that there are no nodes
		else:
			print "No nodes"
			return False	
			
	def print_as_list(self):
		print "Printing..."
		print_node_arr = []
		if self.head != None:
			current_node = self.head
			while current_node.next != None:
				current_node = current_node.next
				print_node_arr.append(current_node)
			print print_node_arr
		else:
			print "NO OTHER NODES"
			return False

#PAIR PROGRAMMING SECTION START	
	def insert_node_after(self,search_val,insert_val):
		search_node_val = search_val
		insert_new_node = node(insert_val)
		# this method prints the values of of all the nodes in the list
		print "Inserting Node..."
		if self.head != None:
			# we will initialize our current node as the head node
			current_node = self.head
			#print the value of the head node
			print "Initial Node Value: %s" %current_node.value
			# this while loop moves us forward through the linked list
			temp_next = current_node.next
			while  temp_next != None:
				if current_node.value == search_node_val:
					insert_new_node.next = current_node.next
					current_node.next = insert_new_node
					temp_next = None
					print "###Inserted Node###"
				else:
					print "DID NOT FIND NODE"	
				print "Current Node Value: %s" %current_node.value
				print "Search Value: %s" %search_node_val
				current_node = current_node.next	
		# in the case that there are no nodes
		else:
			print "No nodes"
			return False

	def remove_node_after(self,search_val):
		search_node_val = search_val
		# this method prints the values of of all the nodes in the list
		print "Remove Node..."
		if self.head != None:
			# we will initialize our current node as the head node
			current_node = self.head
			#print the value of the head node
			print "Initial Node Value: %s" %current_node.value
			# this while loop moves us forward through the linked list
			temp_next = current_node.next
			while  temp_next != None:
				if current_node.value == search_node_val:
					fwd_node = current_node.next
					current_node.next = fwd_node.next
					temp_next = None
					print "###Removed Node###"
				else:
					print "DID NOT FIND NODE"	
				print "Current Node Value: %s" %current_node.value
				print "Search Value: %s" %search_node_val
				fwd_node = current_node
				current_node = current_node.next
		# in the case that there are no nodes
		else:
			print "No nodes"
			return False	

	def find_value(self,search_val):
		search_node_val = search_val
		# this method prints the values of of all the nodes in the list
		print "Finding Node..."
		if self.head != None:
			# we will initialize our current node as the head node
			current_node = self.head
			#print the value of the head node
			print "Initial Node Value: %s" %current_node.value
			# this while loop moves us forward through the linked list
			temp_next = current_node.next
			while  temp_next != None:
				if current_node.value == search_node_val:
					temp_next = None	
					print "###Found Node### %s" %current_node.value
				else:
					print "DID NOT FIND NODE"	
				print "Current Node Value: %s" %current_node.value
				print "Search Value: %s" %search_node_val
				prev_node = current_node
				current_node = current_node.next
		# in the case that there are no nodes
		else:
			print "No nodes"
			return False		
				

#PAIR PROGRAMMING END			

sll = single_linked_list()

for i in range(1,6+1):
	#Creating new nodes
	sll.add_node(i)
	#Going through and checking if the current node it NOT EQUAL to none
	#If the 
	#sll.remove_node()

#sll.insert_node_after(3,4)
sll.remove_node_after(3)
#sll.find_value(3)
sll.traverse()
#sll.print_as_list()
