import mysql.connector

mydb= mysql.connector.connect(
        host="localhost",
        user="root",
        password="honvith",
        database="cefa_management"
        )

mycursor=mydb.cursor()

def fetch_menu():
    mycursor.execute("SELECT * FROM menu")  
    rows = mycursor.fetchall()  # Get all rows as a list of tuples

    menu = {}
    for row in rows: 
        item = row[0]  # Extract item name (first column)
        price = row[1]  # Extract price (second column)
        menu[item] = price

    menu_keys=list(menu.keys())
    menu_values=list(menu.values())

    return menu,menu_keys,menu_values 


def change_menu(menu):
    print("___MENU___")
    print("1. change the price of the specific item")
    print("2. add a new item ")
    print("3. remove an item")
    print("4 display menu")
    print("5. exit")

    while True:
        opt=int(input("please enter you option"))
        if(opt==1):
            print(menu)
            item=input("please enter the item name")
            if (item in menu):
                price=float(input(f"please enter the new price for {item} = "))
                mycursor.execute("update menu set price = %s where menu_item = %s",(price,item))
                mydb.commit()
                print("price changed successfully")
            else:
                print(f"the item with the name {item} is not found")

            
        elif(opt==2):
            new_item=input("please enter the name of the new item = ")
            price=float(input("please enter the price of the new item = "))
            mycursor.execute("insert into menu values(%s,%s)",(new_item,price))
            mydb.commit()
            print("the new item has been added successfully")
            

        
        elif(opt==3):
            item=input("please enter the item name")
            if (item in menu):
                mycursor.execute("delete from menu where menu_item = %s",(item,))
                mydb.commit()
                print("the item has been deleted successfully")
            else:
                print(f"the item with the name {item} is not found")
            
                
        elif(opt==4):
            menu=fetch_menu()
            print(menu)
        
        elif(opt==5):
            print("exiting from the sub menu ")
            break
        
        
        else:
            print("invalid option please enter a valid option")


def menu_print(menu_keys,menu_values):
    print("____MENU____")
    print("    ITEM     |    PRICE")
    for i in range (len(menu_keys)):
        print(i+1,"  ",menu_keys[i],"    =    ",menu_values[i])

def take_order(menu_keys,menu_values):
    dict={}
    while True:
        opt=int(input("please enter the menu item number you want to order = "))
        if(opt==1):
           number=int(input("how much do you want to order  ="))
           price=numbers*menu_values[opt-1]
           dict.
    
menu,menu_keys,menu_values=fetch_menu()
menu_print(menu_keys,menu_values)
