# Write one call multiple it is known as function 
# Code reusability 
# print(10,20,sep=",")

# Variable is a container that holds the reference of objects
# that why python is called call by reference
# Literals holds the object values 

# class Addtocart:
#     def __init__(self):
#         self.items={}

#     def additem(self,kname, vname):
#         self.items[kname]=vname

#     def showcart(self):
#         print(self.itmes)

# obj=Addtocart()
# obj.additem("vivo",40000)
# obj.showcart()


#######   Full stack Projects   #######

#  Landing Pages
#  Login
#  Registration
#  User Account or Dashboard
#  Admin Panel
#  Item adds Dynamic
#  Subscription for required sites
#  Cloudnary Data
#  Inventry management for ecommerce
#  Validation
#  Authentication & Permision
#  APIs for connecting frontend & Backend
#  Models , Relations 
#  Deployment , Hosting

# a=3
# b=2
# print(a//b)
# c1=2+3j
# c2=5
# print(int(c1.real))
# print(int(abs(c1)))
# print(len(dir(c1)))
# print(c1+c2)
# com1=int(c1)
# print("Complex to int :",com1)
# c3=5
# com=complex(c3)
# print("Int to complex :",com)

# nums=[-10,5,-2]
# a=sorted(nums,key=abs)
# print(a)

###### String Methods ########
st="hello Every1 mY name is Dharmendra CHILHATE 20 @ / _ " 
 ### String Case Conversion methods ###
# print("capitalize: ",st.capitalize())
# print("title: ",st.title())
# print("upper: ",st.upper())
# print(st.lower())
# print(st.casefold())
# print(st.swapcase())

### String Search & Position Methods
# print(st.find('z')) #first occurence
# print(st.rfind('z')) #last occcurence
# print(st.index('E')) #
# print(st.rindex('E'))

#### Validation method ####
# s = "Python3"
# print(s.isalnum())      # True
# print(s.isalpha())      # False
# print(s.isdigit())      # False
# print(s.islower())      # False
# print(s.isupper())      # False
# print(s.isspace())      # False
# print(s.istitle())      # True
# print(s.isidentifier())

# s = "python.py"
# print(s.startswith("py"))   # True
# print(s.endswith(".py"))    # True

# s = "apple banana apple"
# print(s.count("apple"))  # 2
# print(s.split())         # ['apple', 'banana', 'apple']
# print(s.split("a"))      # ['', 'pple b', 'n', 'n', ' ', 'pple']
# print(s.rsplit(" ", 1))  # ['apple banana', 'apple']


# x=10
# print(bin(x))
# print(oct(x))
# print(hex(x))

# x1=0O12
# x2=0Xb
# print(bin(x1))
# print(hex(x1))
# print(oct(x))
# print(bin(x2))
# print(x1,x2)

## Indentity Operator
x,y,z=4,6,3
# print(x,y,z)
# print(x is y)
# print(x is not y)

### Bitwise Operator
# AND  &
# OR |
# Bitwise not ~
# Bitwise X-OR ^
# left shift <<
# right shift >>

x=7
y=10
print(x & y)
print(x | y)
print(~y)
print(~x)
print(x^y)
print(x<<2)
print(y>>2)

