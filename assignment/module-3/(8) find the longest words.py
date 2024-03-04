a=open("demo.txt","r")

b=a.read()
print(b)
c=b.split()
d=list(c)
e=sorted(d,key=len)
print(e[-1])