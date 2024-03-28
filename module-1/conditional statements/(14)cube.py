for i in range(1,15):
    for j in range(1,15):
        if (i==1 and j==4)or(i==2 and(j==3 or j==6))or(i==3 and(j==2 or j==8))or(i==4 and(j==1 or j==10))or(i==5 and(j==3 or j==9))or(i==6 and (j==5 or j==8))or(i==7 and(j==7))or(i==7 and 
            (j==4))or(i==8 and(j==3 or j==6))or(i==9 and(j==2 or j==8))or(i==10 and(j==1 or j==10))or(i==11 and(j==3 or j==9))or(i==12 and (j==5 or j==8))or(i==13 and(j==7)):
           print(end="* ")
        elif (j==1 and (i>4 and i<10))or(j==4 and(i>1 and i<7))or(j==7 and(i>7 and i<13))or(j==10 and(i>4 and i<10)):
            print(end="| ")
        else:
            print(end="  ")
    print("\n",end="")