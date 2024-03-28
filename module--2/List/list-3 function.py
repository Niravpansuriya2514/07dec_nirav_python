list1=['c','c++','ds','python','java','php']

# print length in list
print(len(list1))

# add data in your list in last eliment
list1.append('database')
print(list1)

# add data in your list in any space reference to index
list1.insert(2,'c#')
print(list1)

# data delete in your list in last eliment defalt
list1.pop()
print(list1)

# data delete in your list in index wise
list1.pop(2)
print(list1)

# data delete in your list object wise
list1.remove('c')
print(list1)

# data delete in index wise
del list1[0]
print(list1)

# all data clear in your list
# list1.clear()
# print(list1)

# print all data is reverse
list1.reverse()
print(list1)

# all data in order in alphabetically
list1.sort()
print(list1)

# data copy in other list
newlist1=list1.copy()
print(newlist1)

# add other list in your list without using function
newlist1=['HTML','CSS','JS','Bootstrap']
print(newlist1)
print(list1+newlist1)


# add other list in your list using extend() function
list1.extend(newlist1)
print(list1)

