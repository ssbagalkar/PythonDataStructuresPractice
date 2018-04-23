class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == []

    def push(self, item):
        self.items.append(item)

    def popItem(self):
        if not self.isEmpty():
            self.items.pop()

    def maxItem(self):
        return (max(self.items))


myStack = Stack()
numQueries = int(input())
for _ in range(numQueries):
    currentInput = list(input().split())
    if currentInput[0] == '1':
        myStack.push(int(currentInput[1]))
    elif currentInput[0] == '2':
        myStack.popItem()
    else:
        print(myStack.maxItem())