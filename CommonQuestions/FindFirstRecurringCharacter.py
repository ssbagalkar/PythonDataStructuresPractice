
# Find First Recurring character in a string
# https://www.youtube.com/watch?v=GJdiM-muYqc
# Below implement is using lists. The *in* has average complxity of 0(n) in list.
# So using dictionary, which has average complexity of O(1), for *in* is much better

## Using Lists
#
# def findFirstRecurringCharacter(myString): myList=[]
#     for ii in range(len(myString)):
#         if myString[ii] in myList:
#             return myString[ii]
#         else:
#             myList.append(myString[ii])

# Using Dictionary
def findFirstRecurringCharacter(myString):
    myDictionary = {}
    for char in (myString):
        if char in myDictionary:
            return char
        else:
            myDictionary[char] = 1


print(findFirstRecurringCharacter(('DBCADB')))