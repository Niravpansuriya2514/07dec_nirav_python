list1=["python","c","c++","php","java","android","flutter"]
list2=[]
# list1.pop(0)
# list1.pop(3)
# list1.pop(3)
# print(list1)

del list1[0],list1[3],list1[3]

print(list1)

for i in list1:
    if i not in (0,4,5):
        list2.append(i)
print(list2)