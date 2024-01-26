temp=open("file 1 to 100.txt","a")

for i in range(100):
    temp.write(f"{i+1}\n")