
########## Q.1##########
 ## Write a program to create class based method to find the factorial of any  number.
class Calculate:
    def Factorial(n):
        fact = 1
        for i in range(n,0,-1):
            fact = fact*i
        print(fact)
obj=Calculate
n=int(input("Enter the number :"))
obj.Factorial(n)


  ############ Q.2 ############
  ##Write a Python program to create a person class. Include attributes like name, country and date of birth.
  ##  Implement a method to determine the person's age.

from datetime import datetime
class Person:
    def __init__(self, name , country , dob):
         self.name=name
         self.country=country
         self.dob=dob
    def birth(self):
         current=datetime.now().year
         age=current-self.dob
         print("Age :",age)
obj=Person("dharmendra","IND",2004)
obj.birth()

      ######## Q.3 ##########
     ## Write a program to create class using static variable for swapping of two numbers. 

class Swaping:
    a=10
    b=20
    @staticmethod
    def change():
        Swaping.a,Swaping.b = Swaping.b,Swaping.a
        print(Swaping.a,Swaping.b)
obj=Swaping
obj.change()

 ####### Q.4 ##########
# #Write a Python program to create a class representing a Circle. Include 
##         methods to calculate its area and perimeter.

class Circle:
      def area(r):
          Arofc=3.14*r*r
          print(Arofc)
      def perimeter(r):
          Pm=2*3.14*r
          print(Pm) 

C = Circle
r=int(input("Enter the radius of circle :"))
C.area(r)
C.perimeter(r)
      
 ####### Q.5 ##########
##Write a Python program to create a calculator class. Include methods 
# for basic arithmetic operations.

class Calculator:
    def add(*n):
        sum=0
        for i in n:
            sum=sum+i
        print("The Addition is :",sum)
    def sub(a,b):
        subt=a-b        
        print("The subtraction is :",subt)
    def multi(*n):
        val=1
        for i in n:
            val=val*i
        print("The multiplication is :",sum)
    def divide(x,y):
        res = x/y
        print("The division is :",res)
obj = Calculator
obj.add(2,3,4,5,7) 
obj.sub(10,7)
obj.multi(2,4,3)
obj.divide(7,3)

 ##### Q.6 #######
    ## Create a static method in a class to check if a number is prime 
class Prime:
    @staticmethod
    def newmethod(n):
        i=1
        count=0
        while(i<=n):
            if(n%i==0):
                count+=1
            i+=1
        if(count==2):
           print("It is prime number")
        else:
           print("not")
n=int(input("Enter the number :"))
Prime.newmethod(n)

 ####### Q.7 #########
## Write a program to create class using static method to check the given string is palindrome or not?
class Pallindrome:
      @staticmethod
      def Check(str):
          if(str==str[::-1]):
             print("String is pallimndrome")
          else :
             print("not")
s=input("Enter the string :")
Pallindrome.Check(s)


  #### Q.8 #####
##  Write a program to count the object.

class Counter:
   count=0
   def __init__(self):
      Counter.count+=1
obj1=Counter()
obj2=Counter()
obj3=Counter()
obj4=Counter()
print(Counter.count)

###### Q.9 ######
#  Write a program to create class  using instance variables to calculate  the power. 
class Calculate:
    def __init__(self,number,power):
        self.n=number
        self.p=power
    def power(self):
        p=self.n**self.p
        print(self.p," power of ",self.n," is :",p)
n=int(input("Enter the number :"))
p=int(input("Enter the power for calculate: "))
obj=Calculate(n,p)
obj.power()

####### Q.10 ###########
##Write a program to create instances based  method on the diameter provided and do the calculations. 
class Circle:
    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter/2
    @classmethod
    def diameter(cls, diameter):
        return cls(diameter)
    def circumference(self):
        return 2*3.14*self.radius
    def area(self):
        return 3.14*(self.radius ** 2)
d=int(input("Enter the diameter: "))
C = Circle.diameter(d)
print(f"Diameter: {C.diameter}")
print(f"Radius: {C.radius}")
print(f"Circumference: {C.circumference()}")
print(f"Area: {C.area()}")
