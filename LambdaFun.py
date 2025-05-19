import functools
# lambda function is use for limited time
# when we have not using many time function then we use lambda function

# x=lambda p,q: (p+q)
# a=int(input("Enter the number"))
# b=int(input("Enter the number"))
# x(a,b)
# print(x(a,b)+5)
  
  ########### square of list using lambda fucntion ########
# l=[1,2,3,4,6,7,8]
# x=list(map(lambda x:x**2 , l))
# print(x) 
        
        ######## using reduce method ######

# x=list(filter(lambda x:  x%2==0 ,l))
# print(x)
             ######even number code #####
             
# print(list(filter(lambda x:  x%2==0 ,[1,2,3,4,5])))

        #######using reduce method ######
l=[1,2,3,4,6,7,8]
print(functools.reduce(lambda a,b : a if a<b else b ,l))

# a=lambda:print("hello python")
# a()