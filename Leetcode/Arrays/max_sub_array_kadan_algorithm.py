from typing import List
# Leetcode --> https://leetcode.com/problems/maximum-subarray/submissions/
# CSDOJO explanation --> https://www.youtube.com/watch?v=86CQq3pKSUw
def maxSubArray(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    ii = 1
    global_max = nums[0]
    current_max = nums[0]

    while ii < len(nums):
        current_max = max(nums[ii], sum([current_max, nums[ii]]))
        if current_max > global_max:
            global_max = current_max
        ii += 1
    return global_max
