# There are three methods in constructor
# instance method
# class method
# static method 


class Student:
    school="VJVM"
    grade="10th"
    def __init__(self , name , age):
        self.n=name
        self.a=age
    @classmethod
    def update_school(cls , sch):
        cls.school=sch
    @classmethod
    def update_grade(cls, grd):
        cls.grade=grd
    @staticmethod
    def newmethod(x,y):
        print(x+y)
    def Show_details(self):
        print(self.n)
        print(self.a)
        print(Student.school)
        print(Student.grade)
obj= Student("dharmendra", 20)
obj.Show_details()
Student.update_grade("12th")
obj.Show_details()
obj.newmethod(4,5)
# Student.newmethod(5,6)
