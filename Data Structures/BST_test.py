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
        arr = [4, 2, 6, 1, 3, 5, 7]
        for num in arr:
            self.bst.add(num)

        self.assertEqual(self.bst.display(), [1, 2, 3, 4, 5, 6, 7])

        self.bst.remove(4) # Remove node with two children
        self.assertEqual(self.bst.display(), [1, 2, 3, 5, 6, 7], "Failed to remove node with two children")

        self.bst.remove(3) # Remove node with no children
        self.assertEqual(self.bst.display(), [1, 2, 5, 6, 7], "Failed to remove node with no children")

        self.bst.remove(2) # Remove node with only left child
        self.assertEqual(self.bst.display(), [1, 5, 6, 7], "Failed to remove node with only left child")
        
        self.bst.remove(6) # Remove node with only right child
        self.assertEqual(self.bst.display(), [1, 5, 7], "Failed to remove node with only right child")

    def test_traversals(self):
        arr = [4, 2, 6, 1, 3, 5, 7]
        for num in arr:
            self.bst.add(num)

        self.assertEqual(self.bst.display("inorder"), [1, 2, 3, 4, 5, 6, 7], "Failed inorder traversal")
        self.assertEqual(self.bst.display("preorder"), [4, 2, 1, 3, 6, 5, 7], "Failed preorder traversal")
        self.assertEqual(self.bst.display("postorder"), [1, 3, 2, 5, 7, 6, 4], "Failed postorder traversal")
        self.assertEqual(self.bst.display("levelorder"), [4, 2, 6, 1, 3, 5, 7], "Failed levelorder traversal")
        

if __name__ == '__main__':
    unittest.main()