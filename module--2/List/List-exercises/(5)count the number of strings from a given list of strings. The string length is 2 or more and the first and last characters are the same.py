list1=["php","dfe","nun","wdeed","dvd"]
print(list1)
a=0
for i in list1:
    if len(i)>=2 and i[0]==i[-1]:
        print(i)
        a+=1
print(a)