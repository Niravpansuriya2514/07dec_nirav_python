
# create a list
n=int(input("how many enter eliment iin your list: "))
list1=[]

for i in range(n):
    x=input("enter your eliment : ")
    list1.append(x)

# convert a list to tuple

tuple1=tuple(list1)
print(tuple1)