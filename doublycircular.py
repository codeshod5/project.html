import math
class Node:
    def __init__(self,data) :
        self.prev = None
        self.data = data
        self.next = None


def main():
    head = Node(45)
    head.next = head
    head.prev = head
    head = insertatbegin(head)
    insertatend(head)
    inserbeforepos(head,60,3)
    # inserafterpos(head,46,4)
    # inserafterpos(head,45,4)
    # printmiddle(head)
    counttingdigit(head,45)
    # head = deleteatbegin(head)
    # head = deleteatbegin(head)
    # deleteatend(head)
    # deleteatpos(head,3)
    # deleteatpos(head,3)
    reverse(head)
    print("before reversing")
    display(head)



def insertatbegin(head):
    tail = head.prev
    temp = Node(50)
    temp.next = head
    temp.prev = tail
    head.prev = temp
    tail.next = temp
    head = temp
    return head

def insertatend(head):
    tail = head.prev
    temp = Node(40)
    temp.next = tail.next
    temp.prev = tail
    tail.next = temp
    head.prev = temp
    tail = temp

def inseratpos(head,val,pos): #here before pos
    ptr = head
    index=1
    while index != pos-1:
        index+=1
        ptr = ptr.next
    # print("this is ",ptr.data)
    temp = Node(val)
    temp.next = ptr.next
    temp.prev = ptr
    ptr.next = temp
    temp.next.prev = temp

def inserafterpos(head,val,pos): #here we have to stop at pos
    ptr = head
    index=0
    while index != pos-1:
        index+=1
        ptr = ptr.next
    # print("this is ",ptr.data)
    temp = Node(val)
    temp.next = ptr.next
    temp.prev = ptr
    ptr.next = temp
    temp.next.prev = temp

def inserbeforepos(head,val,pos): #here before pos
    ptr = head
    index=1
    while index != pos-1:
        index+=1
        ptr = ptr.next
    # print("this is ",ptr.data)
    temp1 = ptr.prev
    temp = Node(val)
    temp.next = ptr
    temp.prev = temp1
    temp1.next = temp
    ptr.prev = temp
    

def deleteatbegin(head):
    if head.next == head:
        print("it is deleted")
        return None

    ptr = head
    tail = head.prev
    head = ptr.next
    head.prev = tail
    tail.next = head
    return head

def deleteatend(head):
    tail = head.prev
    ptr = tail.prev
    ptr.next = tail.next
    head.prev = ptr
    
    
def deleteatpos(head,pos):
    if pos == 1:
        deleteatbegin(head)
    else:

     ptr = head
    index = 1
    while(index != pos-1):
        index+=1
        ptr =ptr.next
    print("this is lasr=t",ptr.data)
    temp = ptr.next
    if temp.next == head:
        ptr.next = head
        head.prev = ptr
    else:
     ptr.next = temp.next
     temp.next.prev = ptr

def printmiddle(head):
    count = 5/2
    ptr = head
    
    
    index = 1
    while index != math.ceil(count):
        index+=1
        ptr = ptr.next
    if index%2 != 0:
       print("this is middle",ptr.data)

    else:
        print("this is middle",ptr.next.data)
   
    
def counttingdigit(head,searchfor):
    count =0
    ptr = head
    while True:
        if ptr.data == searchfor:
            count+=1
        ptr = ptr.next
        if ptr == head:
            break

    print("total count",count)

def reverse(head):
    if head is None:
        return
    
    tail = head.prev
    ptr = tail
    while True:
        print(ptr.data)
        if ptr == head:
            break
        ptr = ptr.prev

    

      


def display(head):
    count = 0
    ptr = head
    while True:
        print(ptr.data)
        ptr =ptr.next
        count+=1
        if ptr==head:
            break
    return count



if __name__ == "__main__":
    main()





    