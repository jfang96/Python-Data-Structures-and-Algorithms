class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Print the Linked List
    def print_list(self):
        currVal = self.head
        while currVal is not None:
            print(currVal.data)
            currVal = currVal.next

    # Add element to beginning of Linked List
    def add_first(self, value):
        newNode = Node(value)
        # Set new node's next value to head
        newNode.next = self.head
        # Set head.prev as new Node
        if self.head is not None:
            self.head.prev = newNode
        # Set head to new node
        self.head = newNode

    # Add element to end of Linked List
    def add_last(self, value):
        newNode = Node(value)
        # If no items in list, set head as new new node
        if self.head is None:
            self.head = newNode
            return
        # Get to last node in the List
        lastNode = self.head
        while lastNode.next is not None:
            lastNode = lastNode.next
        # Add the node to end
        lastNode.next = newNode
        newNode.prev = lastNode
        
    # Insert element after target value
    def add_after(self, targetValue, value):
        # Check if list is empty
        if self.head is None:
            raise Exception("List is empty")

        newNode = Node(value)
        # Iterate through list to get to targetValue's node
        targetNode = self.head
        while targetNode.data is not targetValue:
            targetNode = targetNode.next
        # Remember targetNode's next
        tempNode = targetNode.next
        # Set targetNode's next as newNode
        targetNode.next = newNode
        # Set newNode's next as the previously remembered node
        newNode.next = tempNode
        newNode.next.prev = newNode
        newNode.prev = targetNode

    # Remove value from Linked List
    def remove(self, removeValue):
        # Iterate through list to get removeValue's node
        removeNode = self.head
        while removeNode.data is not None:
            if removeNode.data is removeValue:
                break
            prev = removeNode
            removeNode = removeNode.next

        # removeValue is not in the List
        if removeNode is None:
            return
        
        prev.next = removeNode.next
        removeNode.data = None

        

list1 = LinkedList()
list1.add_first("first")
list1.add_last("last")
list1.add_last("last2")
list1.add_last("last3")
list1.add_after("first", "second")
list1.remove("last")


list1.print_list()