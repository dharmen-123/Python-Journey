# ### Declaration of local variables in constructor 

a=13
class Student:
    def __init__(self, x,y):
        self.x=x
        self.y=y
        # global z 
        z=10        #Local variables
        print(z)
    def show(self):
        p=20
        print(p)
        # print(z)
        print(a)
obj=Student(10,20)
obj.show()