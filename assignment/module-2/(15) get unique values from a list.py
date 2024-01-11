list=[]
set1=set()
n=int(input("how many eliment enter in your list: "))

for i in range(n):
    x=input("enter eliment in your list: ")
    list.append(x)
print(list)

for j in list:
    set1.add(j)


list1=[]
for k in set1:
    list1.append(k)
print("your unique list is: ")
print(list1)





