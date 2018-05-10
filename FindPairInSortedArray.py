# Find a pair with given sum in sorted array
# If found display the 2 numbers else display -1

arr = [1, 2, 5, 8, 14]

sumToFind = 8


def findPairInSortedarray(arr, sumToFind):
    leftIndex = 0
    rightIndex = len(arr) - 1

    for ii in range(len(arr)):

        if leftIndex >= rightIndex:
            print("-1")
        else:
            currentSum = arr[leftIndex] + arr[rightIndex]
            # Check if sum of left index and right index is equal to sumToFind.
            # and return the 2 numbers.
            if currentSum == sumToFind:
                print(arr[leftIndex], arr[rightIndex])
                break

            if sumToFind < currentSum:
                rightIndex -= 1

            if sumToFind > currentSum:
                leftIndex += 1


findPairInSortedarray(arr, sumToFind)