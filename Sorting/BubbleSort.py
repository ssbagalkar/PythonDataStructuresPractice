def bubble_sort_optimized(arr):
    n = len(arr)
    while n >= 1:
        swapped = False
        for ii in range(n-1):
            if arr[ii]>arr[ii+1]:
                arr[ii], arr[ii+1] = arr[ii+1], arr[ii]
                swapped = True
        if not swapped:
            return arr
        n-=1
    return arr


def bubble_sort_not_optimized(arr):
    n = len(arr)
    while n > 0:
        for ii in range(n-1):
            if arr[ii]>arr[ii+1]:
                arr[ii], arr[ii+1] = arr[ii+1], arr[ii]
        n -= 1
    return arr


array_to_be_sorted = [2, 7, 4, 1, 5, 3]
print(bubble_sort_not_optimized(array_to_be_sorted))
print(bubble_sort_optimized(array_to_be_sorted))
assert bubble_sort_not_optimized(array_to_be_sorted) == bubble_sort_optimized(array_to_be_sorted)
