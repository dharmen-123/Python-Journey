  ############### FILE HANDLING ############
    ## store data permanently ##
    ### Operations 
    #   open()
    #   read/write()
    #   close()
 ### THERE are Two mode in file handing ####
   # # x mode and w mode , read mode , append mode 
#in w mode cursor position is start from zero
# x mode create new file
# cursor position in x mode is zero

            # x                        w

# f= open('n4.py', 'w')
# print("File created")
# print(f.name)
# print(f.mode)
# print(f.readable)
# print(f.writable)
# print(f.closed)
# f.close
# print(f.closed)

# f=open("n4.py",'r')
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close
# print(f.closed)

### IN append mode the cursor position is at the last

f=open("x1.py",'a')
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.closed)
f.close
print(f.closed)