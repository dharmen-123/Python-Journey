


cart={}
cart['userid']=1
cart['items']=[]
cart['quantity']=[]
cart['items'].append(2)
cart['quantity'].append(3)
print(cart)
cart['items'].append(6)
cart['items'].append(3)
cart['quantity'].append(1)
cart['quantity'].append(2)
print(cart)
item_index=cart['items'].index(6)
print(item_index)
item_qua=cart['quantity'][item_index]
print(item_qua)
