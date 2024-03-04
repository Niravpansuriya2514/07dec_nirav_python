a=open("demo.txt","a")
b=open("file 1 to 100.txt","r")

c=b.read()
print(c)

a.write(f"\n{c}")