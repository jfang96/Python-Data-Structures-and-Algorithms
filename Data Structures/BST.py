class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def display(self, sortType = "inorder"):
        arr = []

        if sortType == "inorder":
            self.inorder(self.root, arr)
        elif sortType == "preorder":
            self.preorder(self.root, arr)
        elif sortType == "postorder":
            self.postorder(self.root, arr)
            
        print(arr)

    def inorder(self, node, arr):
        if node is None:
            return

        self.inorder(node.left, arr)
        arr.append(node.data)
        self.inorder(node.right, arr)
            

    def add(self, data):
        '''  Add the data as a leaf in the BST. Should traverse the tree to find
         the appropriate location. If the data is already in the tree, then
         nothing should be done (the duplicate shouldn't get added, and size
         should not be incremented).

         Should have a running time of O(log n) for a balanced tree, and a
         worstcase of O(n).

         Args:
         data -- data to add
         '''
        self.root = self.rAdd(self.root, data)

    def rAdd(self, curr, data):
        ''' Recursive helper method for add '''
        if curr is None:
            self.size += 1
            return BSTNode(data)
        if data < curr.data:
            curr.left = self.rAdd(curr.left, data)
        elif data > curr.data:
            curr.right = self.rAdd(curr.right, data)
        return curr