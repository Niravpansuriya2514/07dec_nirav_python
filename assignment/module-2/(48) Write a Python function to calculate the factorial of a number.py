

def factorialno():
    a=int(input("enter your number: "))
    fact=0
    
    if a>=0:
        for i in range(a):
         fact+=a*a-1
        print(fact)
    else:
       print("invalid input")
    
factorialno()