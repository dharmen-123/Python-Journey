 ######### decorator is used to modify and change the behaviour of other function without changing its code

# def decorator(fun): 

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
def Outerfun(n):
    def innerfun(x,y):
        x=x*2
        y=y+10
        n(x,y)
    return innerfun
@Outerfun
def Mainfun(p,q):
    print(p+q)
a=int(input("Enter the number :"))
b=int(input("Enter the number :"))
Mainfun(a,b)