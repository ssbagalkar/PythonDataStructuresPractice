"""
Problem link --> https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/

Video --> https://www.youtube.com/watch?v=-GtpxG6l_Mc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=10

"""
def minimum_subset_sum_difference_fn(arr):
    n = len(arr)
    s = sum(arr)
    dp = [[False for _ in range(s+1)] for _ in range(n+1)]
    for ii in range(n+1):
        dp[ii][0] = True

    #Build table exactly the same as subset sum
    for ii in range(1, n+1):
        for jj in range(1, s+1):
            if arr[ii-1] <= jj:
                dp[ii][jj] = dp[ii-1][jj-arr[ii-1]] or dp[ii-1][jj]
            elif arr[n-1] > jj:
                dp[ii][jj] = dp[ii-1][jj]

    #Now get the candidates
    candidate_list = []
    for jj in range(s+1):
        if dp[n][jj] is True:
            candidate_list.append(jj)

    #Get the min value
    min_val = float("inf")
    for ii in range(len(candidate_list)//2):
        min_val = min(min_val, s-2*candidate_list[ii])
    return min_val


arr = [1, 6, 5, 11]
expected = 1
assert minimum_subset_sum_difference_fn(arr) == expected
print("test passed")
