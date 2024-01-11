mainlist=[]
sublist=[]
sublist2=[]

# INPUT LIST

n1=int(input("how many enter eliment in your list: "))

for i in range(n1):
    x=input(f"enter your eliment {i+1} : ")
    mainlist.append(x)
print("your list is:")
print(mainlist)

# INPUT SUBLIST
for a in range(5):
    n2=int(input("how many enter eliment in your sublist: "))

    if n2 <= n1: 
       for j in range(n2):
          y=input(f"enter your eliment {j+1} : ")
          sublist.append(y)
       print("your sub list:")
       print(sublist)
       len1=len(sublist)

       # check your sublist in your list

       for k in sublist:
           if k in mainlist:
              sublist2.append(k)
       len2=len(sublist2)

       print("check a your sublist in your list")
       if len1==len2:
          print("yes...")
       else:
          print("no...")
       break

    else:
       print("invalid input")
       print("Please enter the sub list element less than or equal to the first list element")









    

