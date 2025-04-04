def list():
    mylist=[]
    def append_a_value (mylist):
        while True:
            try:
                value=int(input("please enter a value to append = "))
                mylist.append(value)
                print("operation successful \nhere is the updated list = ",mylist)
                return mylist
            except ValueError:
                print("\nPlease enter a valid integer number of base 10 \n")
    
    def insert_a_value (mylist):
        while True:
            try:
                index=int(input("please enter the position you want to insert starting from 1 = "))
                if (index <= len(mylist)):
                    while True:
                        try:
                            value=int(input("please enter a value to insert = "))
                            mylist.insert(index-1,value)
                            print("operation successful \nhere is the updated list = ",mylist)
                            return mylist
                        except ValueError:
                            print("\n please entera a valid integer of base 10\n")
                else:
                    print("\n please enter a valid position of the list \n")
            except ValueError:
                print("\n please enter a valid position number of base 10\n ")

    def extend_the_list (mylist):
        mylist2=[]
        while True:
            try:
                size=int(input("please enter the number of elements you want to extend at a time = "))
                while True:
                    try:
                        for i in range (size):
                            element=int(input(f"please enter the {i+1} element = "))
                            mylist2.append(element)
                        mylist.extend(mylist2)
                        print("operation successful \nhere is the updated list = ",mylist)
                        return mylist
                    except ValueError:
                        print("\n please enter a valid integer number of base 10\n")
            except ValueError:
                print("\n please enter a valid integer number of base 10 \n ")

    def remove_an_element (mylist):
        if(len(mylist)!=0):
            while True:
                try:
                    value=int(input("please enter a value to remove"))
                    if(value in mylist):
                        mylist.remove(value)
                        print("operation successful \nhere is the updated list = ",mylist)
                        return mylist
                    else:
                        print("\nelement not found\n")
                except ValueError:
                    print("\nplease enter a valid integer number with base 10\n")
        else:
            print("the list is empty")
            return mylist

    def pop_an_element (mylist):
        if(len(mylist)!=0):
            while True:
                try:
                    index=int(input("please enter the index of the value to pop = "))
                    mylist.pop(index)
                    print("operation successful \nhere is the updated list = ",mylist)
                    return mylist
                except ValueError:
                    print("\nplease enter a valid index from the list\n")
                except IndexError:
                    print("\nplease enter a valid index from the list\n")
        else:
            print("the list is empty")
            return mylist

    print("\n______---LIST_MENU---______\n")
    print("1. APPEND A VALUE TO LIST")
    print("2. INSERT A VALUE TO LIST")
    print("3. EXTEND THE LIST")
    print("4. REMOVE AN ELEMENT")
    print("5. POP AND ELEMENT")
    print("6. EXIT\n")
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

def tuple():
    mytuple=(5,7,2,4,7,2,9,1,5,8,3,7,0,4)
    def count(mytuple):
        while True:
            try:
                print("tuple = ",mytuple)
                value=int(input("please enter a number to count it's appirence = "))
                if(value in mytuple):
                    return mytuple.count(value)
                else:
                    print("\nthe number you entered does not exists\n")
            except ValueError:
                print("\nplease enter a valid integer of base 10 \n")

    def index(mytuple):
        while True:
            try:
                print("tuple = ",mytuple)
                value=int(input("please enter a number to finds its position = "))
                if(value in mytuple):
                    return mytuple.index(value)
                else:
                    print("\nthe number you entered does not exists\n")
            except ValueError:
                print("\nplease enter a valid integer of base 10\n")

    print("\n______---LIST_MENU---______\n")
    print("1. COUNT A NUMBER IN TUPLE")
    print("2. FIND THE INDEX OF A NUMBER IN TUPLE")
    print("3. EXITING")

    while True:
        option=int(input("please enter your option = "))
        if(option==1):
            print("the number has occured ",count(mytuple)," times")
        elif(option==2):
            print("the number is found first at position = ",index(mytuple))
        elif(option==3):
            print("breaking..")
            break;
        else:
            print("please enter a valid option")

tuple()