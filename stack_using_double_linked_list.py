class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prv=None

#all the operations are performed at the begining

def push(head):
    data=int(input("please enter the node data = "))
    new_node=Node(data)
    if(head==None):
        head=new_node
    else:
        temp=head
        head=new_node
        head.next=temp
        temp.prv=head
        print("successfully pushed one element")
    return head

def pop(head):
    if(head==None):
        print("the stack is underflow")
    else:
        temp=head
        head=temp.next
        if (head!=None):
            head.prv=None
        print("successfully poped one element")
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
print("-____MENU____-")
print("1. PUSH A ELEMENT")
print("2. POP A ELEMENT")
print("3. TRAVERS THE STACK")
print("4. PEAK INTO STACK")
print("5. EXIT")
while True:
    opt=int(input("please enter you option from the menu = "))
    if(opt==1):
        head=push(head)
    elif(opt==2):
        head=pop(head)
    elif(opt==3):
        travers(head)
    elif(opt==4):
        peak(head)
    elif(opt==5):
        print("exiting..")
        break;
    else:
        print("please enter the valid input from the menu")
