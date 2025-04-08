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
# n=int(input("Enter the number"))
# i=1
# mul=1
# while(i<=n):
#     mul=mul*i
#     if i<n:
#         print(i,end='*')
#     else:
#         print(i,end='= ')
#     i=i+1
# print(mul)

   ###### Factorial #########
# n=int(input("Enter the number : "))
# i=1
# fact=1
# while(i<=n):
#     fact=fact*i
#     i=i+1
# print('Factorial of {} is {} '.format(n,fact))


# n=int(input("Enter The number"))
# i=1
# while(i<=n):

#     if i%2==0:
#         print(i,end=',')
#     else:
#         print

  ######### Pallindrome Number ########
# n=int(input("Enter the number :"))
# x=n
# rev=0
# while n>0:
#     last=n%10
#     rev=rev*10+last
#     n=n//10
# if x==rev:
#     print("Given number is pallindrome")
# else:
#     print("not ")

             ############## 2nd Way to find pallindrome #########

# n=input("Enter the Number : ")
# if n==n[::-1]:
#   print(f"The given number {n} is Pallindrom")
# else:
#   print("Given number is not a pallindorme")

    ##################   TASK QUESTIONS   ###################
    ##################   TASK QUESTIONS   ###################

                     ######### Print the n Even Number #############

# num=int(input("Enter the number : "))
# i=1
# while (i<=num):
#   if i<num:
#     print(2*i,end=',')
#   else :
#     print(2*i)  
#   i=i+1

                     ########### Print Sum of N Even Number #########

# num=int(input("Enter the number : "))
# i=1
# sum=0
# while (i<=num):
#     sum=sum+(2*i) 
#     if i<num:
#       print(2*i,end=' + ')
#     else :
#       print(2*i,end=" = ")  
#     i=i+1
# print(sum)

     ######### Print the even number from 1 to n ##############

# n=int(input("Enter the Number : "))
# i=1
# while(i<=n):
#     if i<n:
#         if i%2==0:
#           print(i,end=",")
#     else:
#       print(i)
#     i=i+1 

     ######### Print the SUM of even number from 1 to n ##############
     
# n=int(input("Enter the Number : "))
# i=1
# sum=0
# while(i<=n):
#     sum=sum+i
#     if i<n:
#         if i%2==0:
#           print(i,end=" + ")
#     else:
#       print(i,end=" = ")
#     i=i+1  
# print(sum)

       #||||||||||||||||||||||||| ODD NUMBER QUESTION ||||||||||||||||||||||||||||||#

                          ######### Print the n Odd Number #############

# num=int(input("Enter the number : "))
# i=1
# while (i<=num):
#   if i<num:
#     print((2*i)-1,end=',')
#   else :
#     print((2*i)-1,end=" ")  
#   i=i+1

                     ########### Print Sum of N Odd Number #########

# num=int(input("Enter the number : "))
# i=1
# sum=0
# while (i<=num):
#     sum=sum+((2*i)-1) 
#     if i<num:
#       print((2*i)-1,end=' + ')
#     else :
#       print((2*i)-1,end=" = ")  
#     i=i+1
# print(sum)

     ######### Print the Odd number from 1 to n ##############

# n=int(input("Enter the Number : "))
# i=1
# while(i<=n):
#     if i<n:
#         if i%2==0:
#           print(i-1,end=",")
#     else:
#       print(i-1,end=" ")
#     i=i+1  

     ######### Print the SUM of Odd number from 1 to n ##############
     
# n=int(input("Enter the Number : "))
# i=1
# sum=0
# while(i<=n):
#     if i<n:
#         if i%2==0:
#           print(i-1,end=" + ")
#         else:
#           sum=sum+i
#     else:
#       print(i-1,end=" = ")
#     i=i+1  
# print(sum)
  
    ######## Count number of digit in given number ############
# n=int(input("Enter the number :"))
# count=0
# while(n>0):
#      n=n//10
#      count+=1
# print(count)
# n=input("Enter num: ")
# print(len(n))

      ########### Armstrong Number ###########
# n=int(input("Enter the number :"))
# x=n
# m=x
# count=0
# sum=0
# while(n>0):
#      n=n//10
#      count+=1
# while(x>0):
#      y=x%10
#      sum=sum+y**count
#      x=x//10
# print(sum)
# if(m==sum):
#      print('Given number {} is armstrong'.format(m))
# else :
#      print("not armsttrong")


str=input("Enter string : ")
l=0
r=len(str)-1
while(l<r):
     if(str[l]==str[r]):
          l+=1
          r-=1
     else:
          print("not")
if(l==r):
     print("Given String is Pallindrome")
else:
     print("Not Pallindrome")


