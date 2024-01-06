# Lists are used to store multiple items in a single variable
# List is a collection which is ordered and changeable 
# Allows duplicate members

n=int(input("how many eliment enter in list: "))
str=[]

for i in range(n):
    s=input("enter your list eliment: ")
    str.append(s)
    
print(str)
str.reverse()
print(str)