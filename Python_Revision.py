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
# x="Hello Dev"   #str
# print(x , type(x)) 
# x=23            #int
# print(x , type(x)) 
# x=20.34         #float
# print(x , type(x)) 
# x=8+1j          #complex
# print(x , type(x)) 
# x=["apple",'C',38]      #List
# print(x , type(x)) 
# x=('set', 38, "a",'Y')
# print(x , type(x)) 
# x=range(4)      #Range
# print(x , type(x)) 
# x={'name':"Dharmendra",'age':21}
# print(x , type(x)) 
# x=True
# print(x , type(x)) 
# x=bytearray(5)
# print(x , type(x))
# x=memoryview(bytes(3))
# print(x , type(x)) 
# x=None
# print(x , type(x)) 

# import random
# print(random.randrange(100,1000))

            # PYTHON STRINGS #
#  string in python are declared by single and double qoutes ,marks
# print('Jai shree ram')
# print("Har har mahadev")
# print("""Jai Mahakal""")
# print("He is called 'Ram'")
# print("Ram is \"Playing\" football")     #\ Escape character
# a=("My name is Ravi Prakash Tiwari"
#     "and I am currently doing the Btech"
#    "in the specialization of AIML"
#    "I am in my 6 th sem now with 8.4 CGPA")
# print(a)

        # STRING are Array
# a="Machine Learning"
# print(a[2])
# print(a[:10:2])

# a="Artificial Intelligence"
# for x in a:
#      print(x,end=" ")
# print("Inte" in a)

                # String Operation
# a="  hello WORLD "
# print(a.upper())
# print(a.capitalize())
# print(a.casefold())
# print(a.lower())
# print(a.strip())
# print(a.replace("h",'c'))
# print(a.split())
# flat=294
# print(f"my subject is Computer Network")

                # Strings are Arrays
# z="Database Management"
# print(z[::-1])
# z="The best things in life are happiness"
# print("free" not in z)
# print(z[-2::-1])
# a="Ram"
# b="Shyam"
# print(a+b)

        # F- STRINGS
# age=21
# print(f"My name is Raj , I am {age} year old")
# price=34
# print(f"The price is {price:.2f} dollars")

        # Escape Characters
# print("We are Celebrating the \"festival Diwali\" at this time ")

        # STRING METHODS
a="the army man"
# print(a.capitalize())
# print(a.casefold())
# print(a.center(19,'-'))
# print(a.count('a'))
# txt = "My name is Ståle"
# x = txt.encode()
# print(x)
# print(a.endswith('n'))
# txt = "H\te\tl\tl\to"
# x =  txt.expandtabs(4)
# print(x)
# print(a.find('a'))
      #  String Format
# txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# txt2 = "My name is {0}, I'm {1}".format("John",36)
# txt3 = "My name is {}, I'm {}".format("John",36)
# print(txt1)
myvar = {"name" : "Jane", "age" : 36}
txt = "Happy birthday {name} you are now on level {age}!"
print(txt.format_map(myvar))
