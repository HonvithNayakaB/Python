def create():
    n=int(input("please enter the lenght of the list = "))
    l1=[]
    for i in range(n):
        element=int(input("please enter the element = "))
        l1.append(element)
    l1.sort()
    return l1

def binary_search(l1):
    target=int(input("\nplease enter the element to find = "))
    high=len(l1)
    low=0
    while(high>=low):
        mid=(high+low)//2
        if(l1[mid]==target):
            return mid
        elif(l1[mid]>target):
            high=mid-1
        else:
            low=mid+1
    return -1

l1=create()
print("the sorted list \n ",l1)
result=binary_search(l1)
if(result!=-1):
    print("the element is found at index = ",result)
else:
    print("the element is not found in the list")