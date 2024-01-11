for r in range(1,6):
    for c in range(1,6):
        if c==1 or c==5 or (c==2 and(r==2))or (c==3 and(r==3))or (c==4 and(r==4)):
            print("**",end="")
        else:
            print("  ",end="")
        #   if r==1 or r==5:
        #        print("*",end="")
        #   else:
        #        print(" ")
    print("\n")