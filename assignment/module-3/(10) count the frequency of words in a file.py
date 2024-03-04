a=open("demo.txt","r")

b={}
for i in a:
    c=i.split(" ")
    for j in c:
        if j in b:
           b[j]=b[j]+1
        else:
           b[j]=1

for key in list(b.keys()):
    print(key,"=",b[key])