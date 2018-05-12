"""
 * There are two sorted arrays nums1 and nums2 of size m and n respectively.
 * Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
 *
 * Solution
 * Take minimum size of two array. Possible number of partitions are from 0 to m in m size array.
 * Try every cut in binary search way. When you cut first array at i then you cut second array at (m + n + 1)/2 - i
 * Now try to find the i where a[i-1] <= b[j] and b[j-1] <= a[i]. So this i is partition around which lies the median.
 *
 * Time complexity is O(log(min(x,y))
 * Space complexity is O(1)

 Link:
 https://www.youtube.com/watch?v=LPFhl65R7ww&t=590s

 """
import math


def findMedianSortedArray(arr1, arr2):
    if len(arr1) > len(arr2):
        return (findMedianSortedArray(arr2, arr1))

    x = len(arr1)
    y = len(arr2)

    low = 0
    high = x

    while (low <= high):
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        # If partitionX is 0, it means there is nothing on the left side, use -INF.
        if partitionX == 0:
            maxLeftX = -math.inf
        else:
            maxLeftX = arr1[partitionX - 1]

        if partitionX == x:
            minRightX = math.inf
        else:
            minRightX = arr1[partitionX]

        if partitionY == 0:
            maxLeftY = -math.inf
        else:
            maxLeftY = arr2[partitionY - 1]

        if partitionY == y:
            minRightY = math.inf
        else:
            minRightY = arr2[partitionY]

        if (maxLeftX <= minRightY and maxLeftY <= minRightX):
            '''We have partitioned array at correct place
            Now get max of left elements and min of right elements to get the median
            in case of even length combined array size
            or get max of left for odd length combined array size'''

            if (x + y) % 2 == 0:
                return (max(maxLeftX, maxLeftY), min(minRightX, minRightY) / 2)
            else:
                return (max(maxLeftX, maxLeftY))

        elif (maxLeftX > minRightY):  # we are too far on right side for partitionX. Go on left side.
            high = partitionX - 1

        else:
            low = partitionX + 1

arr1 = [1, 3, 8, 9, 15]
arr2 = [7, 11, 18, 19, 21, 25]

print(findMedianSortedArray(arr1, arr2))