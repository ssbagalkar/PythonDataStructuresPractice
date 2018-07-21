class Tree:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


root = Tree(3)
root.left = Tree(1)
root.right = Tree(5)

root.left.left = Tree(0)
root.left.right = Tree(2)

root.right.left = Tree(4)
root.right.right = Tree(6)


def search_bst(tree, key):
	found = False
	# base case
	if key == tree.val:
		found = True
		return found

	else:

		if key < tree.val:
			# search in left subtree
			while tree:
				if key < tree.val:
					tree = tree.left
				elif key > tree.val:
					tree = tree.right
				else:
					found = True
					return found
			return found
		else:
			# search in right subtree
			while tree:
				if key < tree.val:
					tree = tree.left
				elif key > tree.val:
					tree = tree.right
				else:
					found = True
					return found
			return found


print(search_bst(root, 2))
#
#
def search_bst_recursive(tree, key):
	if not tree:
		return False
	if tree.val == key:
		return True
	
	if key > tree.val:
		return (search_bst_recursive(tree.right, key))
	
	if key < tree.val:
		return (search_bst_recursive(tree.left, key))


print(search_bst_recursive(root, -1))
