# Basic Implementation from GeeksForGeeks

# Node class
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# LinkedList class
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None


if __name__ == 'main':

    # Start with empty linked list
    lList = LinkedList()
    lList.head = Node(1)
    second = Node(2)
    third = Node(3)

    # We have created 3 nodes till now

    #  llist.head        second              third
    #      |                |                  |
    #      |                |                  |
    # +----+------+     +----+------+     +----+------+
    # | 1  | None |     | 2  | None |     |  3 | None |
    # +----+------+     +----+------+     +----+------+

    lList.head.next = second  # Link first node with second
    second.next = third  # Link second node to third

'''
  Now next of second Node refers to third.  So all three
  nodes are linked.

  llist.head        second              third
       |                |                  |
       |                |                  |
  +----+------+     +----+------+     +----+------+
  | 1  |  o-------->| 2  |  o-------->|  3 | null |
  +----+------+     +----+------+     +----+------+
  '''