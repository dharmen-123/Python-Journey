# Collection of elements(pair of key value)
# represented in {}with comma seperated 
# key must be unique 
# Value may be same 
# indexing and slicing are not support 
# mutable in nature 

d = {'name':"Dhamrmedra",'branch':"AIML",'roll':"12345"}
# print(d)
# print(d['roll'])

####### FUNCTION IN DICTIONARY ###############

#len()
#max()
# min() 
# type()
# id()

# print(max(d))
# print(min(d))
# print(type(d))
# print(id(d))
# print(len(d))

x=d.copy()
d.clear()
# print(d)
# print(x)
# print(d.fromkeys())
l=['name','age','quali']
dic = dict.fromkeys(l)
# print(dic)

st = "dharmendra"
s1=set(st)
# print(s1)
d1=dict.fromkeys(st,'python')
# print(d1)

print(x.items())
print(x.keys())
print(x.values())