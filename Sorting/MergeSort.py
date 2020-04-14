# https://www.youtube.com/watch?v=TzeBrDU-JaY
# Time Complexity - O(nlogn)
# Space Complexity - O(n)
# Written by me completely using pseudocode from above video

def merge(first_arr, second_arr, original):
    ii = 0
    jj = 0
    kk = 0
    n = len(first_arr)
    m = len(second_arr)
    while ii < n and jj < m:
        if first_arr[ii] < second_arr[jj]:
            original[kk] = first_arr[ii]
            ii += 1
        else:
            original[kk] = second_arr[jj]
            jj += 1
        kk += 1

    while ii < n:
        original[kk] = first_arr[ii]
        ii += 1
        kk += 1

    while jj < m:
        original[kk] = second_arr[jj]
        jj += 1
        kk += 1

    return original


def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return arr
    mid_index = n // 2
    left_arr = arr[0:mid_index]
    right_arr = arr[mid_index:]
    # recursively run on left array
    merge_sort(left_arr)
    merge_sort(right_arr)
    return merge(left_arr, right_arr, arr)


print(merge_sort([12, 11, 13, 5, 6, 7]))
