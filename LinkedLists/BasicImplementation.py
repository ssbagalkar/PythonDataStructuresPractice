# Basic Implementation of linked lists
#https://medium.com/@kojinoshiba/data-structures-in-python-series-1-linked-lists-d9f848537b4d
class Node:
def __init__(self,val):
	self.val = val
	self.next = None # the pointer initially points to nothing
	

node1 = Node(12)
node2 = Node(99)
node3 = Node(37)

node1.next = node2 # 12->99
node2.next = node3 # 99->37