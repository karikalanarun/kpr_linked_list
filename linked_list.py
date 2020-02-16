class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, item):
        if self.head == None and self.tail == None:
            self.head = self.tail = Node(item)
        else:
            self.tail.next = self.tail = Node(item)
    def __str__(self):
        if self.head == self.tail:
            return "[" + str(self.head) +"]"
        else:
            return "[" + str(self.head) + ", "+str(self.tail) +"]"

a =  LinkedList()
a.append(5)
a.append(6)
a.append(7)
print(a)
