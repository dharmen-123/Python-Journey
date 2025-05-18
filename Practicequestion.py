 #####                 #     *
 #####                 #    * *
 #####                 #   * * *
 #####                 #  * * * *
 #####                 # * * * * *

# n=int(input("Enter the number :"))
# i=1
# while(i<=n):
#     print(" "*(n-i)+" *"*i)
#     i=i+1  


               ######################################
  #####           #######       *
  #####           #######     * * *
  #####           #######   * * * * *

# n=int(input("Enter the number :"))
# i=1
# while(i<=(2*n)):
#      print(" "*(2*n-i)+" *"*i)  
#      i=i+2


######################################### 

# s="i Am dharmendra Chilhate"
# print(s.capitalize())
# print(s.count('a'))
# print(s.lower())
# print(s.upper())
# print(s.title())
# print(s.isalnum())
# print(s.replace('i','My'))

          ########################################

# s=input("Enter the String : ").lower()  
# vowel="aeiou"
# v=0
# c=0
# for i in s:
#     if i in vowel:
#         v+=1
#     else:
#        i.isalpha()
#        c+=1
# print(f"Vowel is {v} and Consonants is {c}")


   ############## COUNT THE DIGIT SMALL CAPITAL LETTER #############

# val=input("Enter the string : ")
# capital=0
# small=0
# num=0
# for i in val:
#     if i.isdigit():
#         num+=1
#     elif i.islower():
#         small+=1
#     else:
#         capital+=1
# print(capital , small , num)

# s1="python"
# s2="thyonp"
# c1=0
# c2=0
# for i in s1:
#     if i in s2:
#         c1+=1 
#         c1-=1 
# print(c1)


# input_number  = 5
# for i in range(input_number):
#     print(" " * (input_number - i) + "*" * (2*i + 1))

  ############### SPY NUMBER ##################

# n=int(input("Enter the number :"))
# x=n
# sum=0
# mul=1
# while(n>0 and x>0):
#       s=n%10
#       sum=sum+s
#       mul=mul*s
#       n=n//10
# if(mul==sum):
#    print("It is SPY number")
# else:
#    print("Not Spy number")
   
   ################## PETERSON NUMBER #########################

# n=int(input("Enter the number :"))
# pnum=n
# sum=0
# while(n>0):
#       last=n%10
#       n=n//10
#       fact=1
#       for i in range(1,last+1):
#           fact*=i
#       sum+=fact
# if(pnum==sum):
#    print("It is peterson number")
# else:
#    print("Not")   

# #         #######  * * * * * * * * *
# #         #######    * * * * * * *
# #         #######      * * * * *
# #         #######        * * *
# #         #######          *

# n=int(input("Enter the number :"))
# i=1
# while(i<=(2*n-1)):
#      print(" "*i+" *"*((2*n)-i))
#      i=i+2

  ############# SUNNY NUMBER ############

# n=(int(input("Enter the number for check sunny number :")))
# a=n
# sun=0
# sum=0
# count=0
# sum2=0
# while(n>0):
#     n=n//10
#     count+=1
# while(a>0):
#    y=a%10
#    sum=sum+y**count
#    sun+=y
#    a=a//10
# while(sum>0):
#    b=sum%10
#    sum2+=b
#    sum=sum//10
# if(sum2==sun):
#    print("sunny number")
# else:
#    print("not")



# from functools import reduce
# l=[1,2,8,4,8,5]
# def Max(x,y):
#    if(x>y):
#      return x
#    else :
#      return y
# x = reduce(Max, l)
# print(x)

# import datetime
# Ctime=datetime
# print(Ctime.datetime(...))

  ########## |||||||||||| ########### *********** ############ &&&&&&&&&&& #########
  ########## |||||||||||| ########### *********** ############ &&&&&&&&&&& #########

########## Q.1##########
 ## Write a program to create class based method to find the factorial of any  number.
# class Calculate:
#     def Factorial(n):
#         fact = 1
#         for i in range(n,0,-1):
#             fact = fact*i
#         print(fact)
# obj=Calculate
# n=int(input("Enter the number :"))
# obj.Factorial(n)


  ############ Q.2 ############
  ##Write a Python program to create a person class. Include attributes like name, country and date of birth.
  ##  Implement a method to determine the person's age.

