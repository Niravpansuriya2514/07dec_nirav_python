a=int(input("enter your number: "))
def divisor():
    sum=0

    for i in range(1,a):
       if a % i==0:
           sum+=i
    print("divisor is: ",sum)
          
divisor()
