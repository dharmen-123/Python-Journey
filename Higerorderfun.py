import functools
# l=[1,2,3,4,5]
# def Squar(n):
#     return (n**2)
# x=map(Squar,l)
# print(x)
# print(tuple(x))

  ########### Multiply two collection using map function ######
# l1=[1,2,3,4,5]
# t1=(1,2,3,4,5)
# def Squr(m,n):
#     return (m*n)
# x=map(Squr,l1,t1)
# print(list(x))

 ###########################

# l=[1,2,3,4,5]
# def Even(n):
#     if(n%2==0):
#         return n

# x=filter(Even,l)
# print(tuple(x))

 ############### reduce function ##############
 
# l=[10,20,30,5,25,12,6]
# def Maxfun(x,y):
#       if(x>y):
#         return x
#       else :
#         return y
# x= functools.reduce(Maxfun , l)
# print(x)