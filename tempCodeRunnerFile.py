    index=int(input("please enter the position you want to insert starting from 1 = "))
                if (index <= len(mylist)):
                    value=int(input("please enter a value to insert = "))
                    mylist.insert(index-1,value)
                    print("operation successful \nhere is the updated list = ",mylist)
                    return mylist
                else:
                    print("\n please enter a valid position of the list \n")