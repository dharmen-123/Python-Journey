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
# a="the army man"
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
        # Format_map   Syntax - string.format_map(dictionary)
# myvar = {"name" : "Jane", "age" : 36}
# txt = "Happy birthday {name} you are now on level {age}!"
# print(txt.format_map(myvar))

# print(a.index("man",5))

        # String join() Method
# myTuple = ("John", "Peter", "Vicky")
# x = " ".join(myTuple)
# print(x)

        # STRING METHODS 
"""
# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values from a dictionary in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Converts the elements of an iterable into a string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning
"""
# txt="Hello World"
# print(txt[2:5])
# print(txt.upper())
# name="Python"
# print(f"I love {name}")

# x = "Hello"
# y = 15
# print(bool(x))
# print(bool(y))
# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool(()))
# print(bool([]))
# print(bool({}))

        # ARITHMETIC Operator #
""" 
Operator	Name	Example	
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	        x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y
"""
# x = 15
# y = 4

# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x % y)
# print(x ** y)
# print(x // y)

        # ASSIGNMENT OPERATOR #
""" 
Operator     Example	  Same As	
=	     x = 5	  x = 5	
+=	     x += 3	  x = x + 3	
-=	     x -= 3	  x = x - 3	
*=	     x *= 3	  x = x * 3	
/=	     x /= 3	  x = x / 3	
%=	     x %= 3	  x = x % 3	
//=	     x //= 3	  x = x // 3	
**=	     x **= 3	  x = x ** 3	
&=	     x &= 3	  x = x & 3	
|=	     x |= 3	  x = x | 3	
^=	     x ^= 3	  x = x ^ 3	
>>=	     x >>= 3	  x = x >> 3	
<<=	     x <<= 3	  x = x << 3	
"""

                # Comparison Operators
""" 
Operator      Name	             Example	
==	      Equal	             x == y	
!=	      Not equal	             x != y	
>	      Greater than	     x > y	
<	      Less than	             x < y	
>=	      Greater than or equal to	x >= y	
<=	      Less than or equal to	x <= y
"""
# x = 5
# y = 3
# print(x == y)
# print(x != y)
# print(x > y)
# print(x < y)
# print(x >= y)
# print(x <= y)

                # Logical Operators
""" 
Operator   Description	                                             Example
and 	   Returns True if both statements are true	             x < 5 and  x < 10	
or	   Returns True if one of the statements is true             x < 5 or x < 4	
not	   Reverse the result, returns False if the result is true   not(x < 5 and x < 10)
"""

        # Identity Operators
"""
is      Return true if both varibale are same object
is not  Return True if both variable are not the same object
"""
# x=10
# y=10
# print(x is y)
# print(x is not y)
# x = [1, 2, 3]
# # y = [1, 2, 3]
# y=x
# print(id(x))
# print(id(y))
# print(x == y)
# print(x is y)

        # Membership Operators
""" 
in 
not in 
"""

        # Bitwise Operators
""" 
& AND
| OR
^ XOR
~ NOT
<< Left Shift
>> Right Shift
"""

        # Operator Precedence
""" 
Operator	Description	Try it
()	        Parentheses	
**	        Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	        Addition and subtraction	
<<  >>	        Bitwise left and right shifts	
&	        Bitwise AND	
^	        Bitwise XOR	
|	        Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	        Logical NOT	
and	        AND	
or	        OR

Left-to-Right Evaluation
If two operators have the same precedence, the expression is evaluated from left to right.
"""

        ##             LIST         ##

# thislist = ["apple", "banana", "cherry"]
# print(thislist)
# x=" ".join(thislist)
# print(x)
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

"""
                #Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)
# thislist.insert(2, "watermelon")
# print(thislist)
# print(thislist.pop())
# print(thislist)
# thislist.remove("orange")
# print(thislist)
# del thislist[2]
# print(thislist)
# thislist.clear()
# print(thislist)

                # LIST Comprehension
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)
""" 
The Syntax
newlist = [expression for item in iterable if condition == True]
"""

"""              # LIST METHODS #
Python has a set of built-in methods that you can use on lists.
Method	        Description
append()	Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	        Sorts the list
"""

"""     # TUPLE  Method#
Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found

"""

# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

"""                     # SET  #
Join Sets
There are several ways to join two or more sets in Python.
The union() and update() methods joins all items from both sets.
The intersection() method keeps ONLY the duplicates.
The difference() method keeps the items from the first set that are not in the other set(s).
The symmetric_difference() method keeps all items EXCEPT the duplicates.

Method	        Shortcut	Description
add()	 	                Adds an element to the set
clear()	 	                Removes all the elements from the set
copy()	 	                Returns a copy of the set
difference()	     -	        Returns a set containing the difference between two or more sets
difference_update()  -=	        Removes the items in this set that are also included in another, specified set
discard()	 	        Remove the specified item
intersection()	     &	        Returns a set, that is the intersection of two other sets
intersection_update() &=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	        Returns True if NO items of this set is present in another set
issubset()	      <=	Returns True if all items of this set is present in another set
 	           <	        Returns True if all items of this set is present in another, larger set
issuperset()       >=	        Returns True if all items of another set is present in this set
 	           >	        Returns True if all items of another, smaller set is present in this set
pop()	 	                Removes an element from the set
remove()	 	        Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update() ^=Inserts the symmetric differences from this set and another
union()	                |	Return a set containing the union of sets
update()	        |=	Update the set 

"""

"""             # PYTHON MATCH Statement #
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block

"""

