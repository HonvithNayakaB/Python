def create():
    n=int(input("please enter the linght of the list = "))
    l1=[]
    for i in range(n):
        element=int(input("please enter the element = "))
        l1.append(element)
    return l1

def linear_search(l1):
    target=int(input("\nplease enter the element to find= "))
    n=len(l1)
    for i in range(n):
        if(l1[i]==target):
            return i
    return -1

l1=create()
result=linear_search(l1)
if(result!=-1):
    print("\nthe number if found at index ",result)
else:
    print("\nthe number is not found in the list ")         
