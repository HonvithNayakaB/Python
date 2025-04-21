class listOperation:
    def __init__(self):
        self.data=[]

    def insert(self,value):
        self.data.append(value)

    def delete(self,value):
        if value in self.data:
            self.data.remove(value)

    def display(self):
        print(self.data)

lo=listOperation()
lo.insert(20)
lo.insert(30)
lo.display()
lo.delete(30)
lo.display()