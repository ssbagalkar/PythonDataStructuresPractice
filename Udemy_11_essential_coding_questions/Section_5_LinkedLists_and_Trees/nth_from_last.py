class ListNode():
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next


head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)
fifth = ListNode(5)
sixth = ListNode(6)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth


def linked_list_to_string(head):
	str_list = []
	current = head
	while current != None:
		str_list.append(str(current.data))
		current = current.next
	str_list.append('(None)')
	return '->'.join(str_list)


def nth_from_end(head, n):
	pointer_one = head
	pointer_two = head
	
	for ii in range(n):
		if pointer_two:
			pointer_two = pointer_two.next
		else:
			return None
	
	if pointer_two != None:
		# Move both pointers one by one to right
		while (pointer_two):
			pointer_one = pointer_one.next
			pointer_two = pointer_two.next
		
		return pointer_one.data
	


print(nth_from_end(head, 2))