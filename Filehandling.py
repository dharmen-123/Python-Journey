  ############### FILE HANDLING ############
    ## store data permanently ##
    ### Operations 
    #   open()
    #   read/write()
    #   close()

#in w mode cursor position is start from zero
# x mode create new file
# cursor position in x mode is zero
f=open('n4.py', 'w')
print("File created")
print(f.name)
print(f.mode)
print(f.readable)
print(f.writable)
print(f.closed)
f.close
print(f.closed)

