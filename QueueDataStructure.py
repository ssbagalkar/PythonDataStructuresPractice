class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        print("Enqueued {}".format(item))
        self.items.insert(0,item)

    def dequeue(self):
        if self.items != []:
            print("Dequeued {}".format(self.items[-1]))
            return self.items.pop()
        else:
            print("Cannot dequeue empty queue")

    def size(self):
        return len(self.items)


q.enqueue(8)
print("Queue",q.items)
q.dequeue()
print("Queue",q.items)
q.dequeue()
q.dequeue()