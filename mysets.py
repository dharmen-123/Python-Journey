  ############## SETS ###################

# Colection fo unique Elements
# represented in {} with comma sepreated 
# Unordered collection
# indexing and slicing are not supported
# Muttable in nature  

  ### function #####
#len()
#max()
# min()
# type()
# sum()
# id()

st1={'dharmendra','AIML','Btech',29827,9.5}
s={10,20,30,40,10,20}
# print(st1)
# print(len(st1))
# print(type(st1))
# print(max(st1))
# print(id(st1))
# print(sum(s))
# st1.add(10)
st2=st1.copy()
# print(st2)
st1.clear()
# st2.update(2,3,4,)
# st2.update('Python')
# print(st2)

# l1=[1,2,3]
# l2=[10,2,30]
# st2.update(l1,l2)
# print(st2)
st2.remove('Btech')
# print(st2)
# print(st2.pop())
print(st2)
