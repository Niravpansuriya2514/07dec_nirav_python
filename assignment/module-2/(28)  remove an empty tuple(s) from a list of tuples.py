list1=[('c','c++','java'),('python','android','flutter'),(),()]
print("your list before remove empty list: ")
print(list1)
list2=[]
for i in list1:
    if len(i)>0:
        list2.append(i)
print("your list after remove empty list: ")
print(list2)
      


