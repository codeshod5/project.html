class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.queue = [None]*100
        self.front = -1
        self.rear = -1
    def enqueue(self,inp):
        if self.queue == 99:
            print("overflow")
        else:
            if self.front == -1:
                 self.front = 0
            else:
                self.rear += 1
                self.queue[self.rear] = inp
    def dequeue(self):
        if self.front == -1 or self.front>self.rear:
            print("underflow")
        else:
            temp = self.queue[self.front]
            self.front += 1
            return temp
    def bfs(self, root):
        if root is None:
            return
        self.enqueue(root)
        while self.front <= self.rear:
            current = self.dequeue()  # Dequeue the current node
            if current:
                print(current.data)  # Process the current node
                if current.left is not None:
                    self.enqueue(current.left)
                if current.right is not None:
                    self.enqueue(current.right)


def createnode(inp):
    return Node(inp)

def search(root,parent):
    if root is None:
        return
    if root.data==parent:
        return root
    leftside = search(root.left,parent)
    if leftside is not None:

        return leftside
    rightside = search(root.right,parent)
    if rightside is not None:
        return rightside

def insertatbt(root,parent,child,whichchild):
    
    parent = search(root,parent)

    if parent is None:

        print("parent node not found ")
        return 
    

   # Insert the child node as the left or right child based on `whichchild`
    if whichchild == 1:
        if parent.left is None:
            parent.left = createnode(child)
        else:
            print(f"Left child of parent {parent} is already occupied.")
    elif whichchild == -1:
        if parent.right is None:
            parent.right = createnode(child)
        else:
            print(f"Right child of parent {parent} is already occupied.")
    else:
        print("Invalid value for whichchild. Use 1 for left and -1 for right.")

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def findheight(root):
    if root is None:
        return -1
    
    lefthe = findheight(root.left)
    rigthe = findheight(root.right)

    if lefthe>rigthe:
        return lefthe+1
    else :
        return rigthe+1

def main():
    root = Node(10)
    insertatbt(root, 10, 5, 1)  # Insert 5 as the left child of 10
    insertatbt(root, 10, 2, -1)  # Insert 15 as the right child of 10
    insertatbt(root, 5, 3, 1)  # Insert 3 as the left child of 5
    insertatbt(root, 5, 7, -1)  # Insert 7 as the right child of 5
    inorder(root)
    print(findheight(root))
    print("this is bfs traversal ")
    root.bfs(root)

    # print(f"this is minn {findminmax(root)}")
    # Try to insert a node to a non-existent parent
    # insertatbt(root, 20, 8, 1)  # Should print an error message
if __name__ == "__main__":
    main()
    
    

# def findminmax(root):
#     minn = 10
#     if root == None:
#         return
#     else:
#         findminmax(root.left)
#         if(root.data < minn):
#             minn = root.data
#         findminmax(root.right)
#     return minn

# class Solution:
#     def __init__(self):
#         self.minn = float('inf')  # Initialize the minimum value to infinity

#     def findminmax(self, root):
#         if root is None:
#             return
#         # Update the minimum value
#         if root.data < self.minn:
#             self.minn = root.data
#         # Recur for left and right children
#         self.findminmax(root.left)
#         self.findminmax(root.right)

#         return self.minn
  


def findmax(root):
    # Base case: if the tree is empty, return the smallest possible value
    if root is None:
        return float('-inf')
    
    # Recursively find the maximum value in the left and right subtrees
    left_max = findmax(root.left)
    right_max = findmax(root.right)
    
    # Return the maximum of the current node's data, left subtree max, and right subtree max
    return min(root.data, left_max, right_max)

    
    






        