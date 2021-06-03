"""
Problem Statement:
Evaluate Expression To True-Boolean Parenthesization Recursion
Given a boolean expression with following symbols.
Symbols
    'T' --- true
    'F' --- false
And following operators filled between symbols
Operators
    &   ---boolean AND
    |   --- boolean OR
    ^   --- boolean XOR
Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.
Example:
Input: symbol[]    = {T, F, T}
       operator[]  = {^, &}
Output: 2
The given expression is "T ^ F & T", it evaluates true
in two ways "((T ^ F) & T)" and "(T ^ (F & T))"

Youtube link --> https://www.youtube.com/watch?v=pGVguAcWX4g&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=39
Useful link for code - https://www.youtube.com/watch?v=7Gk36fHV38E&t=854s
Geeks Link --> https://www.geeksforgeeks.org/boolean-parenthesization-problem-memo-37/

Complexity:
Time -->
Space -->

Verified in Leetcode/InterviewBits--> No
"""


def solve_recursion(s: str, i: int, j: int, is_true: bool):
	if i > j:
		return 0

	if i == j:
		if is_true:
			return 1 if s[i] == 'T' else 0
		else:
			return 1 if s[i] == 'F' else 0

	num_ways = 0

	for k in range(i + 1, j, 2):
		left_true = solve_recursion(s, i, k - 1, is_true=True)
		left_false = solve_recursion(s, i, k - 1, is_true=False)
		right_true = solve_recursion(s, k + 1, j, is_true=True)
		right_false = solve_recursion(s, k + 1, j, is_true=False)

		if s[k] == '&':
			if is_true is True:
				num_ways += left_true * right_true
			else:
				num_ways += (left_false * right_false) + (left_false * right_true) + (left_true * right_false)

		elif s[k] == '|':
			if is_true is True:
				num_ways += (left_false * right_true) + (left_true * right_false) + (left_true * right_true)
			else:
				num_ways += left_false * right_false
		elif s[k] == '^':
			if is_true is True:
				num_ways += (left_false * right_true) + (left_true * right_false)
			else:
				num_ways += (left_false * right_false) + (left_true * right_true)

	return num_ways


# this geeks for geeks is giving me wrong answer ???
def solve_memoization(s: str, i: int, j: int, is_true: int, memo):
	if i > j:
		return 0

	if i == j:

		if is_true == 1:
			return 1 if s[i] == 'T' else 0
	else:
		return 1 if s[i] == 'F' else 0

	if memo[i][j][is_true] != -1:
		return memo[i][j][is_true]

	temp_ans = 0

	for k in range(i + 1, j, 2):

		if memo[i][k - 1][1] != -1:
			left_true = memo[i][k - 1][1]
		else:
			# Count number of True in left Partition
			left_true = solve_memoization(s, i, k - 1, 1, memo)

		if memo[i][k - 1][0] != -1:
			left_false = memo[i][k - 1][0]
		else:
			# Count number of False in left Partition
			left_false = solve_memoization(s, i, k - 1, 0, memo)

		if memo[k + 1][j][1] != -1:
			right_true = memo[k + 1][j][1]
		else:
			# Count number of True in right Partition
			right_true = solve_memoization(s, k + 1, j, 1, memo)
	
		if memo[k + 1][j][0] != -1:
			right_false = memo[k + 1][j][0]
		else:
			# Count number of False in right Partition
			right_false = solve_memoization(s, k + 1, j, 0, memo)

		# Evaluate AND operation
		if s[k] == '&':
			if is_true == 1:
				temp_ans = temp_ans + left_true * right_true
			else:
				temp_ans = temp_ans + left_true * right_false + left_false * right_true + left_false * right_false
		# Evaluate OR operation
		elif s[k] == '|':
			if is_true == 1:
				temp_ans = temp_ans + left_true * right_true + left_true * right_false + left_false * right_true
			else:
				temp_ans = temp_ans + left_false * right_false

		# Evaluate XOR operation
		elif s[k] == '^':
			if is_true == 1:
				temp_ans = temp_ans + left_true * right_false + left_false * right_true
			else:
				temp_ans = temp_ans + left_true * right_true + left_false * right_false
		memo[i][j][is_true] = temp_ans

	return temp_ans


my_str = "T|T&F^T"
n = len(my_str)
memo = [[[-1 for _ in range(2)] for _ in range(n + 1)] for _ in range(n + 1)]
print(solve_memoization(my_str, 0, n - 1, 1, memo))
print(solve_recursion(my_str, 0, n - 1, True))
