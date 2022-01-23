# AVL TEST
import unittest
from AVL import AVL

class TestAVLMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.avl = AVL()

    def test_add(self):
        arr = [8, 3, 1, 6, 4, 7, 10, 14, 13, 13]
        for num in arr:
            self.avl.add(num)
        
        self.assertEqual(self.avl.display(), [1, 3, 4, 6, 7, 8, 10, 13, 14])

    def test_remove(self):
        arr = [8, 3, 1, 6, 4, 7, 10, 14, 13]
        for num in arr:
            self.avl.add(num)

        self.avl.display()
        self.avl.remove(8)
        self.assertEqual(self.avl.display("levelorder"), [6, 3, 10, 1, 4, 7, 13, 14])
        self.assertEqual(self.avl.display(), [1, 3, 4, 6, 7, 10, 13, 14])
        self.avl.display()
        

    def test_traversals(self):
        arr = [4, 2, 6, 1, 3, 5, 7]
        for num in arr:
            self.avl.add(num)

        self.assertEqual(self.avl.display("inorder"), [1, 2, 3, 4, 5, 6, 7], "inorder traversal wrong")
        self.assertEqual(self.avl.display("preorder"), [4, 2, 1, 3, 6, 5, 7], "preorder traversal wrong")
        self.assertEqual(self.avl.display("postorder"), [1, 3, 2, 5, 7, 6, 4], "postorder traversal wrong")
        self.assertEqual(self.avl.display("levelorder"), [4, 2, 6, 1, 3, 5, 7], "levelorder wrong")
        return

    def test_contains(self):
        arr = [4, 2, 6, 1, 3, 5, 7]
        for num in arr:
            self.avl.add(num)

        self.assertTrue(self.avl.contains(4)) # Check root
        self.assertTrue(self.avl.contains(5)) # Check left leaf
        self.assertTrue(self.avl.contains(2)) # Check left parent
        self.assertTrue(self.avl.contains(3)) # Check right leaf

        self.assertFalse(self.avl.contains(8)) 
        self.assertFalse(self.avl.contains(0))

if __name__ == '__main__':
    unittest.main()