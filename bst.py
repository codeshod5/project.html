class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def createnode(inp):
    return Node(inp)

def search(root,child):
    if root is None:
        return createnode(child)
    
    if child < root.data:
        root.left = search(root.left,child)
        
        
    if child > root.data:
        root.right = search(root.right,child)

    return root



def findmin(root):
    # Keep moving to the leftmost node
    current = root
    while current.left is not None:
        current = current.left
    return current.data


    




def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.data)
    inorder(root.right)
    
def main():
    root =  createnode(4)
    root = search(root,2)
    root = search(root,1)
    root = search(root,5)
    inorder(root)
    print(findmin(root))

if __name__ == "__main__":
    main()