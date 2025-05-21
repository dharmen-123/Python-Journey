# There are three methods in constructor
# instance method
# class method
# static method 


# class Student:
#     school="VJVM"
#     grade="10th"
#     def __init__(self , name , age):
#         self.n=name
#         self.a=age
#     @classmethod
#     def update_school(cls , sch):
#         cls.school=sch
#     @classmethod
#     def update_grade(cls, grd):
#         cls.grade=grd
#     @staticmethod
#     def newmethod(x,y):
#         print(x+y)
#         print(Student.school)
#     def Show_details(self):
#         print(self.n)
#         print(self.a)
#         print(Student.school)
#         print(Student.grade)
# obj= Student("dharmendra", 20)
# obj.Show_details()
# Student.update_grade("11th")
# obj.Show_details()
# obj.newmethod(4,5)
# # Student.newmethod(5,6)
# obj1=Student("harsh", 21)
# obj1.update_grade("12th")
# obj1.update_school('VBHSS')
# obj1.Show_details()

class College:
    def __init__(self,name):
        self.name=name
        College.city="Bhopal"
    @staticmethod
    def show_details(self):
        print(self.name)
        print(College.city)

obj=College("Dharmendra")
obj.show_details(10)
College.show_details()

####### Overloading in PYthon ##########
# class Student:
#     def first(self, x,y):
#         print("hello")
#     def first(self):
#         print("hello")

# ob1=Student()
# ob1.first()