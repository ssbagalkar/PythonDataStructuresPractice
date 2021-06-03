"""
Problem:
Minimum number of deletions and insertions to transform one string into another
Given two strings ‘str1’ and ‘str2’ of size m and n respectively. The task is to remove/delete and insert minimum number of characters from/in str1 so as to transform it into str2. It could be possible that the same character needs to be removed/deleted from one point of str1 and inserted to some another point.
Example:
Input : str1 = "geeksforgeeks", str2 = "geeks"
Output : Minimum Deletion = 8
         Minimum Insertion = 0

Problem Link:         https://www.youtube.com/redirect?event=video_description&v=-fx6aDxcWyg&redir_token=QUFFLUhqa0pVUzNnLUU5ZkJETXdBVVYwdzFyM2ZiaXVpUXxBQ3Jtc0ttLWV5T1lCU21rbDJieUs2cm5zY3JnMEhnWnloVmFhUThHdEl2R2tNTlE0dVpVRk9uZzZLeXhYb24xV0V3cnBRSTBxbE1uamwtcUdMSDRhQnZWNHIteGV1XzQyeHFiMXlsNkRqblMwY3pYcGVIRDJ2OA%3D%3D&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fminimum-number-deletions-insertions-transform-one-string-another%2F
Video Link:         https://www.youtube.com/watch?v=nqowUJzG-iM&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go

Complexity ??

Verified in Leetcode - YES
"""

def min_insert_del_recursion(str_one, str_two, n, m):

    # Base condition
    if n == 0 or m == 0:
        return 0

    # From choice diagram
    if str_one[n-1] == str_two[m-1]:
        return 1 + min_insert_del_recursion(str_one, str_two, n-1, m-1)
    else:
        return max(min_insert_del_recursion(str_one, str_two, n-1, m), min_insert_del_recursion(str_one, str_two, n, m-1))

def min_insert_del_memoization(str_one, str_two, n, m, memo):
    # Base Condition and checking
    if memo[n][m] != 0:
        return memo[n][m]
    if n == 0 or m == 0:
        return 0

    # From choice diagram
    if str_one[n - 1] == str_two[m - 1]:
        memo[n][m] = 1 + min_insert_del_memoization(str_one, str_two, n - 1, m - 1, memo)
    else:
        memo[n][m] = max(min_insert_del_memoization(str_one, str_two, n - 1, m, memo),
                         min_insert_del_memoization(str_one, str_two, n, m - 1, memo))
    return memo[n][m]


def min_insert_del_tabular(str_one, str_two, n, m):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for ii in range(1, n+1):
        for jj in range(1, m+1):
            if str_one[ii-1] == str_two[jj-1]:
                dp[ii][jj] = 1 + dp[ii-1][jj-1]
            else:
                dp[ii][jj] = max(dp[ii-1][jj], dp[ii][jj-1])
    return dp[n][m]


str_one = "heap"
str_two = "pea"
# str_one = "EACBD"
# str_two = "EABCD"
n = len(str_one)
m = len(str_two)
print("Recursion Results:")
lcs_recursion = min_insert_del_recursion(str_one, str_two, n, m)
if n >= m:
    print(f"Min Deletions-->{m-lcs_recursion}")
    print(f"Min Insertions-->{n - lcs_recursion}")
else:
    print(f"Min Deletions-->{n - lcs_recursion}")
    print(f"Min Insertions-->{m - lcs_recursion}")
print(" ------------------------------------------- ")
print("Memoization Results:")
memo = [[0 for _ in range(m+1)] for _ in range(n+1)]
lcs_memoization = min_insert_del_memoization(str_one, str_two, n, m, memo)
if n >= m:
    print(f"Min Deletions-->{m -lcs_memoization}")
    print(f"Min Insertions-->{n - lcs_memoization}")
else:
    print(f"Min Deletions-->{n - lcs_memoization}")
    print(f"Min Insertions-->{m - lcs_memoization}")
print(" --------------------------------------------- ")
print("Tabular Results:")
lcs_tabular = min_insert_del_tabular(str_one, str_two, n, m)
if n > m:
    print(f"Min Deletions-->{m -lcs_tabular}")
    print(f"Min Insertions-->{n - lcs_tabular}")
else:
    print(f"Min Deletions-->{n - lcs_tabular}")
    print(f"Min Insertions-->{m - lcs_tabular}")
