#  Function is use for code reusability 
 ###### SYNTAX of funtion #########
# def Function_name (parameter):  #function initialize
#     |
#     |funnction_body           #function declaration
#     |
#     |return Value 

# Function_name(argument) #function calling


# def Add(x,y):
#     print(x+y)
# print(Add(10,5))
# Add(5,8)

# def Add(x,y):
#     return(x+y)
# print(Add(10,5))
# Add(5,8)

# def Add(x,y):
#     print(x+y)
# z=Add(10,5)
# print(z)
# print("Hello")
# print(z)

        #### Print Evene Number using function #####

# def Even(n):
#     for i in range(1,n+1):
#         if(i%2==0):
#             print(i)
# n=int(input("Enter the number :"))
# Even(n)

       ########## Leap year questions ###########

# def Leapyear(n):
#       if((n%4==0 or n%400==0) and n%100!=0):
#           # if(n%100!=0):
#           print("It is leap year")
#       else:
#           print("not")
      
# n=int(input("Enter the year :"))
# Leapyear(n)

  ####### Relation B/T Parameters & Arguments

# positional Arguments
# Keyword Arguments
# Default Arguments
# positional length / variables length argument
# Keyword length /Keyword variables length argument

########## Positional Arguments #######
# def Add(x,y):
#     print(x,y)
#     return x+y
# a=int(input("Enter the number :"))
# b=int(input("Enter the number :"))
# z=Add(a,b)
# print(z)

  ######## Key word arguments #####
  
# def Add(x,y):
#     print(x,y)
#     return x+y
# a=int(input("Enter the number :"))
# b=int(input("Enter the number :"))
# z=Add(x=a,y=b)
# print(z)

 ######## Default Arguments #########

# def Add(x=0,y=0):
#     return x+y
# a=int(input("Enter the number :"))
# b=int(input("Enter the number :"))
# z=Add()
# print(z)

  ######### Variable length Arguments ######
# def add(*n):
#   print(n)
#   print(type(n))

# add()
# add(10)

  ####### Assign multiple values in arguments ######
# def add(*n):
#     sum=0
#     for i in n:
#         for j in i:
#             sum=sum+j
#     return sum
# n=eval(input("Enter all values"))
# z=add(n)
# print(z) 