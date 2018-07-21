##My solution
def click(field, num_rows, num_cols, given_i, given_j):
	# base_case
	if field[given_i][given_j] != 0:
		return field
	else:
		field[given_i][given_j] = -2
		
	# upper row
	if given_i - 1 >= 0:
		if field[given_i - 1][given_j] == 0:
			# field[given_i - 1][given_j] = -2
			# recursively make all neighbours -2 if they are zero
			click(field, num_rows, num_cols, given_i - 1, given_j)
	
	# lower row
	if given_i + 1 < num_rows:
		if field[given_i + 1][given_j] == 0:
			# field[given_i + 1][given_j] = -2
			# recursively make all neighbours -2 if they are zero
			click(field, num_rows, num_cols, given_i + 1, given_j)
	
	# next column
	if given_j + 1 < num_cols:
		if field[given_i][given_j + 1] == 0:
			# field[given_i][given_j + 1] = -2
			# recursively make all neighbours -2 if they are zero
			click(field, num_rows, num_cols, given_i, given_j + 1)
	
	# previous column
	if given_j - 1 >= 0:
		if field[given_i][given_j - 1] == 0:
			# field[given_i][given_j - 1] = -2
			# recursively make all neighbours -2 if they are zero
			click(field, num_rows, num_cols, given_i, given_j - 1)
	
	# diagonal upper right
	if given_i - 1 >= 0 and given_j + 1 < num_cols:
		if field[given_i - 1][given_j + 1] == 0:
			# field[given_i - 1][given_j + 1] = -2
			# recursively make all neighbours -2 if they are zero
			click(field, num_rows, num_cols, given_i - 1, given_j + 1)
	
	# diagonal upper left
	if given_i - 1 >= 0 and given_j - 1 >= 0:
		if field[given_i - 1][given_j - 1] == 0:
			# field[given_i - 1][given_j - 1] = -2
			# recursively make all neighbours -2 if they are zero
			click(field, num_rows, num_cols, given_i - 1, given_j - 1)
	
	# diagonal lower right
	if given_i + 1 < num_rows and given_j + 1 < num_cols:
		if field[given_i + 1][given_j + 1] == 0:
			# field[given_i + 1][given_j + 1] = -2
			# recursively make all neighbours -2 if they are zero
			click(field, num_rows, num_cols, given_i + 1, given_j + 1)
	
	# diagonal lower left
	if given_i + 1 < num_rows and given_j - 1 >= 0:
		if field[given_i + 1][given_j - 1] == 0:
			# field[given_i + 1][given_j - 1] = -2
			# recursively make all neighbours -2 if they are zero
			click(field, num_rows, num_cols, given_i + 1, given_j - 1)


	return field
	
## following solution is from the lesson answer using BFS method
# from collections import deque


# def click(field, num_rows, num_cols, given_i, given_j):
	# to_check = deque()
	# if field[given_i][given_j] == 0:
		# field[given_i][given_j] = -2
		# to_check.insert(0, (given_i, given_j))
	# else:
		# return field
	
	# while len(to_check) > 0:
		# current_i, current_j = to_check.pop()
		# for ii in range(current_i - 1, current_i + 2):
			# for jj in range(current_j - 1, current_j + 2):
				# if ii >= 0 and ii < num_rows and jj >= 0 and jj < num_cols and field[ii][jj] == 0:
					# to_check.insert(0, (ii, jj))
					# field[ii][jj] = -2
		# return field

field1 = [[0, 0, 0, 0, 0],
					[0, 1, 1, 1, 0],
					[0, 1, -1, 1, 0]]

print(click(field1, 3, 5, 2, 2))
# [[0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 0],
#  [0, 1, -1, 1, 0]]

print(click(field1, 3, 5, 1, 4))
# [[-2, -2, -2, -2, -2],
#  [-2, 1, 1, 1, -2],
#  [-2, 1, -1, 1, -2]]


field2 = [[-1, 1, 0, 0],
					[1, 1, 0, 0],
					[0, 0, 1, 1],
					[0, 0, 1, -1]]

print(click(field2, 4, 4, 0, 1))
# [[-1, 1, 0, 0],
#  [1, 1, 0, 0],
#  [0, 0, 1, 1],
#  [0, 0, 1, -1]]

print(click(field2, 4, 4, 1, 3))
# [[-1, 1, -2, -2],
#  [1, 1, -2, -2],
#  [-2, -2, 1, 1],
#  [-2, -2, 1, -1]]