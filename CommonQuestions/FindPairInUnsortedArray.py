arr = [4, 5, 2, 1, 0, -4, -5]

sumToFind = 0


'''
###This solution will not work as we need orderedDict

def findPairInUnsortedArray(arr, sumToFind):
    complementDict = {}
    found = False


    for ii in range(len(arr)):

        complementDict[arr[ii]] = sumToFind - arr[ii]

        # Check if current value is present in value in dictionary

        if arr[ii] in complementDict.values():
            index = list(complementDict.values()).index(arr[ii])
            print(arr[ii], end=' ')
            print(list(complementDict.keys())[index])
            found = True
            break

    if not found:
        print(-1)
		'''
# arr = [2,4,1,6,5,40,-1]
#
# sumToFind = 40
from collections import OrderedDict



def FindSumInUnSortedArray(arr,sumToFind):
    myDict = OrderedDict()
    found = False
    for ii in range(len(arr)):
        myDict[arr[ii]] = sumToFind - arr[ii]
        if arr[ii] in list(myDict.values())[:-1]:
            found = True
            print(sumToFind - arr[ii],end=" ")
            print(arr[ii])
            break
    if not found:
        print(-1)




FindSumInUnSortedArray(arr,sumToFind)



