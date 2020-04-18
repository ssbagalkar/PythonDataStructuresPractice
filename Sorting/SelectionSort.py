def selection_sort(arr):
    n = len(arr)
    for ii in range(n):
        min_element_index = ii
        for jj in range(ii+1, n):
            if arr[jj] < arr[min_element_index]:
                min_element_index = jj
        arr[ii], arr[min_element_index] = arr[min_element_index], arr[ii]
    return arr

print(selection_sort([5, 2, 0, -8, 3]))