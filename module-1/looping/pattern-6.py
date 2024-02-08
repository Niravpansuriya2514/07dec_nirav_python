
n=5
k=4
for i in range(65,70):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(65,i+1):
        print(chr(j),end=" ")
    print("\n")
