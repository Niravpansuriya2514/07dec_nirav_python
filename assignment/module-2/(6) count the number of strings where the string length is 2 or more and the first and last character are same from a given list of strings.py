
list=['python','java','android','flutter','php']

# count the number of string
print("number of string in your list: ",len(list))

# return your string
for i in list:
    if len(i)>=2 and i[0]==i[-1]:
        print("your return string is: ",i)

