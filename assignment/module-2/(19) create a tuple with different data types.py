# create static tuple
tuple1=('python',7238,3.14)

# create user input tuple
list=[]

str=input("enter your string eliment : ")
list.append(str)
int=int(input("enter your interger eliment : "))
list.append(int)
float=float(input("enter your float eliment : "))
list.append(float)
bool=bool(input("enter your boolian eliment : "))
list.append(bool)

tuple2=tuple(list)
print(tuple2)

    