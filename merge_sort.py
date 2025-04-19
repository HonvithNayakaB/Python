def create ():
    n=int(input("please enter the length of the array = "))
    l1=[]
    for i in range (n):
        element=int(input("please enter the element = "))
        l1.append(element)
    print("\n unsorted array = ",l1)
    return (l1)

def merge_sort(l1):
    n=len(l1)
    if(n>1):
        left_arr=l1[:n//2]
        right_arr=l1[n//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i=0
        j=0
        k=0

        while(i<len(left_arr) and j<len(right_arr)):
            if(left_arr[i]<right_arr[j]):
                l1[k]=left_arr[i]
                i+=1
            else:
                l1[k]=right_arr[j]
                j+=1
            k+=1

        while(i<len(left_arr)):
            l1[k]=left_arr[i]
            i+=1
            k+=1

        while(j<len(right_arr)):
            l1[k]=right_arr[j]
            j+=1
            k+=1

    return l1

l1=create()
print("\nsorted array = ",merge_sort(l1))