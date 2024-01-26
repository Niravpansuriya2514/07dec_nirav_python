            #    LIST                               TUPLE

# list is changeable                | tuple in unchangeable
# Lists have many built-in methods	| Tuple does not have many built-in methods

# create a list and change a value
list=[] 
n1=int(input("how many eliment enter in your list: "))

for i in range(n1):
    x=input(f"enter your eliment {i+1} : ")
    list.append(x)
print("your list is: ")
print(list)

list[2]='android'
print(list)

# create tuple too not change value to reason tuple have not changleable mathod

list2=[]
n2=int(input("how many enter eliment in your tuple: "))

for j in range(n2):
    y=input("enter your eliment: ")
    list2.append(y)
# list convert in to tuple
print(tuple(list2))