# from datetime import datetime
# class Person:
#     def __init__(self, name , country , dob):
#          self.name=name
#          self.country=country
#          self.dob=dob
#     def birth(self):
#          current=datetime.now().year
#          age=current-self.dob
#          print("Age :",age)
# obj=Person("dharmendra","IND",2004)
# obj.birth()

      ######## Q.3 ##########
     ## Write a program to create class using static variable for swapping of two 
     ## numbers. 
# class Swaping:
#     a=10
#     b=20
#     @staticmethod
#     def change():
#         Swaping.a,Swaping.b = Swaping.b,Swaping.a
#         print(Swaping.a,Swaping.b)
# obj=Swaping
# obj.change()

 ####### Q.4 ##########
# #Write a Python program to create a class representing a Circle. Include 
##         methods to calculate its area and perimeter.

# class Circle:
#       def area(r):
#           Arofc=3.14*r*r
#           print(Arofc)
#       def perimeter(r):
#           Pm=2*3.14*r
#           print(Pm) 

# C = Circle
# r=int(input("Enter the radius of circle :"))
# C.area(r)
# C.perimeter(r)
      
 ####### Q.5 ##########
##Write a Python program to create a calculator class. Include methods 
# for basic arithmetic operations.

# class Calculator:
#     def add(*n):
#         sum=0
#         for i in n:
#             sum=sum+i
#         print("The Addition is :",sum)
#     def sub(a,b):
#         subt=a-b        
#         print("The subtraction is :",subt)
#     def multi(*n):
#         val=1
#         for i in n:
#             val=val*i
#         print("The multiplication is :",sum)
#     def divide(x,y):
#         res = x/y
#         print("The division is :",res)
# obj = Calculator
# obj.add(2,3,4,5,7) 
# obj.sub(10,7)
# obj.multi(2,4,3)
# obj.divide(7,3)

 ##### Q.6 #######
    ## Create a static method in a class to check if a number is prime 
# class Prime:
#     @staticmethod
#     def newmethod(n):
#         i=1
#         count=0
#         while(i<=n):
#             if(n%i==0):
#                 count+=1
#             i+=1
#         if(count==2):
#            print("It is prime number")
#         else:
#            print("not")
# n=int(input("Enter the number :"))
# Prime.newmethod(n)

 ####### Q.7 #########
## Write a program to create class using static method to check the given string is palindrome or not?
# class Pallindrome:
#       @staticmethod
#       def Check(str):
#           if(str==str[::-1]):
#              print("String is pallimndrome")
#           else :
#              print("not")
# s=input("Enter the string :")
# Pallindrome.Check(s)


  #### Q.8 #####
##  Write a program to count the object.

# class Counter:
#    count=0
#    def __init__(self):
#       Counter.count+=1
# obj1=Counter()
# obj2=Counter()
# obj3=Counter()
# obj4=Counter()
# print(Counter.count)

###### Q.9 ######
#  Write a program to create class  using instance variables to calculate  the power. 
# class Calculate:
#     def __init__(self,number,power):
#         self.n=number
#         self.p=power
#     def power(self):
#         p=self.n**self.p
#         print(self.p," power of ",self.n," is :",p)
# n=int(input("Enter the number :"))
# p=int(input("Enter the power for calculate: "))
# obj=Calculate(n,p)
# obj.power()

####### Q.10 ###########
##Write a program to create instances based  method on the diameter provided and do the calculations. 
# class Circle:
#     def __init__(self, diameter):
#         self.diameter = diameter
#         self.radius = diameter/2
#     @classmethod
#     def diameter(cls, diameter):
#         return cls(diameter)
#     def circumference(self):
#         return 2*3.14*self.radius
#     def area(self):
#         return 3.14*(self.radius ** 2)
# d=int(input("Enter the diameter: "))
# C = Circle.diameter(d)
# print(f"Diameter: {C.diameter}")
# print(f"Radius: {C.radius}")
# print(f"Circumference: {C.circumference()}")
# print(f"Area: {C.area()}")

