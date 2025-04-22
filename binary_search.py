import time
import matplotlib.pyplot as plt
import numpy as np
def create():
    n=int(input("please enter the lenght of the list = "))
    l1=[]
    for i in range(n):
        element=int(input("please enter the element = "))
        l1.append(element)
    l1.sort()
    return l1

def binary_search(l1,target):
    high=len(l1)-1
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
target=int(input("\nplease enter the element to find = "))
start_time=time.time()
result=binary_search(l1,target)
end_time=time.time()
times=end_time-start_time
if(result!=-1):
    print("the element is found at index = ",result)
else:
    print("the element is not found in the list")
print("the time taken to search for the element is = ",times)

elements=[]
for i in range(6):
    elements.append(i*500)

times=[]

for i in range(6):
    l1=np.random.randint(1,500,i*500).tolist()
    target=np.random.randint(1,500)
    start_time=time.time()
    binary_search(l1,target)
    end_time=time.time()
    total_time=end_time-start_time
    times.append(total_time)

plt.plot(elements,times,label="binary search")
plt.xlabel("number of elements")
plt.ylabel("time taken")
plt.grid()
plt.show()