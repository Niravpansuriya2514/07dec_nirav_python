for i in range(1,16):
    for j in range(1,16):
        if (i==3 and j==8)or(i==2 and(j==7 or j==9))or(i==1 and
            ((j>3 and j<7)or(j>9 and j<13)))or(i==2 and 
            (j==3 or j==13))or(i==3 and (j==2 or j==14))or(i==4 and
            (j==2 or j==14))or(i==5 and (j==3 or j==13))or(i==6 and
            (j==4 or j==12))or(i==7 and (j==5 or j==11))or(i==8 and 
            (j==6 or j==10))or(i==9 and(j==7 or j==9))or(i==10 and(j==8)):
           print(end="*")
        else:
            print(end=" ")
    print("\n",end="")
    
