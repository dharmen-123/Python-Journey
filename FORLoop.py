# n=int(input("Enter the number"))
# for i in range(2,n+1,2):
#     print(i)

   ########### EVEN number number ###########

# n=int(input("Enter the number"))
# for i in range(1,n+1):
#     print(2*i)

   ########### ODD number ###########
# n=int(input("Enter the number"))
# for i in range(1,n+1):
#     print(2*i-1)

# num=int(input("Enter the number : "))
# i=1
# while (i<=num):
#   if i<num:
#     print(2*i,end=',')
#   else :
#     print(2*i)  
#   i=i+1

########################################
  ########### Q.1 ##########
# num=int(input("Enter the number : "))
# for x in range(1,num+1):
#    print(x*2)

 ########## Q.2 ############

########### HCF of given number #######
# x=int(input("Enter the number :")) 
# y=int(input("Enter the number :")) 
# mv=min(x,y)
# for i in range(1,mv):
#     if(x%i==0 and y%i==0):
#         hcf=i
# print(hcf)

 ######### Print N natural number #####
# n=int(input("Enter the number :"))
# for i in range(1,n+1):
#     print(i,end=" ")

   ########## Sum of N natural number  ###########

# n=int(input("Enter the number :"))
# sum=0
# for i in range(1,n+1):
#    sum=sum+i
# print(sum)

 
n=int(input("Enter the number :"))
for i in range(1,n+1):
   if i<n:
      print(2*i,end=',')
   else :
      print(2*i)  
   i=i+1
