list1=[('sub1','python'),('sub2','c'),('sub3','c++'),('sub4','android')]
print("list of tuple before convert dictionary")
print(list1)
dic={}

for i in list1:
    dic[i[0]]=i[1]
print("\nyore dictionary after convert list of tuples in to dictionary")
print(dic)

a={}
a=dict(list1)
print(a)
