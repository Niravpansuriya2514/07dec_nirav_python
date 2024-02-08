dic1={1:'python',2:'c'}
dic2={3:'java',4:'c++'}
dic3={5:'android',6:'flutter'}
maindic={}
for i in dic1.items():
    maindic[i[0]]=i[1]

for i in dic2.items():
    maindic[i[0]]=i[1]

for i in dic3.items():
    maindic[i[0]]=i[1]
print(maindic)
