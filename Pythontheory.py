# Write one call multiple it is known as function 
# Code reusability 
# print(10,20,sep=",")


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
