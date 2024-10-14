class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def createnode(inp):
    return Node(inp)

def get_height(root):
    if root == None:
        return -1
    else:
        return root.height


def leftrotate(root):
    newroot = root.right
    temp = newroot.left
    newroot.left = root
    root.right = temp

    root.height = max(get_height(root.left), get_height(root.right)) + 1
    newroot.height = max(get_height(newroot.left), get_height(newroot.right)) + 1
    return newroot


def rightrotate(root):
    newroot = root.left
    temp = newroot.right
    newroot.right = root
    root.left = temp

    root.height = max(get_height(root.left), get_height(root.right)) + 1
    newroot.height = max(get_height(newroot.left), get_height(newroot.right)) + 1
    return newroot


def get_balance(root):

    if root == None:
        return 0
    else:
        return get_height(root.left) - get_height(root.right)


def search(root,child):
    if root is None:
        return createnode(child)
    
    if child < root.data:
        root.left = search(root.left,child)
        
        
    if child > root.data:
        root.right = search(root.right,child)
    
    root.height = max(get_height(root.left), get_height(root.right)) + 1

    balance = get_balance(root)

    if balance>1 and child < root.left.data:
        return rightrotate(root)
    
    if balance<-1 and child > root.right.data:
        return leftrotate(root)
    
    if balance>1 and child > root.left.data:
        root.left = leftrotate(root.left)
        return rightrotate(root)
    
    if balance<-1 and child< root.right.data:
        root.right = rightrotate(root.right)
        return leftrotate(root)
    


    return root


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
   

if __name__ == "__main__":
    main()