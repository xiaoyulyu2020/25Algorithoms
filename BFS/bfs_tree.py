
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
def getHeight(node):
    if node is None:
        return 0
    else:
        leftHeight = getHeight(node.left)
        rightHeight = getHeight(node.right)
        if leftHeight > rightHeight:
            return leftHeight + 1
        else:
            return rightHeight + 1

def currentLevelOut(root, level):
    if root is None:
        return 
    else:
        if level == 1:
            print(root.value, end = ' ')
        elif level > 1:
            currentLevelOut(root.left, level - 1)
            currentLevelOut(root.right, level - 1)

def printBFS(root):
    h = getHeight(root)
    for i in range(1, h + 1):
        currentLevelOut(root, i)

if __name__ == "__main__":
    root=Node(1)
    root.insert(2)
    root.insert(3)
    root.insert(4)
    root.insert(5)
    root.insert(6)
    
    printBFS(root)