#  Those variable which are not not depend on the class or object that is called static or class variables


class Student:
    school="VJVM"
    def __init__(self , name , age):
        self.name=name
        self.age=age
        Student.city='Bhopal'
    def add_more(self):
        Student.greed='10th'

obj=Student('Dharmendra',20)
obj.add_more()
print(obj.school)
Student.school2='EFS'
print(Student.school)
print(Student.city, Student.greed)