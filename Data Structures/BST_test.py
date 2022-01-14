# BST TEST
import unittest
from BST import BST

class TestBSTMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.bst = BST()

    def test_add(self):
        arr = [8, 3, 1, 6, 4, 7, 10, 14, 13, 13]
        for num in arr:
            self.bst.add(num)
        
        self.assertEqual(self.bst.display(), [1, 3, 4, 6, 7, 8, 10, 13, 14])

    def test_remove(self):
        return

    def test_traversals(self):
        arr = [4, 2, 6, 1, 3, 5, 7]
        for num in arr:
            self.bst.add(num)

        self.assertEqual(self.bst.display("inorder"), [1, 2, 3, 4, 5, 6, 7], "inorder traversal wrong")
        self.assertEqual(self.bst.display("preorder"), [4, 2, 1, 3, 6, 5, 7], "preorder traversal wrong")
        self.assertEqual(self.bst.display("postorder"), [1, 3, 2, 5, 7, 6, 4], "postorder traversal wrong")
        self.assertEqual(self.bst.display("levelorder"), [4, 2, 6, 1, 3, 5, 7], "levelorder wrong")
        return

    def test_contains(self):
        arr = [4, 2, 6, 1, 3, 5, 7]
        for num in arr:
            self.bst.add(num)

        self.assertTrue(self.bst.contains(4)) # Check root
        self.assertTrue(self.bst.contains(5)) # Check left leaf
        self.assertTrue(self.bst.contains(2)) # Check left parent
        self.assertTrue(self.bst.contains(3)) # Check right leaf

        self.assertFalse(self.bst.contains(8)) 
        self.assertFalse(self.bst.contains(0))

if __name__ == '__main__':
    unittest.main()