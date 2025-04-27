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

n=int(input("Enter the number :"))
i=0
while(i<n):
    print(" "*((2*n)-(i+1))+"*"*(i+1))
    i=i+1