a=open("demo.txt","a")

id=input("enter your id: ")
name=input("enter your name: ")

a.write(f"\nid = {id}\nname = {name}")

b=open("demo.txt","r")

print(b.read())