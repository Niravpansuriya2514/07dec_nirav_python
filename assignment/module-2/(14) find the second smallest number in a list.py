list1=[]
n=int(input("how many eliment enter  in your list: "))

for i in range(n):
    x=input("enter your eliment in interger or string value: ")
    list1.append(x)

def interger():

    print(list1)
    list1.sort()

    print("second smallest nuber is: ",list1[2])

def string():

    list2=[]
    
    for i in list1:
        list2.append((len(i),(i)))

    list2.sort()
    print("our second smallest number is: ",list2[1][1])


print("your list is intergr type to press is -> 1")
print("your list is string type to press is -> 2")
a=int(input("enter your choice: "))

if a==1:
    interger()
elif a==2:
    string()
else:
    print("invalid input")
    
