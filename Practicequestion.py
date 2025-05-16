 #####                 #     *
 #####                 #    * *
 #####                 #   * * *
 #####                 #  * * * *
 #####                 # * * * * *

# n=int(input("Enter the number :"))
# i=1
# while(i<=n):
#     print(" "*(n-i)+" *"*i)
#     i=i+1  


               ######################################
  #####           #######       *
  #####           #######     * * *
  #####           #######   * * * * *

# n=int(input("Enter the number :"))
# i=1
# while(i<=(2*n)):
#      print(" "*(2*n-i)+" *"*i)  
#      i=i+2


######################################### 

# s="i Am dharmendra Chilhate"
# print(s.capitalize())
# print(s.count('a'))
# print(s.lower())
# print(s.upper())
# print(s.title())
# print(s.isalnum())
# print(s.replace('i','My'))

          ########################################

# s=input("Enter the String : ").lower()  
# vowel="aeiou"
# v=0
# c=0
# for i in s:
#     if i in vowel:
#         v+=1
#     else:
#        i.isalpha()
#        c+=1
# print(f"Vowel is {v} and Consonants is {c}")


   ############## COUNT THE DIGIT SMALL CAPITAL LETTER #############

# val=input("Enter the string : ")
# capital=0
# small=0
# num=0
# for i in val:
#     if i.isdigit():
#         num+=1
#     elif i.islower():
#         small+=1
#     else:
#         capital+=1
# print(capital , small , num)

# s1="python"
# s2="thyonp"
# c1=0
# c2=0
# for i in s1:
#     if i in s2:
#         c1+=1 
#         c1-=1 
# print(c1)


# input_number  = 5
# for i in range(input_number):
#     print(" " * (input_number - i) + "*" * (2*i + 1))

  ############### SPY NUMBER ##################

# n=int(input("Enter the number :"))
# x=n
# sum=0
# mul=1
# while(n>0 and x>0):
#       s=n%10
#       sum=sum+s
#       mul=mul*s
#       n=n//10
# if(mul==sum):
#    print("It is SPY number")
# else:
#    print("Not Spy number")
   
   ################## PETERSON NUMBER #########################

# n=int(input("Enter the number :"))
# pnum=n
# sum=0
# while(n>0):
#       last=n%10
#       n=n//10
#       fact=1
#       for i in range(1,last+1):
#           fact*=i
#       sum+=fact
# if(pnum==sum):
#    print("It is peterson number")
# else:
#    print("Not")   

# #         #######  * * * * * * * * *
# #         #######    * * * * * * *
# #         #######      * * * * *
# #         #######        * * *
# #         #######          *

# n=int(input("Enter the number :"))
# i=1
# while(i<=(2*n-1)):
#      print(" "*i+" *"*((2*n)-i))
#      i=i+2

  ############# SUNNY NUMBER ############

# n=(int(input("Enter the number for check sunny number :")))
# a=n
# sun=0
# sum=0
# count=0
# sum2=0
# while(n>0):
#     n=n//10
#     count+=1
# while(a>0):
#    y=a%10
#    sum=sum+y**count
#    sun+=y
#    a=a//10
# while(sum>0):
#    b=sum%10
#    sum2+=b
#    sum=sum//10
# if(sum2==sun):
#    print("sunny number")
# else:
#    print("not")



# from functools import reduce
# l=[1,2,8,4,8,5]
# def Max(x,y):
#    if(x>y):
#      return x
#    else :
#      return y
# x = reduce(Max, l)
# print(x)

# import datetime
# Ctime=datetime
# print(Ctime.datetime(...))

 ########## Q, ##########
# class Calculate:
#     def Factorial(n):
#         fact = 1
#         for i in range(n,0,-1):
#             fact = fact*i
#         print(fact)
# obj=Calculate
# obj.Factorial(5)



 ######## Q, ################
 
