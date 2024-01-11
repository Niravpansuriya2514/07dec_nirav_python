n=6
for i in range(1,n):
    for j in range(1,n):
        if (i==1 and (j==1)) or (j==2 and (i==2)) or (j==4 and (i==2)) or (j==3 and (i==3)) or (j==2 and (i==4)) or (j==4 and (i==4)) or (j==5 and (i==5))or (j==1 and i==5)or (i==1 and j==5):
           print("* ",end="")
        else:
           print("  ",end="")  
    print("\n")

for k in range(1,n):
    for l in range(1,n):
        if (k==1 and (l==1 or l==5)) or (k==2 and (l==2 or l==4)) or (k==3 and l==3) or (k==4 and (l==2 or l==4)) or (k==5 and (l==1 or l==5)):
            print("+ ",end="")
        else:
            print("  ",end="")
    print("\n")

for m in range(1,n):
    for n in range(1,n+1):
        if (n==1 and (m==1 or m==5))or (n==2 and (m==2 or m==4)) or (n==3 and m==3) or (n==4 and ((m==2) or (m==4))) or (n==5 and (m==1 or m==5)):
            print("# ",end="")
        else:
            print("  ",end="")
    print("\n")

a=""
for o in range(1,n):
    for p in range(1,n):
        if (o==1 or o==5) and (p==1 or p==5) or (o==2 or o==4) and (p==2 or p==4) or (o==3 and p==3):
            a=a+"@ "
        else:
            a=a+"  "
    a=a+"\n"
print(a)

for q in range(1,n):
    for r in range(1,n):
        if (q==1 or q==5) and (r>4 or r<2) or (q==r) or (r==2 and q==4) or (r==4 and  q==2):
            print("$ ",end="")
        else:
            print("  ",end="")
    print("\n")