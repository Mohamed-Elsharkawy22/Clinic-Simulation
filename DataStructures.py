class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


###########################################################################################
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


#############################################################################################
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        current = self.head
        previous = None
        while current != None:
            if current.getData() > item:
                break
            previous = current
            current = current.getNext()
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        while current != None:
            if current.getData() == item:
                return True
            if current.getData() > item:
                return False
            current = current.getNext()
        return False

    def remove(self, item):
        previous = None
        current = self.head
        while current != None:
            if current.getData() == item:
                break
            previous = current
            current = current.getNext()
        if previous == None:
            self.head = self.head.getNext()
        else:
            previous.setNext(current.getNext())

    def index(self, item):
        current = self.head
        idx = 0
        while current != None:
            if current.getData() == item:
                return idx
            idx += 1
            current = current.getNext()

    def pop(self, pos=None):
        if pos == None:
            current = self.head
            while current.getNext().getNext() != None:
                current = current.getNext()
            temp = current.getNext().getData()
            current.setNext(None)
            return temp
        else:
            if pos == 0:
                temp = self.head.getData()
                self.head = self.head.getNext()
                return temp
            idx = 0
            current = self.head
            while idx != pos - 1:
                idx += 1
                current = current.getNext()
            temp = current.getNext().getData()
            current.setNext(current.getNext().getNext())
            return temp

    def print(self):
        current = self.head
        while current != None:
            print(current.getData(), end=" ")
            current = current.getNext()
        print(" ")


class UnorederedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        temp = Node(item)
        if self.head == None:
            self.tail = temp
        temp.setNext(self.head)
        self.head = temp

    def append(self, item):
        temp = Node(item)
        temp.setNext(None)
        self.tail.setNext(temp)

    def print(self):
        current = self.head
        while current != None:
            print(current.getData(), end=" ")
            current = current.getNext()
        print(" ")

########################################

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.left = None
        self.right = None
        self.size = 0

    def length(self):
        return self.size


    def insertLeft(self, newNode):
        if self.left is None:
            self.left = BinaryTree(newNode)
        else:
            tempNode = BinaryTree(newNode)
            tempNode.left = self.left
            self.left = tempNode
    def insertRight(self,newNode):
        if self.right is None:
            self.right = BinaryTree(newNode)
        else:
            tempNode = BinaryTree(newNode)
            tempNode.left = self.left
            self.left = tempNode

    def getNodeVal(self):
        return self.key

    def getLefChild(self):
        return self.left

    def getRightChild(self):
        return self.right


if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push("hello")
    my_stack.push("world")
    print("size:", my_stack.size())
    print(my_stack.peek())
    print(my_stack.pop())
    print(my_stack.pop())
    print("isEmpty:", my_stack.isEmpty())
    temp = Node(93)
    var = 55
    print(temp.getData())
    print(temp.getNext())
    temp.setData(22)
    temp.setNext(var)
    print(temp.getData())
    print(temp.getNext())

    ul = UnorederedList()
    ul.add(3)
    ul.add(5)
    ul.add(9)
    ul.print()
    ul.append(222)
    print("**************************************")
    ul = OrderedList()
    ul.add(5)
    ul.add(3)
    ul.add(18)
    ul.add(9)
    ul.print()
    print("**************************************")
    print(ul.search(1))
