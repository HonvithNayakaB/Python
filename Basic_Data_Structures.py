def list():
    mylist=[]
    def append_a_value (mylist):
        value=int(input("please enter a value to append = "))
        mylist.append(value)
        print("operation successful \nhere is the updated list = ",mylist)
        return mylist
    
    def insert_a_value (mylist):
        index=int(input("please enter the position you want to insert starting from 1 = "))
        value=int(input("please enter a value to insert = "))
        mylist.insert(index-1,value)
        print("operation successful \nhere is the updated list = ",mylist)
        return mylist

    def extend_the_list (mylist):
        mylist2=[]
        size=int(input("please enter the number of elements you want to extend at a time"))
        for i in range (size):
            element=int(input(f"please enter the {i+1} element = "))
            mylist2.append(element)
        mylist.extend(mylist2)
        print("operation successful \nhere is the updated list = ",mylist)
        return mylist

    def remove_an_element (mylist):
        value=int(input("please enter a value to remove"))
        if(value in mylist):
            mylist.remove(value)
            print("operation successful \nhere is the updated list = ",mylist)
        else:
            print("element not found")
        return mylist

    def pop_an_element (mylist):
        index=int(input("please enter the index of the value to pop = "))
        mylist.pop(index-1)
        print("operation successful \nhere is the updated list = ",mylist)
        return mylist

    print("""____LIST_MENU____
          1. APPEND A VALUE TO LIST
          2. INSERT A VALUE TO LIST
          3. EXTEND THE LIST
          4. REMOVE AN ELEMENT
          5. POP AND ELEMENT
          6. EXIT""") 
    while True:
        option=int(input("please enter your option = "))
        if(option==1):
            mylist=append_a_value(mylist)
        elif(option==2):
            mylist=insert_a_value(mylist)
        elif(option==3):
            mylist=extend_the_list(mylist)    
        elif(option==4):
            mylist=remove_an_element(mylist)
        elif(option==5):
            mylist+pop_an_element(mylist)
        elif(option==6):
            print("EXITING FROM THE LIST MENU \nENTERED THE MAIN MENU") 
            break
        else:
            print("please enter a valid option from the menu")  

list()