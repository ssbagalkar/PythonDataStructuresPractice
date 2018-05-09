arr  = [ 5, 6, 7, 8, 9, 10, 1, 2, 3 ]

def binarySearchWithRotation(arr,low, high,key):
    #base case
    if low > high:
        return -1

    # find the mid index
    midIndex = low + (high-low) // 2
    if arr[midIndex] == key:
        return midIndex

    if arr[low] <= arr[midIndex]:
        # Check if 1st array till mid is sorted and check if key is present in that part
        if key >= arr[low] and key <= arr [ midIndex ] :
            return (binarySearchWithRotation(arr,low,midIndex-1,key))
        return(binarySearchWithRotation(arr,midIndex+1,high,key))

    if key >= arr[midIndex] and key <= arr[high]:
        return (binarySearchWithRotation(arr,midIndex+1,high,key))
    return(binarySearchWithRotation(arr,low,midIndex-1,key))






print(binarySearchWithRotation(arr, 0, len(arr)-1, 1))