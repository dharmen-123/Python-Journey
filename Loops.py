  ############Q.1 Print N natural number #######
# n=int(input("Enter the number"))
# i=1
# while(i<=n):
#     if i<n:
#         print(i,end=',')
#     else:
#         print(i)
#     i=i+1
    
# s="dharmendra"
# n=4
# print(n*s,sep=" ")


   ############## Q.2  SUM of N Natural Number#########
# n=int(input("Enter the number"))
# i=1
# sum=0
# while(i<=n):
#     sum=sum+i
#     if i<n:
#         print(i,end='+')
#     else:
#         print(i,end='=')
#     i=i+1
# print(sum)

  ###### Q.3 Multiply N natural number ########
n=int(input("Enter the number"))
i=1
mul=1
while(i<=n):
    mul=mul*i
    if i<n:
        print(i,end='*')
    else:
        print(i,end='= ')
    i=i+1
print(mul)