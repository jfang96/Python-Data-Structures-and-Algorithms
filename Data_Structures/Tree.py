class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class Tree:
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
