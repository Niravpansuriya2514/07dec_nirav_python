def common():
    n=int(input("how many enter eliment in your list: "))
    list1=[]
    list2=[]
    print("\tLIST-1")
    for i in range(n):
        x=input(f"enter your eliment {(i+1)}: ")
        list1.append(x)

    print("-------------------------------------")

    print("\tLIST-2")
    for i in range(n):
        x=input(f"enter yourc eliment {(i+1)}: ")
        list2.append(x)


    for i in list1:
        if i in list2:
            print("true..")
            break

            
common()