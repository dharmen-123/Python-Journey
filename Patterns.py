     ######### Square Pattern ########
               # #  *  *  *  *  * 
               # #  *  *  *  *  *
               # #  *  *  *  *  *
               # #  *  *  *  *  *
               # #  *  *  *  *  *
# n=int(input("Enter "))
# i=1
# while(i<=n):
#     print(' * '*n)
#     i=i+1

   
# n=int(input("Enter the number : "))
# for i in range(1,n+1):
#     print(' * '*n)
 
 ############ Right Angle Triangle ###########
                        # #          *
                        # #        * *
                        # #      * * *
                        # #    * * * *
                        # #  * * * * *
# n=int(input("Enter the number : "))
# i=1
# while(i<=n):
#     print('  '*(n-i)+' *'*i)
#     i=i+1 

  ########## left Angle Traingle ###########
                   # #  *
                   # #  *  *
                   # #  *  *  *
                   # #  *  *  *  *
                   # #  *  *  *  *  *  
# n=int(input("Enter the number : "))
# i=1
# while(i<=n):
#     print(' * '*i+'   '*(n-i))
#     i=i+1 

############# Perfect Triangle ############## 
                  # #     *
                  # #    * *
                  # #   * * *
                  # #  * * * *
                  # # * * * * * 
# n=int(input("Enter the number : "))
# i=1
# while(i<=n):
    # print(' '*(n-i)+' *'*i)
    # i=i+1

   ######### Temple Pattern #############
                   # #      *
                   # #     * *
                   # #    * * *
                   # #   * * * *
                   # #  * * * * *
                   # #  * * * * *
                   # #  * * * * *
                   # #  * * * * *
                   # #  * * * * *
                   # #  * * * * *   
# n=int(input("Enter the number : "))
# i=1
# while(i<=n):
#     print(' '*(n-i)+' *'*i)
#     i=i+1 
# for i in range(1,n+1):
#     print(' *'*n)

 ############# Inverted Left Angle Triangle ###########
                     # #  * * * * * 
                     # #  * * * *
                     # #  * * *
                     # #  * *
                     # #  *
# n=int(input("Enter the number "))
# i=0
# while(i<n):
#     print('* '*(n-i)+' '*i)
#     i=i+1

  ############ 2nd Way #########
# n=int(input("Enter the number "))
# i=0
# while(i<n):
#     print('* '*(n-i))
#     i=i+1

 ############### 3rd Way ############
# n=5
# i=0
# while(i<n):
#     print('*'*n)
#     n=n-1

  ############# Inverted Left Angle Triangle ###########
## **********
##  *********
##   ********
##    *******
##     ******
##      *****
##       ****
##        ***
##         **
##          *
# n=int(input("Enter the number "))
# i=0
# while(i<n):
#     print(' '*i+'*'*(n-i))
#     i=i+1 

#  * * * * * * * * * *
#   * * * * * * * * *
#    * * * * * * * *
#     * * * * * * *
#      * * * * * *
#       * * * * *
#        * * * *
#         * * *
#          * *
#           *  
# n=int(input("Enter the number "))
# i=0
# while(i<n):
#     print(' '*i+' *'*(n-i))
#     i=i+1 


n=int(input("Enter the number : "))
i=1
while(i<=n):
    print('*'*i+' '*(n-i))
    i=i+1
i=1
while(i<n):
    n=n-1
    print('*'*n)