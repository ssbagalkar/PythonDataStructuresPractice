def BubbleSort(myArray):
    k = 0
    for ii in range(len(myArray)):
        for jj in range(len(myArray)-k-1):
            if myArray[jj] > myArray[jj+1]:
                myArray[jj],myArray[jj+1] = myArray[jj+1],myArray[jj]
        k =+ 1
    return myArray
    
arrayToBeSorted = [2,7,4,1,5,3]
print(BubbleSort(arrayToBeSorted))
