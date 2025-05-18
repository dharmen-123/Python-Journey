# constructor is a special type of magic method which calls automatically after making object
#constructor is used to initialize the variable

# class Home:
#     def _init_(self,name,contact,address):   ## self is a reference variable which holds the address of current class of current object
#         print("Constructor called")
#         self.n=name      
#         self.c=contact
#         self.a=address
#         print(id(self))
# obj1=Home('Name',123,'Bhopal')
# # obj1._init_('Harsh',345,'india')
# print(id(obj1))
# print(obj1.n)
# print(obj1.c)
# print(obj1.a)


# variables :-
# -> instance variable
# -> static/class variable
# ->local variable

#  object badalne ke sath apni value baadal dee
# variables which changes there values with there declaration  are instance variables 
# variables which only accessible in blocks are local variables
# 


# class Student:
#     school='SHSS'   ##static or class variable
#     def _init_(self,name,email,add):
#         self.n=name
#         self.e=email
#         self.a=add
#     def Show_details(self):
#         principal_name='python'  ##local variable
#         print(self.n,self.e,self.a)
# obj=Student('Harsh','harsh14thakre@gmail.com','Bhopal')
# obj.Show_details()
# print(obj.school)     
# print(obj.a,obj.n,obj.e)



class A:    
    def __init__(self,a,b):
        # print("Hello.")
        # print(id(self))
        self.a = a   # declare inside constructors
        self.b = b
        print(self.a) # access inside constructors
    # def _init_(self,a,b,e):
    #     # print("Hello.")
    #     # print(id(self))
    #     self.a = a   # declare inside constructors
    #     self.b = b 
    def new(self,c):
        print("Hi..")
        print(self.a) # access inside instence menthod
        self.c = c  # declare inside instence menthod
    
    def new1(self):
        print(self.d)
        print(self.e)
obj = A(2,4)
# print(id(obj))
obj.new(10)
print(obj.a)
print(obj.b)
print(obj.c)    # access outside of the class
obj.d = 100     # declare outside of the class
obj.e="hello"
obj.new1()
