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

test = [2,3,4,10,40]
print(binarySearch(test,0,len(test)-1,10))

#Complexity is O(logn)

