class node:
    def __init__(self,data):
        self.data=data
        self.prv=None
        self.next=None

def insertion_at_begining(head):
    data=int(input("please enter the data for the node = "))
    new_node=node(data)
    if(head==None):
        head=new_node
    else:
        temp=head
        head=new_node
        temp.prv=head
        head.next=temp
    print("successfully added a node ")
    return head

def insertion_at_end(head):
    data=int(input("please enter the data for the node = "))
    new_node=node(data)
    if(head==None):
        head=new_node
    else:
        temp=head
        while(temp.next!=None):
            temp=temp.next
        temp.next=new_node
        new_node.prv=temp
    print("successfully added a node ")
    return head

def deletion_at_begining(head):
    if(head==None):
        print("the list is empty")
    else:
        temp=head
        head=temp.next
        head.prv=None
    print("successfully added a node ")
    return head

def deletion_at_end(head):
    if(head==None):
        print("the list is empty")
    else:
        temp=head
        while(temp.next!=None):
            temp=temp.next
        temp=temp.prv
        temp.next=None
    print("successfully added a node ")
    return head

def traversing(head):
    if(head==None):
        print("the list is empty")
    else:
        temp=head
        while(temp!=None):
            print(temp.data)
            temp=temp.next
        
head=None
print("____MENU____")
print("1. INSERTION AT BEGINING")
print("2. INSERTION AT END")
print("3. DELETION AT BEGINING")
print("4. DELETION AT END")
print("5. TRAVERSING")
print("6. END ")

while True:
    opt=int(input("please enter your option = "))
    if(opt==1):
        head=insertion_at_begining(head)
    elif(opt==2):
        head=insertion_at_end(head)
    elif(opt==3):
        head=deletion_at_begining(head)
    elif(opt==4):
        head=deletion_at_end(head)
    elif(opt==5):
        traversing(head)
    elif(opt==6):
        print("exiting..")
        break
    else:
        print("please enter a valid input..")
