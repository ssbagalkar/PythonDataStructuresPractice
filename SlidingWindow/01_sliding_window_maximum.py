"""
Video Link -->  https://www.youtube.com/watch?v=KtpqeN0Goro&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=3&ab_channel=AdityaVerma
Problem link --> https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1


Time Complexity: O(n)
Auxiliary Space: O(1)

verified on geeks -->  YES

This is a very easy problem. Don't confuse this with maximum of all arrays in sliding approach which is #4
"""

def sliding_window_max(arr, k):
    n = len(arr)
    ii = 0
    jj= 0
    max_sum = float("-inf")
    current_sum = 0
    while jj < n:
        current_sum = current_sum + arr[jj]
        if (jj - ii + 1) < k:
            jj += 1
        elif (jj-ii+1) == k:
            max_sum = max(current_sum, max_sum)
            current_sum -= arr[ii]
            ii += 1
            jj += 1
    return max_sum


arr = [1, 3, -1, -3, 5, 3, 6, 7]
print(sliding_window_max(arr, 3))