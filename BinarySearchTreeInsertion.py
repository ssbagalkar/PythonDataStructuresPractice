# Python program to demonstrate insert operation in binary search tree 
 
# A utility class that represents an individual node in a BST
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key