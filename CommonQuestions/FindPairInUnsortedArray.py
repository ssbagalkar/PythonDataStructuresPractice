arr = [4, 5, 2, 1, 0, -4, -5]

sumToFind = -5


def findPairInUnsortedArray(arr, sumToFind):
    complementDict = {}
    found = False


    for ii in range(len(arr)):

        complementDict[arr[ii]] = sumToFind - arr[ii]

        # Check if current value is present in value in dictionary

        if arr[ii] in complementDict.values():
            index = list(complementDict.values()).index(arr[ii])
            print(arr[ii], end=' ')
            print(list(complementDict.keys())[index])
            found = True
            break

    if not found:
        print(-1)
findPairInUnsortedArray(arr, sumToFind)

