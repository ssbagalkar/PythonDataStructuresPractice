arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]


def LinearSearch(arr, key):
    for ii in range(len(arr)):
        if key == arr[ii]:
            return ii
    return -1


print(LinearSearch(arr, 0))
	