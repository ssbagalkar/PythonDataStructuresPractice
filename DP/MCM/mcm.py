
"""

Refer this beautiful math oriented explanation

http://www.personal.kent.edu/~rmuhamma/Algorithms/MyAlgorithms/Dynamic/chainMatrixMult.htm


Given a sequence of matrices, find the most efficient way to multiply these matrices together.
The problem is not actually to perform the multiplications,
but merely to decide in which order to perform the multiplications.

Youtube Link:https://www.youtube.com/watch?v=kMK148J9qEE&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=34
Geeks link: https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/

Time Complexity of Recursion : Exponential
Time Complexity of Memoization:  0(n^3) cubed

Verified in Leetcode: Nope

"""


import math
def matrix_chain_multiplication_recursion(arr, i, j):
    # Base condition
    if i == j:
        return 0

    cost = math.inf
    for k in range(i, j):
        temp_val = matrix_chain_multiplication_recursion(arr, i, k) + \
                   matrix_chain_multiplication_recursion(arr, k+1, j) + \
                   arr[i-1] * arr[k] * arr[j]

        if temp_val < cost:
            cost = temp_val
    return cost


def matrix_chain_multiplication_memoized(arr, i, j, memo):

    # Check if already present in memo table
    if memo[i][j] != -1:
        return memo[i][j]

    if i >= j:
        return 0

    cost = math.inf

    for k in range(i, j):
        temp_val = matrix_chain_multiplication_recursion(arr, i, k) + \
                    matrix_chain_multiplication_recursion(arr, k+1, j) + \
                    arr[i-1] * arr[k] * arr[j]

        if temp_val < cost:
            memo[i][j] = temp_val
            cost = temp_val

    return memo[i][j]


# Driver program to test above function
arr = [1, 2, 3, 4, 3]
n = len(arr)
memo = [[-1 for _ in range(n+1)] for _ in range(n+1)]
assert matrix_chain_multiplication_recursion(arr, 1, n-1) == \
       matrix_chain_multiplication_memoized(arr, 1, n-1, memo=memo)

print(matrix_chain_multiplication_memoized(arr, 1, n-1, memo))