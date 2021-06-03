"""
https://www.youtube.com/watch?v=Osz-Vwer6rw&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=49&ab_channel=AdityaVermaAdityaVerma

How to approach this problem?

Simple steps to follow and think:
1. Either we will find the max sum passing
	a. Through the root with left children involved i.e left children + parent node
	b. Through the root with right children involved i.e right tree + parent node
	c. Node only
	d. Left Tree + Right Tree + Node

	We have to keep track of all the paths and get max among them

2. For keeping track of a and b, the cost function is recursively calculated on
	left tree and right tree. Let's call that variable temp. Defined as
	MAX(left_tree_call, right_tree_call) + node.data)

	Then, for keeping track of c, we add root data and take max amongst the two i.e
	MAX(MAX(left_tree_call, right_tree_call) + node.data) , node.data)

	The reason for this max is we might encounter some negative value in the children nodes( or the node in question
	as well). So, we have no idea, which path will give us the MAX value. So, we make a recursive call
	to check all paths in left and right subtree and add that to the root/node in question.

	Then we compare it with just the node in question and store this value in variable temp

3. For d, the node under consideration is the root of the maxSum path and no ancestor of root are there in max sum path
So objective function is MAX(left_tree_call + right_tree_call + node.data, temp)

Time Complexity of above approach:
O(n)


Verified In LeetCode/HackerRank ? Yes
"""


class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def find_max_sum_util(root):
	if root is None:
		return 0

	# recursively call left and right subtree to find the sum
	left_sum = find_max_sum_util(root.left)
	right_sum = find_max_sum_util(root.right)

	# store value of a, b and c in temp. This path assumes you don't know whether the max
	# value will include the root node or not
	temp = max(max(left_sum, right_sum) + root.data, root.data)

	# store value of max of temp and d in variable answer. This keeps track of path
	# assuming that the root and both its children are involved in the max sum path
	answer = max(temp, left_sum + right_sum + root.data)

	# We will store all these values and compare each with result variable
	find_max_sum_util.result = max(find_max_sum_util.result, answer)

	return temp


def find_max_sum(root):
	find_max_sum_util.result = float("-inf")
	find_max_sum_util(root)
	return find_max_sum_util.result

# Driver code
if __name__ == '__main__':
	root = Node(-10)
	root.left = Node(9)
	root.right = Node(20)
	root.right.right = Node(7)
	root.right.left = Node(15)

	print("Max sum is", find_max_sum(root))
