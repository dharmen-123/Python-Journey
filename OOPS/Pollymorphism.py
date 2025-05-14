 ########## POLYMORPHISM #########
   
   ### Method overload ###
# class A:
#     def add(self, x,y):
#         return x+y
#     def add(self, x,y,z):
#         return x+y+z

# obj=A()
# obj.add(20,4)
# obj.add(2,5,6)

class A:
    def add(self,* n):
        sum=0
        for i in n:
            sum=sum+i
        print(sum)
obj=A()
obj.add(1,2,3)