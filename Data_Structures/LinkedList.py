class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Print the Linked List
    def print_list(self):
        currVal = self.head
        values = []
        while currVal is not None:
            values.append(currVal.data)
            currVal = currVal.next
        print('[' + ', '.join(values) + ']')

    # Add element to beginning of Linked List
    def add_first(self, value):
        newNode = Node(value)
        # If no items in list, set head and tail as new node
        if self.head is None: 
            self.head = newNode
            self.tail = newNode
        else: # Set new node's next value to head
            newNode.next = self.head
            # Set head to new node
            self.head = newNode
        self.size += 1


    # Add element to end of Linked List
    def add_last(self, value):
        newNode = Node(value)
        # If no items in list, set head and tail as new node
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else: # Simply set tail of the List to new node
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    # Remove first element
    def remove_first(self):
        eleData = None
        if self.size == 0:
            return eleData
            
        if self.size == 1: 
            self.head = None
            self.tail = None
        else:
            eleData = self.head.data
            self.head.data = None
            self.head = self.head.next
        self.size -= 1
        return eleData

    # Remove last element
    def remove_last(self):
        eleData = None
        if self.size == 0: 
            return eleData

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            curr = self.head
            while curr.next != self.tail:
                curr = curr.next
            eleData = self.tail.data
            curr.next = None
            self.tail.data = None
            self.tail = curr
        self.size -= 1
        return eleData