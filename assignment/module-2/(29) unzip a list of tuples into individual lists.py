list1=[('java','python'),('android','flutter'),('c','c++')]
print("your list before unzip a list of tuple")
print(list1)
list2=[]

for i in list1:
    len1=len(i)
    for j in range(len1):
        list2.append(i[j])

print("your list after unzip a list of tuple")
print(list2)
