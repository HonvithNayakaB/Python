size=10
hash_table=[[] for _ in range(size)]

def hash_function(key):
    return key%size

def insertion(key):
    index=hash_function(key)
    hash_table[index].append(key)
    print(f"success inserted {key} in hash table {[index]}")

def search(key):
    index=hash_function(key)
    if(len(hash_table[index])==0):
        print("match not found")
    else:
        found=False
        for i in hash_table[index]:
            if(i==key):
                print(f"match found for {key} in {index}")
                break
        else:
            print("match not found")
def display():
    for i in range(size):
        print(f"{i} = {hash_table[i]}")
    
print("----MENU----")
print("1. INSERTION")
print("2. SEARCH")
print("3. DISPLAY")
print("4. EXIT")

while True:
    opt=int(input("please enter your option = "))
    if(opt==1):
        key=int(input("please enter the key value = "))
        insertion(key)
    elif(opt==2):
        key=int(input("please enter the key value = "))
        search(key)
    elif(opt==3):
        display()
    elif(opt==4):
        print("breaking ..")
        break
    else:
        print("please enter a valid input")


