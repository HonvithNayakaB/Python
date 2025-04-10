class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def insertion_at_begining(head):
    data=int(input("please enter the node data = "))
    new_node=node(data)
    if(head==None):
        head=new_node
    else:
        temp=head
        head=new_node
        head.next=temp
    return head

def insertion_at_end(head):
    data=int(input("please enter the node data = "))
    new_node=node(data)
    if(head==None):
        head=new_node
    else:
        temp=head
        while(temp.next!=None):
            temp=temp.next
        temp.next=new_node
    return head

def deletion_at_begining(head):
    if(head==None):
        print("the list is empty ")
    else:
        temp=head
        head=temp.next
    return head

def deletion_at_end(head):
    if(head==None):
        print("the list is empty ")
    else:
        temp=head
        while(temp.next!=None):
            temp1=temp
            temp=temp.next
        temp1.next=None
    return head

def traversing(head):
    if(head==None):
        print("the list is empty")
    else:
        temp=head
        while(temp!=None):
            print(temp.data)
            temp=temp.next

def menu ():
    print("____MENU____")
    print("1. INSERTION AT BEGINING")
    print("2. INSERTION AT END")
    print("3. DELETION AT BEGINING")
    print("4. DELETION AT END")
    print("5. TRAVERSING")
    print("6. EXIT")

head=None

menu()

while True:
    opt=input("please enter your option = ")
    if(opt=='1'):
        head=insertion_at_begining(head)
    elif(opt=='2'):
        head=insertion_at_end(head)
    elif(opt=='3'):
        head=deletion_at_begining(head)
    elif(opt=='4'):
        head=deletion_at_end(head)
    elif(opt=='5'):
        traversing(head)
    elif(opt=='6'):
        print("exiting..")
        break
    else:
        print("please enter a valid input from the menu ")
