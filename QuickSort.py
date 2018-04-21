def partition(myArray,low,high):
    ii = low-1
    pivot = myArray[high]
    for jj in range(low,high):

        # Test condition
        if myArray[jj] <= pivot:

            #increment index of smaller element
            ii+= 1

            #swap ii with jj index
            myArray[ii],myArray[jj] = myArray[jj],myArray[ii]
    myArray[ii+1],myArray[high] = myArray[high],myArray[ii+1]
    return (ii+1)
            



def quickSort(myArray,low,high):
    if low < high:

        # find the partition
        pivotIndex = partition(myArray,low,high)

        # run quick sort on top array
        myArray = quickSort(myArray,low,pivotIndex-1)
        myArray = quickSort(myArray,pivotIndex+1,high)
    return myArray
test = [10,80,30,90,40,50,70]
print(quickSort(test,0,len(test)-1))
