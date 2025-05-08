# Object= physical existance of class is known as object
# Class= class is a blueprint of object
# To add real world entity in our programming language

# Syntax of class
######Class name should be write in capital letters
# Class  Class_Name:   
#       "doc string"
#        variables(properties)
#         methods(behaviour)

# class is a blueprint of object which holds the properties and behavior of object.

# Variables:-
# -> class variable/static variabe
# -> instance variable
# -> local variable

# Methods:-
# -> Instance method
# -> Class method
# -> Static method



# class Calculator:
#     x=10             ##variable
#     def add(x,y):    ##method
#         return x+y
# obj=Calculator
# z=obj.add(10,20)
# print(z)   

class Calculator:
    x=10
    def add(x,y):
        return x+y
obj=Calculator
z=obj.add(10,20)
print(obj.x)