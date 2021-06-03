"""
Problem:
Minimum number of deletions to make a string palindrome
Given a string of size ‘n’. The task is to remove or delete minimum number of
characters from the string so that the resultant string is palindrome.
Example:
Input : s = "aebcbda", output = 2
Remove characters 'e' and 'd'
Resultant string will be 'abcba'
which is a palindromic string

Problem Link: https://www.geeksforgeeks.org/minimum-number-deletions-make-string-palindrome/
Video link: https://www.youtube.com/watch?v=CFwCCNbRuLY&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=28

Complexity Analysis:
n is length of longest string
                Time                Space
Recursion       O(2^n)              O(1)

Memoization     O(n^2)              O(n^2)

Tabular         O(n^2)              O(n^2 ) ?


Verified in Leetcode - ?

Note: The solution is exactly the same if they ask for min number of insertions as well
"""

def min_del_palindrome_recursion(str_one, str_two, n, m):

    # Base condition
    if n == 0 or m == 0:
        return 0

    # From choice diagram
    if str_one[n-1] == str_two[m-1]:
        return 1 + min_del_palindrome_recursion(str_one, str_two, n-1, m-1)
    else:
        return max(min_del_palindrome_recursion(str_one, str_two, n-1, m), min_del_palindrome_recursion(str_one, str_two, n, m-1))


def min_del_palindrome_memoization(str_one, str_two, n, m, memo):
    # Base Condition and checking
    if memo[n][m] != 0:
        return memo[n][m]
    if n == 0 or m == 0:
        return 0

    # From choice diagram
    if str_one[n - 1] == str_two[m - 1]:
        memo[n][m] = 1 + min_del_palindrome_memoization(str_one, str_two, n - 1, m - 1, memo)
    else:
        memo[n][m] = max(min_del_palindrome_memoization(str_one, str_two, n - 1, m, memo),
                         min_del_palindrome_memoization(str_one, str_two, n, m - 1, memo))
    return memo[n][m]


def min_del_palindrome_tabular(str_one, str_two, n, m):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for ii in range(1, n+1):
        for jj in range(1, m+1):
            if str_one[ii-1] == str_two[jj-1]:
                dp[ii][jj] = 1 + dp[ii-1][jj-1]
            else:
                dp[ii][jj] = max(dp[ii-1][jj], dp[ii][jj-1])
    return dp[n][m]


s1 = "aebcbda"
s2 = s1[::-1]

n = len(s1)
m = len(s2)
print("Recursion Results:")
print(f"Min Deletions-->{n-min_del_palindrome_recursion(s1, s2, n, m)}")

print(" ------------------------------------------- ")
print("Memoization Results:")
memo = [[0 for _ in range(m+1)] for _ in range(n+1)]
print(f"Min Deletions-->{n -min_del_palindrome_memoization(s1, s2, n, m, memo)}")

print(" --------------------------------------------- ")
print("Tabular Results:")
print(f"Min Deletions-->{m -min_del_palindrome_tabular(s1, s2, n, m)}")
