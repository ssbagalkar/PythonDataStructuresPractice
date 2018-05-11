
# Find all possible permutations of given string assuming there are no duplicates
# Complexity: O(n * n!) --> n distinct items each with n! permutations
def convertToString(myList):
    return ''.join(myList)


def permute(myList, leftIndex, rightIndex):
    if leftIndex == rightIndex:
        print(convertToString(myList))

    else:
        for ii in range(leftIndex, rightIndex + 1): # remember we loop through rightIndex + 1
            # swapping
            myList[ii], myList[leftIndex] = myList[leftIndex], myList[ii]
            
            #recursion
            permute(myList, leftIndex + 1, rightIndex)
            
            # backtracking
            myList[ii], myList[leftIndex] = myList[leftIndex], myList[ii]


myString = "ABC"
myList = list(myString)
n = len(myList)

permute(myList, 0, n - 1) # remember we are permuting till true right index