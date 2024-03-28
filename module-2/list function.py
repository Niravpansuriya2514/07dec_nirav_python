data=['c','c++','ds','python','java','php']
print(data)


if 'c+' in data:
    print("yes...")
else:
    print("data is not found")

# replace your string in index wise
data[2]='android'
print(data)

# your list is print in for loop
for i in data:
    print(i)

# find your list in string index
print(data.index('android'))

# print all data is index wise using index functoion
for i in data:
    print(f"{data.index(i)}={i}")

# print all data is index wise without using index function
n=0
for i in data:
    print(f"{n}={i}")
    n+=1

# add data in your list in last eliment
data.append('database')
print(data)

# add data in your list in any space reference to index
data.insert(2,'c#')
print(data)

# data delete in your list in last eliment defalt
data.pop()
print(data)

# data delete in your list in index wise
data.pop(2)
print(data)

# data delete in your list object wise
data.remove('c')
print(data)

# data delete in index wise
del data[0]
print(data)

# all data clear in your list
# data.clear()
# print(data)

# print all data is reverse
data.reverse()
print(data)

# all data in order in alphabetically
data.sort()
print(data)

# data copy in other list
# newdata=data.copy()
# print(newdata)

# add other list in your list without using function
newdata=['HTML','CSS','JS','Bootstrap']
print(newdata)
print(data+newdata)

# add other list in your list using extend() function
data.extend(newdata)
print(data)

