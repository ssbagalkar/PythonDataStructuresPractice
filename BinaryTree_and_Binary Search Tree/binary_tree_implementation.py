# https://www.youtube.com/watch?v=f5dU3xoE6ms&t=1s&ab_channel=BrianFaure

class Node:
	def __init__(self, data=None):
		self.data = data
		self.left_child = None
		self.right_child = None
		self.parent = None  # pointer to the parent node


class BinarySearchTree:
	def __init__(self):
		self.root = None

	def insert(self, value):
		if self.root is None:
			self.root = Node(value)
		else:
			self._insert(value, self.root)

	def _insert(self, value, current_node):
		if value < current_node.data:
			if current_node.left_child is None:
				current_node.left_child = Node(value)
				current_node.left_child.parent = current_node
			else:
				self._insert(value, current_node.left_child)
		elif value > current_node.data:
			if current_node.right_child is None:
				current_node.right_child = Node(value)
				current_node.right_child.parent = current_node
			else:
				self._insert(value, current_node.right_child)
		else:
			print("Value already in tree")

	def print_tree(self):
		if self.root is not None:
			self._print_tree(self.root)

	def _print_tree(self, current_node):
		if current_node is not None:
			self._print_tree(current_node.left_child)
			print(current_node.data)
			self._print_tree(current_node.right_child)

	def height(self):
		if self.root is not None:
			return self._height(self.root, 0)
		else:
			return 0

	def _height(self, current_node, current_height):
		if current_node is None:
			return current_height
		left_height = self._height(current_node.left_child, current_height + 1)
		right_height = self._height(current_node.right_child, current_height + 1)
		return max(left_height, right_height)

	def search(self, value):
		if self.root is None:
			return False
		else:
			return self._search(value, self.root)

	def _search(self, value, current_node):
		if current_node.data == value:
			return True
		elif value < current_node.data and current_node.left_child is not None:
			return self._search(value, current_node.left_child)
		elif value > current_node.data and current_node.right_child is not None:
			return self._search(value, current_node.right_child)
		return False

	# returns the node with specified input value
	def find(self, value):
		if self.root is None:
			return None
		return self._find(value, self.root)

	def _find(self, value, current_node):
		if value == current_node.data:
			return current_node
		elif value < current_node.data and current_node.left_child is not None:
			return self._find(value, current_node.left_child)
		elif value > current_node.data and current_node.right_child is not None:
			return self._find(value, current_node.right_child)

	def delete_value(self, value):
		return self.delete_node(self.find(value))

	def delete_node(self, node):

		# returns the node with min value in tree rooted at the input node
		def min_value_node(n):
			current = n
			while current.left_child is not None:
				current = current.left_child
			return current

		def num_children(n):
			num_child = 0
			if n.left_child is not None: num_child += 1
			if n.right_child is not None: num_child += 1
			return num_child

		# get parent of the node to be deleted
		node_parent = node.parent

		# get the number of children of the node to be deleted
		node_children = num_children(node)

		# break the operation into the 3 different cases as discussed in the video, based on
		# the structure of the tree and the node to be deleted

		# Case 1--> node has no children
		if node_children == 0:
			# remove reference to the node from the parent
			if node_parent.left_child == node:
				node_parent.left_child = None
			else:
				node_parent.right_child = None

		# Case 2 --> node has 1 child
		if node_children == 1:
			if node.left_child is not None:
				child = node.left_child
			else:
				child = node.right_child

			if node_parent.left_child == node:
				node_parent.left_child = child
			else:
				node_parent.right_child = child

			# correct the parent pointer in node
			child.parent = node_parent

		# Case 3
		if node_children == 2:
			# get the inorder successor of the deleted node
			successor = min_value_node(node.right_child) ## can't understand why?

			node.data = successor.data

			self.delete_node(successor)


def fill_tree(tree):
	elements = [10, 5, 3, 7, 15, 20]
	for el in elements:
		tree.insert(el)
	return tree


tree = BinarySearchTree()
tree = fill_tree(tree)
tree.print_tree()

# print(f"Tree height --> {tree.height()}")

# print(tree.search(7))

tree.delete_value(5)
print("After deletion:")
tree.print_tree()

tree.delete_value(15)
print("After deletion:")
tree.print_tree()

tree.delete_value(10)
print("After deletion:")
tree.print_tree()

tree.delete_value(7)
print("After deletion:")
tree.print_tree()

