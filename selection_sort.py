def create():
    n=int(input("please enter the size of the list ="))
    l1=[]
    for i in range(n):
        element=int(input("please enter the element = "))
        l1.append(element)
    print("\n unsorted list = ",l1)
    return l1

def selection_sort(l1):
    n=len(l1)
    for i in range(n):
        for j in range(i+1,n):
            if(l1[i]>l1[j]):
                l1[i],l1[j]=l1[j],l1[i]
    print("\nsorted list = ",l1)

l1=create()
selection_sort(l1)
