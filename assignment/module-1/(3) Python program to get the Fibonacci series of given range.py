t1=0
t2=1
next=t1+t2
a=int(input("enter your number:"))
for i in range(a):
    print(next)
    t1=t2
    t2=next
    next=t1+t2