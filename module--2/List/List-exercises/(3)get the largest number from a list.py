list1=['python','java','c++','android','c']
print(list1)
a=0
b=""
for i in list1:
    if len(i)>a:
        a=len(i)
        b=i
print(a,b)

list2=[23,45,56,36,87,46,7,87,46,645]
print(list2)

list2.sort()
print(list2)
print(list2[-1])

for i in list2:
    if i>a:
        a=i
print(a)