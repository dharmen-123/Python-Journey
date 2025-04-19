    ########## SCOPE OF VARIABLES ###

# x=10
# print(id(x))
# if x:
#     x=20
#     print(x)
#     print(id(x))
# print(x)

       #########################

# x=10
# print(id(x))
# def display():
#     x=20
#     print(x)
#     print(id(x))
# display()
# print(x)


x=10
def display():
    global y
    y=20
    print(y)

display()
print(x)
print(y)