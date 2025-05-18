
#### instance variables 

class Student:
    def __init__(self,name,city):
         self.x=name    ## Declaration of instance variables inside the class
         self.y=city    ## Declaration of instance variables inside the class
    def show(self):
        print(self.x,self.y)
obj=Student("dhamendra","BPL")
obj1=Student("Amit","MDDP")
obj.z=10       ## Declaration of instance variables outside the class
print(obj.z)
print(obj.x)
print(obj.y)
obj.show()


# If you want access and declare the instance variable inside the class self keyword is used 

# class Student:
#     x=10
#     def add(self):
#         print("from add method:")
# class Child(Student):
#     print(Student.x)
#     def new(self):
#         Student.add(self)
# obj=Child()
# print(obj.x)
# obj.new()

# class Student:
#     __x=10
#     def __add(self):
#         print("from add method:")
# class Child(Student):
#     # print(Student.__x)
#     # def new(self):
#     #     Student.__add(self)
#     pass
# # obj=Child()
# # print(obj.__x)
# # obj.__add()
# print(dir(Student))


