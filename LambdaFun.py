
# lambda function is use for limited time
# when we have not using many time function then we use lambda function

x=lambda p,q: (p+q)
a=int(input("Enter the number"))
b=int(input("Enter the number"))
x(a,b)
print(x(a,b)+5)