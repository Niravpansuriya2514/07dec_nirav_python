n=int(input("how many enter eliment iin your list: "))
list1=[]

for i in range(n):
    x=input("enter your eliment : ")
    list1.append(x)
tuple1=tuple(list1)

len1=len(tuple1)
print("your tuple length is : ",len1)