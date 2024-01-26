n=int(input("how many enter eliment in your tuple: "))
list=[]

for i in range(n):
    x=int(input("enter your number eliment : "))
    list.append(x)

tuple1=tuple(list)
print(tuple1)