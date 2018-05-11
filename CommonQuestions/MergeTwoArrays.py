# Merge 2 sorted arrays of different sizes

#Time
#complexity is O(n)


def mergeTwoSortedArrays(arr1, arr2):
    sortedArray = []

    ii = jj = 0

    while (ii < len(arr1) and jj < len(arr2)):
        if arr1[ii] < arr2[jj]:
            sortedArray.append(arr1[ii])
            ii += 1
        else:
            sortedArray.append(arr2[jj])
            jj += 1

    if ii < len(arr1):
        sortedArray.extend(arr1[ii:])

    if jj < len(arr2):
        sortedArray.extend(arr2[jj:])

    return sortedArray


arr1 = [1, 11, 15, 26, 38]
arr2 = [1, 13, 17, 30, 45]

print(mergeTwoSortedArrays(arr1,arr2))