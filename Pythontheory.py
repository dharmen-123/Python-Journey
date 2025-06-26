# Write one call multiple it is known as function 
# Code reusability 
# print(10,20,sep=",")

# Variable is a container that holds the reference of objects
# that why python is called call by reference
# Literals holds the object values 

class Addtocart:
    def __init__(self):
        self.items={}

    def additem(self,kname, vname):
        self.items[kname]=vname

    def showcart(self):
        print(self.itmes)

obj=Addtocart()
obj.additem("vivo",40000)
obj.showcart()
