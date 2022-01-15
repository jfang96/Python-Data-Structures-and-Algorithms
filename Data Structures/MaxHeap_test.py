# MaxHeap TEST
import unittest
from MaxHeap import MaxHeap

class MaxHeapMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.heap = MaxHeap()

    def test_add(self):
        arr = [8, 3, 1, 6, 4, 7, 10, 14, 13, 13]
        for num in arr:
            self.heap.add(num)
        
        self.assertEqual(self.heap.arr, [None, 14, 13, 8, 10, 13, 1, 7, 3, 6, 4])

    def test_remove(self):
        arr = [8, 3, 1, 6, 4, 7, 10, 14, 13, 13]
        for num in arr:
            self.heap.add(num)
        
        self.heap.remove()
        self.assertEqual(self.heap.arr, [None, 13, 13, 8, 10, 4, 1, 7, 3, 6])
        self.heap.remove()
        self.assertEqual(self.heap.arr, [None, 13, 10, 8, 6, 4, 1, 7, 3])
        self.heap.remove()
        self.assertEqual(self.heap.arr, [None, 10, 6, 8, 3, 4, 1, 7])
        self.heap.remove()
        self.assertEqual(self.heap.arr, [None, 8, 6, 7, 3, 4, 1])
        self.heap.remove()
        self.assertEqual(self.heap.arr, [None, 7, 6, 1, 3, 4])
        self.heap.remove()
        self.assertEqual(self.heap.arr, [None, 6, 4, 1, 3])
        


if __name__ == '__main__':
    unittest.main()