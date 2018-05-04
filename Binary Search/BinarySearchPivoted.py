def binarySearch(myArray,low,high,x):
    if high >= low:
        # Find the midvalue
        midValueIndex = low + (high-low)//2
        midValue = myArray[midValueIndex]
        if midValue == x:
            return midValueIndex

        if x > midValue:
            return(binarySearch(myArray,midValueIndex + 1, high,x))
        elif x < midValue:
            return(binarySearch(myArray,low,midValueIndex-1,x))

    else:
        return -1



def findPivot(myArray):
    ii = 0
    while(ii <= len(myArray)-2):
        if myArray[ii] > myArray[ii+1]:
            return ii
        ii += 1
    return -1


def binarySearchPivoted(myArray,low,high,x):
    # search for pivotIndex
    pivotIndex = findPivot(myArray)
    if pivotIndex == -1:
        return(binarySearch(myArray,low,high,x))
    pivotValue = myArray[pivotIndex]
    if pivotValue == x:
        return pivotIndex

    if pivotValue > x:
        return(binarySearch(myArray,pivotIndex+1,high,x))
    else:
        return(binarySearch(myArray,low,pivotIndex-1,x))

test = [3,4,5,1,2]

print(binarySearchPivoted(test,0,len(test)-1,2))
