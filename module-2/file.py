temp=open("demo.txt","a")

id=int(input("input enter your id: "))
name=input("enter your name: ")
sub=input("enter  your sub: ")

temp.write(f"\nid = {id}\nname = {name}\nsub = {sub}")