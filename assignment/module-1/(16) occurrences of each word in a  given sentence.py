str=input("enter your sentence: ")

a=str.split()
print(a)

print("count word in your sentence using len function")
print(len(a))

print("count word in your sentence using for loop")
j=0
for i in a:
    j+=1
    
print(j)