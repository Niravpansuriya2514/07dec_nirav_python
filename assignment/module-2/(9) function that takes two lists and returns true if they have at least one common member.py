def fun():
    list1=[]
    list2=[]
    newlist=[]
    set1=set()
    n=int(input("how many eliment enter in your list: "))

    for i in range(n):
        a=input(f"enter your eliment in first list {i+1}: ")
        list1.append(a)
        
    for i in range(n):
        b=input(f"enter your eliment in second list {i+1}: ")
        list2.append(b)

    print("your first list is:")
    print(list1)
    print("\nyour second liist is:")
    print(list2)

    newlist=list1+list2
    for i in newlist:
        set1.add(i)
    
    if len(newlist)!=len(set1):
        print("true")

    

fun()

    


                



