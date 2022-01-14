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
        elif sortType == "levelorder":
            self.levelorder(self.root, arr)

        print(arr)
        return arr

    def inorder(self, node, arr):
        if node is None:
            return

        self.inorder(node.left, arr)
        arr.append(node.data)
        self.inorder(node.right, arr)

    def preorder(self, node, arr):
        if node is None:
            return
        
        arr.append(node.data)
        self.preorder(node.left, arr)
        self.preorder(node.right, arr)

    def postorder(self, node, arr):
        if node is None:
            return
        
        self.postorder(node.left, arr)
        self.postorder(node.right, arr)
        arr.append(node.data)
            
    def levelorder(self, node, arr):
        queue = [node]
        front = 0
        while front < len(queue):
            curr = queue[front]
            front += 1
            if curr is not None:
                arr.append(curr.data)
                queue.append(curr.left)
                queue.append(curr.right)
                
    def contains(self, data):
        return self.rContains(self.root, data)

    def rContains(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True

        if data > node.data:
            node = self.rContains(node.right, data)
        elif data < node.data:
            node = self.rContains(node.left, data)
            

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

    def remove(self, data):
        self.root = self.rRemove(self.root, data)

    def rRemove(self, curr, data):
        if curr is None:
            return None # data not found
        
        if data < curr.data: 
            curr.left = self.rRemove(curr.left, data)
        elif data > curr.data:
            curr.right = self.rRemove(curr.right, data)
        else: # Data found
            if curr.left is None and curr.right is None: # 0 child case
                return None
            if curr.left is not None and curr.right is not None: # Two child case
                tempNode = BSTNode() # Create dummy node to hold removed Successor
                curr.right = self.removeSuccessor(curr.right, tempNode) # Set right subtree
                curr.data = tempNode.data # Update current node's data with the successor data
            elif curr.left is not None: # 1 child case (left)
                return curr.left
            elif curr.right is not None: # 1 child case (right)
                return curr.right 

    def removeSuccessor(self, curr, tempNode):
        ''' Remove successor '''
        if curr.left is None:
            tempNode.data = curr.data
            return curr.right
        else:
            curr.left = self.removeSuccessor(curr.left, tempNode)

    def removePredecessor(self, curr, tempNode):
        if curr.right is None:
            tempNode.data = curr.data
            return curr.left
        else:
            curr.right = self.removePredecessor(curr.right, tempNode)