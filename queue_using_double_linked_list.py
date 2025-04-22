import time
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prv=None

# insertion at begining

def enqueue(head):
    data=int(input("please enter the node data = "))
    new_node=Node(data)
    if(head==None):
        head=new_node
    else:
        temp=head
        head=new_node
        head.next=temp
        temp.prv=head
        print("successfully enqueued a element")
    return head

#deletion at end

def dequeue(head):
    if(head==None):
        print("the queue is underflow")
    elif(head.next==None):
        head=None
        print("successfully dequeued a element")
    else:
        temp=head
        while(temp.next!=None):
            temp=temp.next
        temp=temp.prv
        temp.next=None
        print("successfully dequeued a element")
    return head

def travers(head):
    if(head==None):
        print("the queue is underflow")
    else:
        temp=head
        while(temp!=None):
            print(temp.data)
            temp=temp.next
            
def peak(head):
    if(head==None):
        print("the queue is underflow")
    else:
        temp=head
        print(temp.data)
    
head=None
print("____MENU____")
print("1. ENQUEUE")
print("2. DEQUEUE")
print("3. TRAVERS")
print("4. PEAK")
print("5. EXIT")
while True:
    opt=int(input("please enter your option = "))
    if(opt==1):
        start_time=time.time()
        head=enqueue(head)
        end_time=time.time()
        print("the time taken to to perform the enqueue operaions is = ",end_time-start_time)
    elif(opt==2):
        start_time=time.time()
        head=dequeue(head)
        end_time=time.time()
        print("the time taken to preform the dequeue operation is = ",end_time-start_time)
    elif(opt==3):
        start_time=time.time()
        travers(head)
        end_time=time.time()
        print("the time taken to travers through the queue is = ",end_time-start_time)
    elif(opt==4):
        start_time=time.time()
        peak(head)
        end_time=time.time()
        print("the time taken to peak from the queue is = ",end_time-start_time)
    elif(opt==5):
        print('exiting..')
        break
    else:
        print("print enter a valid input from the menu")
