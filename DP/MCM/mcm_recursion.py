
"""
Given a sequence of matrices, find the most efficient way to multiply these matrices together.
The problem is not actually to perform the multiplications,
but merely to decide in which order to perform the multiplications.

Youtube Link:https://www.youtube.com/watch?v=kMK148J9qEE&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=34
Geeks link: https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/

Complexity : Exponential

Verified in Leetcode: Nope

"""


import math
def matrix_chain_multiplication_recursion(arr, i, j):
    # Base condition
    if i == j:
        return 0

    min_val = math.inf
    for k in range(i, j):
        temp_val = matrix_chain_multiplication_recursion(arr, i, k) + \
                   matrix_chain_multiplication_recursion(arr, k+1, j) + \
                   arr[i-1] * arr[k] * arr[j]

        if temp_val < min_val:
            min_val = temp_val
    return min_val


# Driver program to test above function
arr = [1, 2, 3, 4, 3]
n = len(arr)

print("Minimum number of multiplications is ",
      matrix_chain_multiplication_recursion(arr, 1, n-1))