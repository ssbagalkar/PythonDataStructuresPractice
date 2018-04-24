# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr,arrSize,currentNode):
    # Determine which is the largest node currently
    largestIndex = currentNode # Initialize root

    # Determine the left and right child node indexes of currentNode
    leftChild = 2 * currentNode + 1
    rightChild = 2 * currentNode + 2

    # 1.Check if left child is not out of bounds AND if values of left child is greater than
    # currentNode which is its parent,move largest pointer to left child
    if leftChild < arrSize and arr[leftChild] > arr[largestIndex]:
        largestIndex = leftChild

    # 2.Check if right child is not out of bounds AND if values of right child is greater than
    # currentNode which is its parent,move largest pointer to right child

    if rightChild < arrSize  and arr[rightChild] > arr[largestIndex]:
        largestIndex = rightChild

    #If largest index has changed, swap
    if largestIndex != currentNode:
        arr[largestIndex], arr[currentNode] = arr[currentNode],arr[largestIndex]

        # Now,very important make sure all children of currentNode are also following max heap
        heapify(arr,arrSize,largestIndex)

def heapSort(myArray):
    arrSize = len(myArray)

    #Build a maxheap
    for ii in range(arrSize,-1,-1):
        heapify(myArray,arrSize,ii)

    # One by one extract elements
    for ii in range(arrSize - 1, 0, -1):
        myArray[ii], myArray[0] = myArray[0], myArray[ii]  # swap
        heapify(myArray, ii, 0)

myArray = [1, 5, 6, 8, 12, 14, 16]
heapSort((myArray))
print(myArray)