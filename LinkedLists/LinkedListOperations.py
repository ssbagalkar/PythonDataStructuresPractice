class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next
	
	def insert_after(self, node, new_node):
		new_node.next = node.next
		node.next = new_node
	
	def delete_after(self, node):
		node.next = node.next.next
	
	

# head = ListNode()
# first = ListNode(1)
# second = ListNode(2)
#
# head.next = first
# first.next = second
#
# third = ListNode(3)
# second.insert_after(first, third)
def merge_two_sorted_lists(L1, L2):
	dummy_head = tail = ListNode()
	
	while L1 and L2:
		if L1.data < L2.data:
			tail.next = L1
			L1 = L1.next
		else:
			tail.next = L2
			L2 = L2.next
		tail = tail.next
	
	# Append remaining nodes
	tail.next = L1 or L2
	return dummy_head.next


L1 = ListNode(1)
L1_two = ListNode(5)
L1_three = ListNode(7)

L2 = ListNode(3)
L2_two = ListNode(11)

L1.next = L1_two
L1_two.next = L1_three

L2.next = L2_two
head = merge_two_sorted_lists(L1,L2)

def linked_list_to_string(head):
	str_list = []
	current = head
	while current != None:
		str_list.append(str(current.data))
		current = current.next
	str_list.append('(None)')
	return '->'.join(str_list)


print(linked_list_to_string(head))