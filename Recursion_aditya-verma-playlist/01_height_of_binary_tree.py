"""
Video link-->https://www.youtube.com/watch?v=aqLTbtWh40E&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=5&ab_channel=AdityaVermaAdityaVerma


"""

class Node:
	def __init__(self, data=None):
		self.data = data
		self.right = None
		self.left = None

	def height(self, root):
		if root is None:
			return 0
		return 1 + max(self.height(root.left), self.height(root.right))


# driver code
tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)

print(tree.height(tree))