 ######### decorator is used to modify and change the behaviour of other function without changing its code

# def decorator(fun): 
#     fun()
#     return 5
    
# def main_fun():
#     print("main function")
# x=decorator(main_fun)
# # x()
# print(x)


# def decor():
#     def inner():
#         print("hello")
#     return inner

# x=decor()
# print(x)
# x()

            ###############################

# def decor(z):
#     def inner(x,y):
#         print(x+y)
#         print(z)
#     return inner
# x=decor(10)
# p=int(input("Enter the number :"))
# q=int(input("Enter the number :"))
# x(p,q)

################################################
# def Outerfun(n):
#     def innerfun(x,y):
#         x=x*2
#         y=y+10
#         n(x,y)
#     return innerfun
# @Outerfun
# def Mainfun(p,q):
#     print(p+q)
# a=int(input("Enter the number :"))
# b=int(input("Enter the number :"))
# Mainfun(a,b)


# def outer_func(main_func):
#     def inner_func(s,t):
#         s=s*2
#         t=t+2
#         main_func(s,t)
#     return inner_func   
# @outer_func
# def main_func(p,q):
#     print(p+q)
# s=int(input("Enter any number :"))
# t=int(input("Enter any number :")) 
# main_func(s,t)

##################################
def Special(fun):
    def Inside(num):
       num=num+1
       fun(num)
    return Inside
@Special
def Main(n):
    for i in range(1,11):
        print(n,"X",i,"=",n*i)
n=int(input("Enter the number for print table :"))
Main(n)