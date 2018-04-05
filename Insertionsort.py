def InsertionSort(myArray):
    for ii in range(len(myArray)):
        currentValue = myArray[ii]

        j = ii - 1
        while( currentValue < myArray[j] and j >= 0):
            myArray[j+1] = myArray[j]
            j -= 1
        myArray[j+1] = currentValue
    return myArray  



arrayToBeSorted = [55, 2, 9, 34, 99, 1, 67, 44]
print(InsertionSort(arrayToBeSorted))

