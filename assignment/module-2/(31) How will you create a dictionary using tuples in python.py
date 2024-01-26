tuple1=('sub1','sub2','sub3','sub4')
tuple2=('python','java','android','flutter')
print("your tuple before convert dictionary")
print(tuple1,"\n",tuple2)

len1=len(tuple2)
dic={}

for i in range(len1):
    dic[tuple1[i]]=tuple2[i]

print("your distionary after convert tuple")   
print(dic)
        
    
    

