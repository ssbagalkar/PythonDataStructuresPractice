from typing import List
# Leetcode --> https://leetcode.com/problems/maximum-subarray/submissions/
# CSDOJO explanation --> https://www.youtube.com/watch?v=86CQq3pKSUw
def max_subarray(nums: List[int]) -> int:
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

# Now modify this for max_subarray product
#https://www.youtube.com/watch?v=vtJvbRlHqTA

def max_product(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    ii = 1
    global_max = nums[0]
    previous_max = nums[0]
    previous_min = nums[0]
    while ii < len(nums):
        current_max = max(nums[ii], previous_max * nums[ii], previous_min * nums[ii])
        current_min = min(nums[ii], previous_max * nums[ii], previous_min * nums[ii])
        previous_max = current_max
        previous_min = previous_min
        if current_max > global_max:
            global_max = current_max
        if current_min > global_max:
            global_max = current_min
        ii += 1
    return global_max


print(max_product([-4, -3, -2]))

