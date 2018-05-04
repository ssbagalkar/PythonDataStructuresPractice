def BubbleSort(myArray):
    for ii in range(len(myArray)):
        swapped = False
        for jj in range(len(myArray)-ii-1):
            if myArray[jj] > myArray[jj+1]:
                myArray[jj],myArray[jj+1] = myArray[jj+1],myArray[jj]
                swapped = True
       
        if swapped == False:
           break
    return myArray
    
arrayToBeSorted = [2,7,4,1,5,3]
print(BubbleSort(arrayToBeSorted))
