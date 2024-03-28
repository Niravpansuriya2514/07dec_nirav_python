for i in range(1,10):
    for j in range(1,10):
        if (i==1 and j==5)or(i==2 and(j==4 or j==6))or(i==3 and(j==3 or j==7))or(i==4 and(j==2 or j==8))or(i==5):
            print(end="*")
        else:
            print(end=" ")
    print("\n",end="")