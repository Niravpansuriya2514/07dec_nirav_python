n=int(input("how many enter eliment in your list: "))
list=[]

for i in range(n):
    a=int(input(f"enter integer eliment in your list {(i+1)}: "))
    list.append(a)
print(list)

list.sort()
print("your list smallest eliment is : ",list[0])
print("your list largest eliment is : ",list[-1])

sum=0
for i in list:
    sum+=i
print("sum of all eliment in list is: ",sum)

