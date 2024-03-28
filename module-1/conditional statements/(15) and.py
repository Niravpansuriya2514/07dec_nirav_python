for i in range(1,15):
    for j in range(1,15):
        if (i==2 and(j==7 or j==8))or(i==3 and(j==6 or j==9))or(i==4 and
           (j==6 or j==9))or(i==5 and(j==7 or j==8))or(i==6 and
            (j==6 or j==9))or(i==7 and(j==5 or j==10 or j==14))or(i==8 and
            (j==5 or j==11 or j==13))or(i==9 and(j==5 or j==12))or(i==10 and
            (j==6 or j==11 or j==13))or(i==11 and (j==7 or j==8 or j==9 or j==14)):
            print(end="* ")
        else:
            print(end="  ")
    print("\n",end="")