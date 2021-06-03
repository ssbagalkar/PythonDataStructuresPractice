"""
Problem statement:Given two sequences, find the length of longest contiguous substring present in both of them.


Input : X = “GeeksforGeeks”, y = “GeeksQuiz”
Output : 5
The longest common substring is “Geeks” and is of length 5.

Input : X = “abcdxyz”, y = “xyzabcd”
Output : 4
The longest common substring is “abcd” and is of length 4.

Input : X = “zxabcdezy”, y = “yzabcdezx”
Output : 6
The longest common substring is “abcdez” and is of length 6.

PROBLEM STATEMENT LINK:https://www.geeksforgeeks.org/longest-common-substring-dp-29/
Youtube Video (Aditya Verma)-->https://www.youtube.com/watch?v=HrybPYpOvz0&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=22

Complexity Analysis:
n is length of longest string ( check this )
                Time                Space
Recursion       O(2^n)              O(1)

Memoization     O(m*n)              O(n * m)

Tabular         O(m*n)              O(n * m ) ?

Answers verified in Leetcode/HackerRank? : Yes
"""
import numpy as np

# This recursive approach is take from geeks for geeks. The approach is very similar to 01_lcs problem
def lcss_recursion(str_one, str_two, n , m, count):
    # Base Condition
    if n == 0 or m == 0:
        return count
    if str_one[n-1] == str_two[m-1]:
        count = lcss_recursion(str_one, str_two, n-1, m-1, count+1)
    else:
        count = max(count, max((lcss_recursion(str_one, str_two, n-1, m, 0),
                    lcss_recursion(str_one, str_two, n, m-1, 0))))
    return count

# This is wrong
# def lcss_memoization(str_one, str_two, n, m, memo):
#
#     if memo[n][m] != 0:
#         return memo[n][m]
#
#     # Base Condition
#     if n == 0 or m == 0:
#         return 1
#     if str_one[n-1] == str_two[m-1]:
#         memo[n][m] = lcss_memoization(str_one, str_two, n-1, m-1, memo)
#
#     else:
#         count = max(count, max((lcss_memoization(str_one, str_two, n-1, m, memo),
#                     lcss_memoization(str_one, str_two, n, m-1, memo))))
#         memo[n][m] = count
#     return memo[n][m]


def lcss_tabular(str_one, str_two, n, m):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for ii in range(1, n+1):
        for jj in range(1, m+1):
            if str_one[ii-1] == str_two[jj-1]:
                dp[ii][jj] = 1 + dp[ii-1][jj-1]
            else:
                dp[ii][jj] = 0
    #as we cant use numpy
    # return np.max(np.array(dp))
    max_val_list = []
    for ii in range(n+1):
        max_val = max(dp[ii][:])
        max_val_list.append(max_val)
    return max(max_val_list)



str_one = "abcde"
str_two = "ababcde"
n = len(str_one)
m = len(str_two)
print(lcss_recursion(str_one, str_two, n, m, 0))
print(lcss_tabular(str_one, str_two, n, m))
