class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, key):
        if self.value:
            if key >= self.value:
                if self.right is None:
                    self.right = Node(key)
                else:
                    self.right.insert(key)
            else:
                if self.left is None:
                    self.left = Node(key)
                else:
                    self.left.insert(key)
        else:
            self.value = key

def inorder_print(root):
    if root:
        inorder_print(root.left)
        print(root.value, end=" ")
        inorder_print(root.right)
        
if __name__=="__main__":
    root = Node(1)
    root.insert(2)
    root.insert(3)
    root.insert(4)
    root.insert(5)
    root.insert(6)
    root.insert(7)
    inorder_print(root)