  ############## SETS ###################

# Colection fo unique Elements
# represented in {} with comma sepreated 
# Unordered collection
# indexing and slicing are not supported
# Muttable in nature  

  

st1={'dharmendra','AIML','Btech',29827,9.5}
print(type(st1))
st1.add(10)
st2=st1.copy()
# print(st2)
st1.clear()
st2.remove('Btech')
# print(st2)

# print(st2.pop())
st2.update('A')
print(st2)
