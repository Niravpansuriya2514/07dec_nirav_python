a=4
b=5
for i in range(b,1,-1):

    for k in range(0,b):    
        print(" ",end="")
    # a-=1  
        
        for j in range(k+1):
           print("* ",end="")
        print("\n")

n=5
k=4
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("* ",end="")
    print("\n")
