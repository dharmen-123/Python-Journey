### Generator create a collection in form of generator object
## It holds a collection of elements
# It used yeild instead of return keyword

### Syntax of Generator ##

# def funcname(paramenter):

#     yeild ----
# x=funcname(argument)
# print(next(x))


# def even(n):
#     for i in range(1,n+1):
#         yield 2*i
# x=int(input("Enter the number :"))
# y=even(x)
# print(y)                   # #<generator object even at 0x00000218D4782420>
# print(type(y))              # #<class 'generator'>
# # print(list(y))              # #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# # for i in y:
# #     print(i,end=" ")

# print(next(y))
# print("hello")
# print(next(y))
# print("hi")
# print(next(y))


# def table(n):
#     for i in range(1,n+1):
#         for j in range(1,11):
#              print(i*j,end=" ")
#         yield
# n=int(input("Enter :"))
# a=table(n)
# next(a)
# print("Hello")
# next(a)
# print("Hii")
# next(a)
# print("\npython ")
# next(a)

 ############### Table from 1 to n ######

def Tablenew(n):
    for i in range(2,n+1):
        yield i
x=int(input("Enter no :"))
y=Tablenew(x)
print(len(list(y)))
z=next(y)
for i in range(1,11):
    print(z*i , end=" ")