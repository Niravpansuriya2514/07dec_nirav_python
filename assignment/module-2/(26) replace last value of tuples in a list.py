

list1=[('c','c++','java'),('python','php','node')]
print(list1)
list2=[]

for i in list1:
    list2.append((list(i)))
print(list2)

list2[0][-1]='android'
list2[1][-1]='flutter'

list3=[]
for j in list2:
    list3.append((tuple(j)))
print(list3)


