dic1={'a':100,'b':200,'c':300}
dic2={'a':200,'b':300,'c':400,'d':500}
dic3={}


for i in dic1:
    print(dic1[i])
    if i in dic2:
        dic3[i]=dic1[i]+dic2[i]
print(dic3)

