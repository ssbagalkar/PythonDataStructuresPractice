def SelectionSort(myArray):
	minValueIndex = 0
	for ii in range(len(myArray)):	
		for count in range(ii+1,len(myArray)):
			if myArray[count] < myArray[minValueIndex]:
				minValueIndex = count
		myArray[ii],myArray[minValueIndex] = myArray[minValueIndex],myArray[ii]
	return myArray

arrayToBeSorted = [ 32, 2, 56, 67, 30, 5, 99, 23]
print(SelectionSort(arrayToBeSorted))
