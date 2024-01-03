set={"nirav","dhruv","nilesh","bhavy","nitin"}

# print length of set
print(set)
print("length of set is: ",len(set))

# find a object in your set
if 'dhruv'in set:
    print("yes....")
else:
    print("no....")

# print set in using for loop
for i in set:
    print(i)

# add object in set
set.add("ashvin")
print(set)

# add objects in set
set.update(['viraj',"dolar"])
print(set)

# set remove object
set.remove('viraj')
print(set)

# remove object defalt last object
set.pop()
print(set)

# remove all data in set
# set.clear()
# print(set)

newset={"bholo","jigo","bc","pilo"}
print(newset)

# add new set in your set
# print(set.union(newset))
x=set.union(newset)
print(x)

#clear set
# print(set.intersection(newset))
x=set.intersection(newset)
print(x)