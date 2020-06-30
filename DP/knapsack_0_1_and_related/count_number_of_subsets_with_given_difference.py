"""
Video -->https://www.youtube.com/watch?v=ot_XBHyqpFc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=11

This problem is exactly similar to count of subsets sum.You just have to reduce the problem a bit.
What we want is :
sum(s1)-sum(s2) = given_difference  -1
now,
sum(s1)+sum(s2) = sum(given_array)  -2

so from 1 and 2
sum(s1) = (sum(given_array) + given_difference)/2

Now the problem is reduced to count the number of subsets sum where the sum is sum(s1)

Note: same problem as Target sum
"""

def count_number_of_subsets_with_given_difference(arr, diff):
    s = (diff+sum(arr))//2
    n = len(arr)

    dp = [[0 for _ in range(s + 1)] for _ in range(n + 1)]

    for ii in range(n + 1):
        dp[ii][0] = 1

    for ii in range(1, n + 1):
        for jj in range(1, s + 1):
            if jj >= arr[ii - 1]:
                dp[ii][jj] = dp[ii - 1][jj - arr[ii - 1]] + dp[ii - 1][jj]
            elif jj < arr[ii - 1]:
                dp[ii][jj] = dp[ii - 1][jj]
    return dp[n][s]

arr = [1, 1, 2, 3]
diff = 1
expected = 3
assert count_number_of_subsets_with_given_difference(arr, diff) == expected
print("test passed")
