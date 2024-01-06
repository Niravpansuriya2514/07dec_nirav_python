tuple=("java","c","c++","python","android","flutter","php")
print(tuple)

# print(tuple[0])
# print(tuple[-1])
# print(tuple[0:3])
# print(tuple[:4])
# print(tuple[2:])
# print(tuple[::-1]) print reverse tuple
# print(tuple[:3:-1]) print reverse tuple in last object to third object
# print(tuple[3::-1]) print reverse tuple in third object to first object

# print last obj and last to next obj is skip and print to skip obj to next obj
# print(tuple[-1::-2])

# find length in tuple
print(len(tuple))

# find object
if 'php' in tuple:
    print("yes...")
else:
    print("no...")

# print tuple in column wise  using for loop
for i in tuple:
    print(i)

# find index in object using index function
print(tuple.index("c++"))

del tuple
print(tuple)