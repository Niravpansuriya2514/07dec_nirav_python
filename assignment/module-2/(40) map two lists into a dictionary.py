list1=['sub1','sub2','sub3','sub4']
list2=['python','android','c','c++']
print(list1,"\n",list2)
dic={}
for i in range(len(list1)):
    dic[list1[i]]=list2[i]
print(dic)
