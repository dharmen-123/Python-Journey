   #Constructor overload
         
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


class Parent:
    def __init__(self, bank , house):
        self.bank=bank
        self.house=house
class C(Parent):
    

    def show_details(self):
        print(self.bank ,self.bank1)
        print(self.house ,self.house1)
obj=C  
obj1=C()
