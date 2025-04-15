
   #############################
# # break
# # pass 
# # continue

# break exit the loop 

w=int(input("Enter the number :")) 
x=int(input("Enter the number :")) 
y=int(input("Enter the number :")) 
z=int(input("Enter the number :")) 
h=max(w,x,y,z)
print(h)
while(True):
    if h%w==0 and h%x==0 and h%y==0 and h%z==0:
        lcm = h
        break
    h=h+1
print(f"The LCM of given number is {lcm}")