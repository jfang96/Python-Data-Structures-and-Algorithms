class MinHeap:
    ''' The root will have the smallest value. Priority queue implementation when priority goes to smallest value'''
    def __init__(self):
        self.arr = [None]

    def left(self, index):
        return 2 * index

    def right(self, index):
        return 2 * index + 1

    def parent(self, index):
        if index // 2 > 0:
            return index // 2
        else:
            return 1

    def size(self):
        return len(self.arr) - 1

    def isEmpty(self):
        return self.size == 0

    def add(self, data):
        ''' Add element to heap '''
        self.arr.append(data)
        self.upheap(self.size())

    def upheap(self, index):
        if index == 1:
            return

        parentIndex = self.parent(index)
        # If curr less than parent, swap. Else, terminate
        if self.arr[index] < self.arr[parentIndex]: 
            self.arr[index], self.arr[parentIndex] = self.arr[parentIndex], self.arr[index]
        else:
            return

        self.upheap(parentIndex)

    def remove(self):
        ''' Remove first element in heap (the root) '''
        data = self.arr[1]
        self.arr[1] = self.arr[self.size()] # Set root value as last element in heap
        del self.arr[self.size()] # Delete the last element in heap
        self.downheap(1) # Downheap from the root to maintain order
        return data 

    def downheap(self, index):
        leftIndex = self.left(index)
        if leftIndex > self.size(): # Terminate if at leaf (no left child)
            return

        rightIndex = self.right(index)
        # Determine lowest valued child. If right child is out of bounds, swap with left child
        if rightIndex <= self.size() and self.arr[rightIndex] < self.arr[leftIndex]:
            smallestChildIndex = rightIndex
        else: 
            smallestChildIndex = leftIndex

        # If lowest valued child is less than current, swap. Else, terminate.
        if self.arr[smallestChildIndex] < self.arr[index]:
            self.arr[smallestChildIndex], self.arr[index] = self.arr[index], self.arr[smallestChildIndex]
        else:
            return

        self.downheap(smallestChildIndex)
        
