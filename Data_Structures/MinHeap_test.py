# MaxHeap TEST
import unittest
from MinHeap import MinHeap

class MaxHeapMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.heap = MinHeap()

    def test_add(self):
        arr = [8, 3, 1, 6, 4, 7, 10, 14, 13, 13]
        for num in arr:
            self.heap.add(num)
        
        self.assertEqual(self.heap.arr, [None, 1, 4, 3, 8, 6, 7, 10, 14, 13, 13])

    def test_remove(self):
        arr = [8, 3, 1, 6, 4, 7, 10, 14, 13, 13]
        for num in arr:
            self.heap.add(num)
        
        self.heap.remove()
        self.assertEqual(self.heap.arr, [None, 3, 4, 7, 8, 6, 13, 10, 14, 13])
        self.heap.remove()
        self.assertEqual(self.heap.arr, [None, 4, 6, 7, 8, 13, 13, 10, 14])
        self.heap.remove()
        self.assertEqual(self.heap.arr, [None, 6, 8, 7, 14, 13, 13, 10])
        self.heap.remove()
        self.assertEqual(self.heap.arr, [None, 7, 8, 10, 14, 13, 13])
        self.heap.remove()
        self.assertEqual(self.heap.arr, [None, 8, 13, 10, 14, 13])
        self.heap.remove()
        self.assertEqual(self.heap.arr, [None, 10, 13, 13, 14])
        self.heap.remove()
        self.assertEqual(self.heap.arr, [None, 13, 14, 13])
        self.heap.remove()
        self.assertEqual(self.heap.arr, [None, 13, 14])


        


if __name__ == '__main__':
    unittest.main()