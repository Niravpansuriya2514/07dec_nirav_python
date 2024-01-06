list1=[]
list2=[]

n=int(input("how many enter eliment in your list: "))
for i in range(n):
    a=input(f"enter your eliment in list1 {i+1}: ")
    list1.append(a)

for i in range(n):
    b=input(f"enter your eliment in list2 {i+1}: ")
    list2.append(b)

print("your list1")
print(list1)
print("your list2")
print(list2)

list1.sort()
list2.sort()
print("compare your list")

if list1==list2:
    print("list1 and list2 are equel")
else:
    print("list1 and list2 are not equel")
