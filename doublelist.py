class Node:
    def __init__(self,data) :
        self.prev = None
        self.data = data
        self.link = None


def main():
    head = Node(10)
    head = insertatbegin(head,20) 
    head = insertatbegin(head,30) 
    nsertend(head,80)
    # head =deletatfirst(head)
    # delteatend(head)
    insertbeforepos(head,90,80)
    display(head)



def delteatend(head):
    ptr = head
    while ptr.link != None:
        ptr = ptr.link
    temp = ptr.prev
    temp.link = ptr.link


def searchpos(head,pos):
    ptr = head
    while ptr.data != pos:
        ptr = ptr.link
    return ptr

def insertbeforepos(head,daata,pos):
    temp = searchpos(head,pos)
    ptr = Node(daata)
    ptr.prev = temp.prev
    temp.prev.link = temp
    temp.prev = ptr





def insertatbegin(head,daata):
    temp = Node(daata)
    temp.link = head
    head.prev = temp
    return temp

def nsertend(head,daata):
    temp = Node(daata)
    ptr = head
    while ptr.link != None:
        ptr = ptr.link
    temp.prev = ptr
    ptr.link = temp
    temp.link= None

def deletatfirst(head):
    temp = head
    head = temp.link
    head.prev = None
    return head
def display(head):
    ptr = head
    while ptr != None:
        print(ptr.data)
        ptr= ptr.link
    

if __name__ == "__main__":
    main()
    