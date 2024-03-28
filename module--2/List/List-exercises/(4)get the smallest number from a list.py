list1=['python','java','c++','android','c']
print(list1)

a=0
b=""
for i in list1:
    if len(i)<len(list1[0]):
        a=len(i)
        b=i
print(a,b)

list2=[23,45,456,6,77887,8,89,9,99,99,4334,323]
print(list2)

list2.sort()
print(list2)
print(list2[0])

c=0
for i in list2:
    if i<list2[1]:
        c=i
print(c)
