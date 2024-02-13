def perfectnomber():
    a=int(input("enter your number: "))
    temp=0
    for i in range(1,a):
        if (a%i==0):
            temp=temp+i
    if temp==a:
       print("perfect")
    else:
        print("not perfect")
perfectnomber()