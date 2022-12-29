
class Node:
    def __init__(self, value):
        self.value = None
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value == None:
            self.value = value
        else:
            if value >= self.value:
                self.right = self.insert(value)
            else:
                self.left = self.insert(value)
    
def getHeight(node):
    if node.value is None:
        return 0
    else:
        leftHeight = getHeight(node.left)
        rightHeight = getHeight(node.right)
        if leftHeight > rightHeight:
            return leftHeight + 1
        else:
            return rightHeight + 1

def currentLevelOut(root, level):
    if root is 