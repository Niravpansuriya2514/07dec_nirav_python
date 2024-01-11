a=[]
b=[]

n=int(input("enter your eliment of word: "))

for i in range(1,n+1):
    x=input(f"enter yor word {i}: ")
    a.append(x)
print(a)

for i in a:
    b.append((len(i),i))
print(b)
b.sort()
c=b[-1][0]
d=b[-1][1]
print(b)

print("longest word is: ",d)
print("length of longest word: ",c)
