class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def creat(root):
    data=int(input("please enter the data for the node = "))
    new_node=node(data)
    root=insertion(root,new_node)
    return root

def insertion(root,new_node):
    if(root==None):
        root=new_node
    else:
        if(new_node.data<=root.data):
            root.left=insertion(root.left,new_node)
        else:
            root.right=insertion(root.right,new_node)
    return root

def inorder(root):
    if(root==None):
        return []
    else:
        result=[]
        result.extend(inorder(root.left))
        result.append(root.data)
        result.extend(inorder(root.right))
        return result

def preorder(root):
    if(root==None):
        return []
    else:
        result=[]
        result.append(root.data)
        result.extend(preorder(root.left))
        result.extend(preorder(root.right))
        return result

def postorder(root):
    if(root==None):
        return []
    else:
        result=[]
        result.extend(postorder(root.left))
        result.extend(postorder(root.right))
        result.append(root.data)
        return result

root=None
print("____MENU____")
print("1. INSERT A NODE")
print("2. INORDER")
print("3. PREORDER")
print("4. POSTORDER")
print("5. EXIT")
while True:
    opt=int(input("please enter your option = "))
    if(opt==1):
        root=creat(root)
    elif(opt==2):
        print(inorder(root))
    elif(opt==3):
        print(preorder(root))
    elif(opt==4):
        print(postorder(root))
    elif(opt==5):
        print("exiting..")
        break
    else:
        pirnt("please enter a valid option from the menu..")