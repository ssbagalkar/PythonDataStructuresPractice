# Binary Search Tree
# Here all children to right of parent are greater than parent and
# all nodes to left of parent are smaller than parent

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# A utility function to search a given key in BST
def search(root, key):
    # Base Cases: root is null or key is present at root
    if root is None:
        return str(key) + " Not Found"
    if root.value == key :
        return str(key) + " Found"

    # Key is greater than root's key
    if key > root.value:
        return search(root.right,key)

    # Key is smaller than root's key
    return search(root.left,key)


root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right = Node(14)
root.right.right.left = Node(13)

print(search(root, 11))