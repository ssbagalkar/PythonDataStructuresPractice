

"""

Youtube Link - https://www.youtube.com/watch?v=szKVpQtBHh8&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=36
Time Complexity of Recursion : Exponential
Time Complexity of Memoization:  0(n^3) cubed
Time Complexity of Optimized Memoization : O(n^2)

Verified in Leetcode: Nope
"""
import math
# better option is just revers the string and see if its equal
def is_palindrome(arr, s, e):
    arr = arr[s:e+1]
    return arr == arr[::-1]

def palindrome_partioning_recursion(arr, i, j):
    # Base condition
    if i >= j:
        return 0

    if is_palindrome(arr, i, j):
        return 0

    cost = math.inf
    for k in range(i, j):
        temp_val = 1 + palindrome_partioning_recursion(arr, i, k) + \
                   palindrome_partioning_recursion(arr, k+1, j)

        if temp_val < cost:
            cost = temp_val
    return cost


def palindrome_partioning_memoized(arr, i, j, memo):

    # Check if already present in memo table
    if memo[i][j] != 0:
        return memo[i][j]

    if i >= j:
        return 0

    if is_palindrome(arr, i, j):
        return 0

    cost = math.inf

    for k in range(i, j):
        temp_val = palindrome_partioning_memoized(arr, i, k, memo) + \
                    palindrome_partioning_memoized(arr, k+1, j, memo) + 1

        if temp_val < cost:
            memo[i][j] = temp_val
            cost = temp_val

    return memo[i][j]

"""
Basically here you just check if left and right subsections are already calculated. Hence the complexity
is reduced from O(n^3) to 0(n^2)
"""
def palindrome_partioning_memoized_optimized(arr, i , j, memo):
    # Check if already present in memo table
    if memo[i][j] != 0:
        return memo[i][j]

    if i >= j:
        return 0

    if is_palindrome(arr, i, j):
        return 0

    cost = math.inf

    for k in range(i, j):
        if memo[i][k] != 0:
            left = memo[i][k]
        else:
            left = palindrome_partioning_memoized(arr, i, k, memo)

        if memo[k+1][j] != 0:
            right = memo[k+1][j]
        else:
            right = palindrome_partioning_memoized(arr, k+1, j, memo)

        temp_val = left + right + 1

        if temp_val < cost:
            memo[i][j] = temp_val
            cost = temp_val

    return memo[i][j]


# Driver program to test above function
string = 'ababbbabbababa'
n = len(string)
memo = [[0 for _ in range(n+1)] for _ in range(n+1)]
assert palindrome_partioning_recursion(string, 0, n-1) == \
       palindrome_partioning_memoized(string, 0, n-1, memo=memo)
assert palindrome_partioning_memoized(string, 0, n-1, memo) == \
       palindrome_partioning_memoized_optimized(string, 0, n-1, memo)
print(palindrome_partioning_memoized_optimized(string, 0, n-1, memo))