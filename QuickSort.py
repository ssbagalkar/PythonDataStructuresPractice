def partition(myArray,low,high,pivotIndex):
    pivotValue = myArray[pivotIndex]
    topArrayIndex = low
    for bottomArrayIndex in range(high,pivotIndex+1,-1):
        if (myArray[bottomArrayIndex]< pivotValue):
            if (myArray[topArrayIndex] > pivotValue):

                myArray[topArrayIndex],myArray[bottomArrayIndex] = myArray[bottomArrayIndex],myArray[topArrayIndex]
                topArrayIndex+= 1
    return myArray

def quickSort(myArray,low,high):
    if high > low:
        pivotIndex = ((high-low)//2)+low

        # partition the array
        myArray = partition (myArray,low,high,pivotIndex)

        # recursively call quicksort
        myArray = quickSort ( myArray,low,pivotIndex-1)
        myArray = quickSort ( myArray,pivotIndex+1,high)

    return myArray

arrayToBeSorted = [65,72,23,36,99,20,1,44]
print("Array to be sorted:",arrayToBeSorted)
quickSortedArray = quickSort(arrayToBeSorted,0,len(arrayToBeSorted)-1)
print("Sorted Array:",quickSortedArray)

