def unique():
    list=[]
    set1=set()
    uniquelist=[]
    n=int(input("how many eliment enter in your list: "))

    for i in range(n):
        x=input(f"enter your elimentc {i+1}: ")
        list.append(x)

    print("your list is:")
    print(list)

    for i in list:
        set1.add(i)
    
    for i in set1:
        uniquelist.append(i)

    print("your unique list is:")
    print(uniquelist)

unique()