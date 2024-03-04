a=open("demo.txt","w")
list1=[]
n=int(input("how many enter eliment in list: "))
for i in range(n):
    x=input("enter your eliment: ")
    list1.append(x)

a.write(f"{list1}")