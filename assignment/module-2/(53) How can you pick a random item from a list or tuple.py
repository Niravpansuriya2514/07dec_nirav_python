
# index using pick in random item in list or tuple
list1=[]
tuple=()

n=int(input("how many enter item in list or tuple: "))
 
for i in range(n):
    x=input("enter your eliment: ")
    list1.append(x)

print("your list is")
print(list1)
print("select random item in list using index")

a=int(input("enter your list index number: "))
print(list1[a])
