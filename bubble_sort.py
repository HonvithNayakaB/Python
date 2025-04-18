def create():
    n=int(input("please enter the lenght of the list = "))
    l1=[]
    for i in range(n):
        element=int(input("please enter the element = "))
        l1.append(element)
    print("\n unsorted list =",l1)
    return l1

def bubble_sort(l1):
    n=len(l1)
    for i in range(n):
        for j in range(0,n-i-1):
            if l1[j]>l1[j+1]:
                l1[j],l1[j+1]=l1[j+1],l1[j]
    print("\nsorted list =",l1)

l1=create()
bubble_sort(l1)
