
stacks = [None]*4
top = -1

def push(ele):
    global top
    if top == 3:
        print("overflow")
    else:
        top+=1
        stacks[top] = ele

real = top
def pop(top):
    
    if top == -1:
        print("underflow")
    else:
        if top ==real:
            return
        else:

          print(stacks[top],end=" ")
          top+=1
          pop(top)


        



while True:
    print("1: push")
    print("2: pop")
    print("3: exit")
    choice = int(input("enter the choice"))

    if choice == 1:
        ele = (input())
        push(ele)
    elif choice == 2:
        pop(0)
    elif choice ==  3:
        print("exiting...")
    else:
        print("invalid..")



# class Stack:
#     def __init__(self):
#         self.stacks = [None] * 4
#         self.top = -1

#     def push(self, ele):
#         if self.top == 3:
#             print("overflow")
#         else:
#             self.top += 1
#             self.stacks[self.top] = ele

#     def pop(self):
#         if self.top == -1:
#             print("underflow")
#         else:
#             print(self.stacks[self.top])
#             self.stacks[self.top] = None
#             self.top -= 1

# # Create a stack instance
# stack = Stack()

# while True:
#     print("1: for push")
#     print("2: for pop")
#     print("3: for exit")
#     choice = int(input("Enter your choice: "))
    
#     if choice == 1:
#         ele = int(input("Enter element to push: "))
#         stack.push(ele)
#     elif choice == 2:
#         stack.pop()
#     elif choice == 3:
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice. Please enter 1, 2, or 3.")


#stacks using oops




