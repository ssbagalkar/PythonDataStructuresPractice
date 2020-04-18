
# https://www.youtube.com/watch?v=COk73cpQbFQ&t=811s
# I have written this on my own
def partition(arr, start, end):
    pivot = arr[end]
    p_index = start

    for ii in range(start, end):
        if arr[ii] <= pivot:
            arr[ii], arr[p_index] = arr[p_index], arr[ii]
            p_index += 1

    arr[p_index], arr[end] = arr[end], arr[p_index]
    return p_index


def quick_sort(arr, start, end):
    if start < end:
        p_index = partition(arr, start, end)
        quick_sort(arr, start, p_index-1)
        quick_sort(arr, p_index+1, end)
    return arr

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)-1
print(quick_sort(arr, 0, n))
