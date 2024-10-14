class   Queues:
    def __init__(self):
        self.queue = [None]*4
        self.rear = -1
        self.front = -1
    def  enqueue(self,ele):
        if self.rear == 3:
            print("overlfow")
        else:
            if self.front == -1:
                self.front = 0
            
            self.rear += 1
            self.queue [self.rear]= ele
    
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("underflow")
        else:
            print(self.queue[self.front])
            self.front+=1



queue = Queues()

while True:
    print("1: enqueue")
    print("2: dequeue")
    print("3: exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        ele = int(input("Enter element to enqueue: "))
        queue.enqueue(ele)
    elif choice == 2:
        queue.dequeue()
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")