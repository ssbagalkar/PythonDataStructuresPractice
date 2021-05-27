"""
I like Vivek's explanation more here. For general syntax though, follow Aditya Verma
https://www.youtube.com/watch?v=ey7DYc9OANo

How to approach this problem?

Simple steps to follow and think:
1. Either we will find the diameter passing through the root OR Not passing through the root
2. if passing through the root, the cost function recursively is
	left_height + right_height + 1
3. If not passing through the root, cost function is recursively calling on left tree and then right tree and take max

4. So return MAX( 2, 3 ) i.e max(1+left_height+right_height, max(recursive_fn_call(left), recursive_fn_call(right))

Time Complexity of above approach: O(n^2)

https://www.geeksforgeeks.org/diameter-of-a-binary-tree/

There is also optimized solution to this is O(n) here:
https://www.geeksforgeeks.org/diameter-of-a-binary-tree-in-on-a-new-method/


Verified In LeetCode/HackerRank ? No
"""


# Not optimized code, running in quadratic time
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def height(current_node, current_height):
	if current_node is None:
		return current_height

	if current_node.left is not None:
		left_height = height(current_node.left, current_height + 1)
	else:
		left_height = current_height

	if current_node.right is not None:
		right_height = height(current_node.right, current_height + 1)
	else:
		right_height = current_height

	return max(left_height, right_height)


def diameter(root):
	if root is None:
		return 0

	left_height = height(root.left, 1)
	right_height = height(root.right, 1)

	left_diameter = diameter(root.left)
	right_diameter = diameter(root.right)

	return max(left_height + right_height + 1, max(left_diameter, right_diameter))


# Optimized code, running in linear time

def diameter_optimized(node, ans):
	# Following Aditya's pattern here
	# 1. First is base condition
	if node is None:
		return 0

	# 2. Hypothesis--> This will always recursive the left tree and right tree
	left_height = diameter_optimized(node.left, ans)
	right_height = diameter_optimized(node.right, ans)

	# Induction-->
	temp = 1 + max(left_height, right_height)
	ans[0] = max(ans[0], 1 + left_height + right_height)
	return temp


if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	print(f"Diameter is {diameter(root)}")
	ans = [-99999999]
	diameter_optimized(root, ans)
	answer = ans[0]
	print(f"Diameter is {answer} ")
