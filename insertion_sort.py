def create():
    n=int(input("please enter the size of the list = "))
    l1=[]
    for i in range(n):
        element=int(input("please enter the element = "))
        l1.append(element)
    print("\n unsorted list = ",l1)
    return l1

def insertion_sort(l1):
    n=len(l1)
    for i in range(1,n):
        while (l1[i]<l1[i-1] and i>0):
            l1[i],l1[i-1]=l1[i-1],l1[i]
            i-=1
    print("\n sorted list = ",l1)

l1=create()
insertion_sort(l1)