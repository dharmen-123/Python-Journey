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

# print(x.items())
# print(x.keys())
# print(x.values())

# print(x.popitem())
# print(x)

# print(x.pop('branch'))
# print(x)

x.setdefault('age',20)
# print(x)
x.setdefault('name','Dharmendra')
# print(x)
x1={'a':'A','b':'B'}
x.update(x1)
# print(x)
# x.update('name'['course','btech'])
# print(x)

x['age']=21

# print(x['name'])

x['c']='C'
# print(x)
