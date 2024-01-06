list1=[]
list2=[]
set1=set()
a=int(input("how many eliment in enter your list: "))

for i in range(a):
    x=input("enter eliment in your list: ")
    list1.append(x)

print("YOUR LIST IS:")
print(list1)
print("remove a duplicate eliment in your list")


for i in list1:
    set1.add(i)

for i in set1:
    list2.append(i)
print(list2)