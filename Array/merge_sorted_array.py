
#https://leetcode.com/problems/merge-sorted-array/
from typing import List
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = len(nums1) - len(nums2) - 1
    j = len(nums2) - 1
    k = len(nums1) - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

print(merge([1,2,3,0,0,0],6, [2,5,6],3))