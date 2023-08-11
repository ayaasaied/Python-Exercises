tuplex=(4,6,7,8,9)
print(tuplex)

#to add item
tuplex=tuplex+(9 ,)
#converting the tuple to list
listx = list(tuplex)
listx.append(30)
tuplex =tuple(listx)
print(tuplex)
