dic={1:'python',3:'java',4:'android',2:'c'}
print(dic)

print("your dictionary is ascending")
sortdic1=sorted(dic.items())
print(dict(sortdic1))

len1=len(sortdic1)
sortdic2={}

for i in range(len1-1,-1,-1):
    sortdic2[sortdic1[i][0]]=sortdic1[i][1]
print("your dictionary id descending")
print(sortdic2)
