   #Constructor overload
#    Python support Method overriding
#    Python does not support method Overloading
         
# class Parent:
#     def __init__(self, bank , house):
#         self.bank=bank
#         self.house=house
# class C(Parent):
#     def __init__(self, bank1 , house1):
#         self.bank1=bank1
#         self.house1=house1

#     def show_details(self):
#         print(self.bank ,self.bank1)
#         print(self.house ,self.house1)
    
# obj=Parent("SBI", "MP")
# obj1=C("RBI", "India")
# obj1.show_details()

####################################################

# class Parent:
#     def add(self):
#         print("add from parent")
#     def __init__(self, bank ,branch):
#         self.bank=bank
#         self.branch=branch

# class C(Parent):    
#     def show_details(self):
#         super().add()
#         print(self.bank ,self.branch)
#     def add(self):
#         print("add from child")
# obj=C  
# obj1=C("RBI","MP")
# obj1.show_details()
# obj1.add()

          ######## Method Overloading ##########

# class Parent:
#     def add(self):
#         print("add from parent")
#     def __init__(self, bank ,branch):
#         self.bank=bank
#         self.branch=branch

# class C(Parent):    
#     def add(self):
#         super().add()
#         print(self.bank ,self.branch)
#     def add(self):
#         print("add from child")
# obj=C  
# obj1=C("RBI","MP")
# # obj1.show_details()
# obj1.add()


     ###### TYpes of Inheritance ######

#### SINGLE INHERITANCE ######
    #    |``````````|
    #    |  Parent  |
    #    `````|``````
    #         |
    #         V
    #    |``````````|
    #    |   Child  |
    #    ````````````

# class A:
#     def first(self):
#         print("first class")
# class B(A):
#     def second(self):
#         print("second class")
# obj=B()
# obj.first()
# obj.second()

  ##### MultiLevel Inheritance #####
#    |``````````|
#    |  Grand   |
#    `````|``````
#         V
#    |``````````|
#    |  Parent  |
#    `````|``````
#         V
#    |``````````|
#    |   Child  |
#    ````````````

# class A:
#     def first(self):
#         print("first class")
# class B(A):
#     def second(self):
#         print("second class")
# class C(B):
#     def third(self):
#         print("third class")
# obj=C()
# obj.first()
# obj.second()

  ##### Multiple Inhertance ######

#    |``````````|          |``````````|
#    |  Grand   |          |  Grand   |
#    `````|``````          `````|``````
#         |________   __________|
#                  |  |
#                  V  V
#              |``````````|
#              |  Grand   |
#              ````````````

####### Heirarchical Inheritance ######

class Parent:
    def home(self):
       print("from parent Home")
    def bank(self):
       print("from parent bank")
class Child1(Parent):
     pass
class Child2(Parent):
     pass
obj1=Child1()
obj2=Child2()
obj1.home()
obj1.bank()
obj2.home()
obj2.bank()