list=['id','name','city']
data={}
len=len(list)
print(len)

for i in list:
    v=input(f"enter your {i} :")
    data[i]=v

print(data)