        #   PYTHON REVISION     #
"""
# Python is the popullar programming language
# It is created by the Guido van Rossum in 1991
# used for web dev (server side application)
software development
machine learning 
AI and Automation 

"""
# print("Hello Python ")

# for check the python version of editor we can find it by importing the sys module
# import sys
# print(sys.version)

# Run the python file using Terminal 
# Syntax to run the file - "python file_name.py"

        # PYTHON INDENTATION #
# Indentation refers to the spaces at the beginning of a code line.
# Python uses indentation to indicate a block of code.

        # PYTHON VARIABLE #
# in python varibale is created to assign the value

# x=10
# name="Ram"
# greet="Good Morning"
# print(x)
# print(name," ",greet)

            # Python Statements #
# A computer program is a list of instruction to be executed by computer
# these instruction are called statements
# print("Python is machine language")

        # Semicolons (Optional, Rarely Used)
# print("Python is fun!");print("have a good day");print("good evening")

        # PYTHON OUTPUT / Print
# we use the print() function in python to display the output
# print("I am learning Python")

        # Print Without a New Line
"""By default, the print() function ends with a new line.
If you want to print multiple words on the same line, you can use the end parameter"""

# print("Hello Ravi!",end=" ")
# print("Nice to meet you.")

        # PRINT NUMBERS 
# print(345)
# print(245898)

        # PYTHON COMMENTS #
"""comments can be used to explain the Python code 
comment start with # ans python  will ignore them
"""
# this is the python program 
# print("Jai shree ram")  # it is print statement

    # Multiline Comments #
"""
We can add the multiline string comment using (triple quotes)
"""

      # PYTHON VARIABLES #
# x=23
# print(x)
# name="Raju"
# surname='Tiwari'
# print(name ,surname)

        # VARIABLE NAMES
"""A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
"""
# _my_name="Shivansh"
# percent100=95
# print(_my_name,percent100)

# Different case for variable name
# 1.Camel Case - myVariableName="John"
# 2.Pascal Case - MyVariableName="John"
# 3.Snake Case - my_variable_name ="John"

        # Assign Multiple Values

# x,y,z = "apple","Orange","Cherry"
# print(x,y,z)
# a=b=c="Gamer"
# print(a,b,c)
# fruits=["chiku","lichi","Gavava"]
# m,n,o=fruits
# print(m)
# print(n)
# print(o)

            # Global Variables
# Variable that are created outside the function are known as global variable
# Global variable are by everyone both inside and outside the function 

# x="Learning"    # Global variable
# def func():     
#     print("Machine "+x)

# func()

"""
Create a variable inside a function, with the same name as the global variable
"""
# a=10
# y="Hello"
# def fun():
#   a=20
#   print("sum",a+10,y)
#   a+=5

# fun()
# print(a)

            # GLOBAL KEYWORD #
"""
To create a global variable inside a function, you can use the global keyword.
"""
# def vari():
#     global x
#     x="Awesome"

# vari()
# print("Python is" ,x)

# #####################################
# x = "awesome"
# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()
# print("Python is " + x)

        #  DATA TYPES IN PYTHON #
"""
str , int , float , complex, list , tuple , range , set , frozenset , dict , bool , NoneType
"""
# x=2
# print(type(x))
# a=None
# print(type(a))
# z=frozenset({'A','C','T','C','G'})
# print(z)
# print(type(z))

            # PYTHON STRINGS #
#  string in python are declared by single and double qoutes ,marks
