class MaxHeap:
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

    def add(self, data):
        self.arr.append(data)
        self.upheap(self.size())

    def upheap(self, index):
        if index == 1:
            return

        parentIndex = self.parent(index)
        # If curr higher priority than parent, swap. Else, terminate
        if self.arr[index] > self.arr[parentIndex]: 
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
        # Determine highest valued child
        if rightIndex < self.size() and self.arr[rightIndex] > self.arr[leftIndex]:
            largestChildIndex = rightIndex
        else: 
            largestChildIndex = leftIndex

        # If highest valued child is greater than current, swap. Else, terminate.
        if self.arr[largestChildIndex] > self.arr[index]:
            self.arr[largestChildIndex], self.arr[index] = self.arr[index], self.arr[largestChildIndex]
        else:
            return

        self.downheap(largestChildIndex)
        
