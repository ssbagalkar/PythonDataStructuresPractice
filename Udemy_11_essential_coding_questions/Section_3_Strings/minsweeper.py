# Implement your function below.
def mine_sweeper(bombs, num_rows, num_cols):
	field = [[0 for i in range(num_cols)] for j in range(num_rows)]
	## Fill the bombs as -1
	for bomb in bombs:
		field[bomb[0]][bomb[1]] = -1
		
	for bomb in bombs:
		## all 8 adjancencies
		# upper row
		if bomb[0] - 1 >= 0:
			if field[bomb[0] - 1][bomb[1]] != -1:
				field[bomb[0] - 1][bomb[1]] += 1
		
		# lower row
		if bomb[0] + 1 < num_rows:
			if field[bomb[0]+1][bomb[1]] != -1:
				field[bomb[0] + 1][bomb[1]] += 1
		
		# next column
		if bomb[1] + 1 < num_cols:
			if field[bomb[0]][bomb[1] + 1] != -1:
				field[bomb[0]][bomb[1] + 1] += 1
		
		# previous column
		if bomb[1] - 1 >= 0:
			if field[bomb[0]][bomb[1] - 1] != -1:
				field[bomb[0]][bomb[1] - 1] += 1
		
		# diagonal upper right
		if bomb[0] - 1 >= 0 and bomb[1] + 1 < num_cols:
			if field[bomb[0] - 1][bomb[1] + 1] != -1:
				field[bomb[0] - 1][bomb[1] + 1] += 1
		
		# diagonal upper left
		if bomb[0] - 1 >= 0  and bomb[1] - 1 >= 0:
			if field[bomb[0] - 1][bomb[1] - 1] != -1:
				field[bomb[0] - 1][bomb[1] - 1] += 1
		
		# diagonal lower right
		if bomb[0] + 1 < num_rows and bomb[1] + 1 < num_cols :
			if field[bomb[0] + 1][bomb[1] + 1] != -1:
				field[bomb[0] + 1][bomb[1] + 1] += 1
		
		# diagonal lower left
		if bomb[0] + 1 < num_rows and bomb[1] - 1 >= 0:
			if field[bomb[0] + 1][bomb[1] - 1] != -1:
				field[bomb[0] + 1][bomb[1] - 1] += 1
	
	return field


# NOTE: The following input values will be used for testing your solution.
print(mine_sweeper([[0, 2], [2, 0]], 3, 3))
# [[0, 1, -1],
#  [1, 2, 1],
#  [-1, 1, 0]]

print(mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4))
# [[-1, -1, 2, 1],
#  [2, 3, -1, 1],
#  [0, 1, 1, 1]]

print(mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5))
# [[1, 2, 2, 1, 0],
#  [1, -1, -1, 2, 0],
#  [1, 3, -1, 2, 0],
#  [0, 1, 2, 2, 1],
#  [0, 0, 1, -1, 1]]