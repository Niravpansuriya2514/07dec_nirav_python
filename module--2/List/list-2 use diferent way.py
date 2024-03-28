list1=["python","java","c++","php","android","c","flutter","react js","node js"]
print(list1)

# check object "python" is  in list

if "python" in list1:
    print("yes..")
else:
    print("no..")

# print list using for loop

for i in list1:
    print(i)

# print index in object

print(list1.index("c++"))

for i in list1:
    print(f"{list1.index(i)} = {i}")

print("----------------------------")

n=0
for i in list1:
    print(f"{n} = {i}")
    n+=1