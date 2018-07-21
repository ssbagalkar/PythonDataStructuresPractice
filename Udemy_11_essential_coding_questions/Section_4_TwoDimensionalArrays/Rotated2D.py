import copy
## This is my solution
# n = # rows = # columns in the given 2d array
def rotate(given_array, n):
    rotated = copy.deepcopy(given_array)
    # NOTE: To solve it in place, write this function so that you
    # won't have to create rotated.
    rotated= [[0 for ii in range(n)]for jj in range(n)]
    for ii in range(n):
        k=0
        for jj in range (n):
            rotated[k][abs(n-1-ii)] = given_array[ii][jj]
            k+=1
    return rotated

		
# This is more structured solution from lesson
# def rotate(given_array, n):
    # rotated = copy.deepcopy(given_array)
    # for i in range(n):
        # for j in range(n):
            # (new_i, new_j) = rotate_sub(i, j, n)
            # rotated[new_i][new_j] = given_array[i][j]
    # return rotated


# def rotate_sub(i, j, n):
    # return j, n - 1 - i
		
# NOTE: The following input values will be used for testing your solution.
a1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
print(rotate(a1, 3))
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]

a2 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]]
print(rotate(a2, 4))
# [[13, 9, 5, 1],
#  [14, 10, 6, 2],
#  [15, 11, 7, 3],
#  [16, 12, 8, 4]]
