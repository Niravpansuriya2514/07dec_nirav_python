fact=1
i=1
a=int(input("enter your number : "))
      
if a<0: 
    print("sorry enter your positive")
else:
    for i in range(1,a+1):
        fact*=i
        
    print(f"factorial of {a}  is : ",fact)
