# https://afteracademy.com/blog/check-if-a-binary-tree-is-BST-or-not

class Node:
	def __init__(self, data=None):
		self.data = data
		self.left_child = None
		self.right_child = None


class BinaryTree:
	def __init__(self):
		self.root = None

	def check_if_bst(self):
		pass


def fill_tree(tree):
	elements = [10, 5, 3, 7, 15, 20]
	for el in elements:
		tree.insert(el)
	return tree


