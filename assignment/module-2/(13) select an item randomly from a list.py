list=[]
n=int(input("how many eliment enter in your list: "))

for i in range(n):
    x=input("enter you eliment: ")
    list.append(x)
print(list)
a=int(input("enter the randomly number of eliment: "))

print("your eliment is: ",end="")
print(list[a-1])
