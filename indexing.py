# indexing is use for accesssing the elements of ordered collection 
lst=[228,33.33,'A',"dharmendra"]
tpl=(98,'D',"dharmendra",9.87)

# print(lst.index(228))
# print(tpl[2])
# print(lst[2])

       #######SLICING IN PYTHON#######

# syntax  collection[start point: stop point : (step/direction/jump)]


# RULES of SLICING
# 1 checkout step direction (if it is not  given that means by default 1)
# 2 checkout start and stop direction
# 3 if both direction are same i.e we get same output but if direction are opposite i.e we always get empty output

# s="Dharmendra"
# print(len(s))
# print(s[0:11])
# print(s[::-1])
# print(s[1:11:3])

s1 = 'thinktank'
# print(s1[5:5])

s2 = 'follow'
# print(s2[3:8])

s3 = 'medium'
# print(s3[-4:4])

s4 = 'pythonista'
# print(s4[6:2:-1])

s5 = 'program'
# print(s5[1:6:2])

s6 = 'coder'
# print(s6[::0])

s7 = 'doubled'       #Sclicing in slice
# print(s7[1:6][1:3])   

s8 = 'question'
# print(s8[-1::-2])

s9 = 'subscribe'
# print(s9[-3:-6:2])

s10 = 'completed'
# print(s10[2:5:3])

lst1=[2929,"hello",28.93,'A',29,39.2]
# print(lst1[1::])

lst2= [(1, 'apple'), (2, 'banana'), (3, 'cherry'), (4, 'date')]
# print(lst2[2::2])

# print(lst2[-1::-1])
# print(lst2[:-1:])

#IN SLICING MINIMUM ONE COLON: IS REQUIRE
st="I LOVE PYTHON"
st1 =st.lower()
# print(st1[::-1][::2][1:7][::-1])    
st2="i am dharmendra chilhate"
print(st2.title())
print(st2.capitalize())
print(st2.upper())
print(st2.swapcase())