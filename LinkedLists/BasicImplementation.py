# Basic Implementation of linked lists
# https://medium.com/@kojinoshiba/data-structures-in-python-series-1-linked-lists-d9f848537b4d
# https://www.youtube.com/watch?v=JlMyYuY1aXU&t=304s&ab_channel=BrianFaure
class Node:
	def __init__(self, val=None):
		self.val = val
		self.next = None  # the pointer initially points to nothing


class LinkedList:
	def __init__(self):
		self.head = Node()

	def append(self, val):
		new_node = Node(val)
		current_node = self.head
		while current_node.next is not None:
			current_node = current_node.next
		current_node.next = new_node

	def length(self):
		current_node = self.head
		idx = 0
		while current_node.next is not None:
			idx += 1
			current_node = current_node.next
		return idx

	def display(self):
		current_node = self.head
		elements = []
		while current_node.next is not None:
			current_node = current_node.next
			elements.append(current_node.val)
			elements.append("-->")
		print(elements)

	def get(self, index):
		current_node = self.head
		current_index = 0
		if index >= self.length():
			print("Index exceeds the length of Linked List")
			return None
		elif index < 0:
			print("Please enter non-negative indices")
			return None

		while True:
			if index == current_index:
				return current_node.val
			else:
				current_node = current_node.next
				current_index += 1

	def erase(self, index):
		if index >= self.length():
			print("Error--> out-of-bounds")
		current_idx = 0
		current_node = self.head
		while True:
			last_node = current_node
			current_node = current_node.next
			if index == current_idx:
				last_node.next = current_node.next
				return
			current_idx += 1


	def nth_from_end(self, n):
		#https://www.udemy.com/course/11-essential-coding-interview-questions/learn/lecture/7627022#overview

		pointer_one = self.head
		pointer_two = self.head

		# Move pointer two towards the end
		for ii in range(n):
			if pointer_two.next is not None:
				pointer_two = pointer_two.next
			else:
				return None

		# Move both pointers one by one
		while pointer_two.next is not None:
			pointer_two = pointer_two.next
			pointer_one = pointer_one.next
		return pointer_one.val




my_ll = LinkedList()

my_ll.display()

my_ll.append(1)
my_ll.append(2)
my_ll.append(3)
my_ll.append(4)
my_ll.display()
# print(my_ll.get(2))
# my_ll.erase(2)
# my_ll.display()
print(my_ll.nth_from_end(0))

