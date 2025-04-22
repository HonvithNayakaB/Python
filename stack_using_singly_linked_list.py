import time
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#all operations are performed at the end
def push(head):
    data=int(input("please enter the node data = "))
    new_node=Node(data)
    if(head==None):
        head=new_node
    else:
        temp=head
        while(temp.next!=None):
            temp=temp.next
        temp.next=new_node
        print("element pushed successfully")
    return head

def pop(head):
    if(head==None):
        print("the stack is underflow")
    elif(head.next==None):
        head=None
        print("element poped successfully")
    else:
        temp=head
        while(temp.next!=None):
            temp2=temp
            temp=temp.next
        temp2.next=None
        print("element poped successfully")
    return head

def travers(head):
    if(head==None):
        print("the stack is underflow")
    else:
        temp=head
        while(temp!=None):
            print(temp.data)
            temp=temp.next
    
def peak(head):
    if(head==None):
        print("the stack is underflow")
    else:
        temp=head
        print(temp.data)
    
head=None
print("____MENU____")
print("1. PUSH AND ELEMENT")
print("2. POP AN ELEMENT")
print("3. TRAVERS THE STACK")
print("4. PEAK INTO THE STACK")
print("5. EXIT")
while True:
    opt=int(input("plese enter your option = "))
    if(opt==1):
        start_time=time.time()
        head=push(head)
        end_time=time.time()
        print("the time taken to preform the push operation is = ",end_time-start_time)
    elif(opt==2):
        start_time=time.time()
        head=pop(head)
        end_time=time.time()
        print("the time taken to prefrom the pop operation is = ",end_time-start_time)
    elif(opt==3):
        start_time=time.time()
        travers(head)
        end_time=time.time()
        print("the time take to travers through the stack is = ",end_time-start_time)
    elif(opt==4):
        start_time=time.time()
        peak(head)
        end_time=time.time()
        print("the time taken to peak from the stack is = ",end_time-start_time)
    elif(opt==5):
        print("exiting..")
        break;
    else:
        print("please enter the valid input from the menu")