# Properties of OOPs

##   1 Inheritence
##   2 Polymorphishm
##   3 abstraction
##   4 Encapsulation

# Encapsulation is defined as the wrrapup variables and method into a single unit

# class Python:
#     school= "SWS"
#     def __init__(self , name):
#         self.name=name
#     def show_details(self):
#         print(self.name)
#         print(Python.school)

# obj=Python("Dharmendra")

class First:
    "for demo purpose "
    x=10
    y=20
    # @staticmethod
    def new(self):
        print("hello")
        print(id(self))
    # pass
# print(len(dir(First)))
print(First.__module__)
print(First.__doc__)
print(First.__dict__)
print(id(First))

obj=First()
print(id(obj))
obj.new()
