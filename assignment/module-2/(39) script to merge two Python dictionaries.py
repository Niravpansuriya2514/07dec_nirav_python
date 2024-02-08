dic1={}
dic2={}

n=int(input("how many enter number of pair: "))

for i in range(n):
    k=input("enter the key: ")
    v=input("enter the value: ")
    dic1[k]=v

for j in range(n):
    k=input("enter the key: ")
    v=input("enter the value: ")
    dic2[k]=v

print("your first dictionary")
print(dic1)
print("your second dictionary")
print(dic2)

for i,j in dic1.items():
    dic2[i]=j

print(dic2)