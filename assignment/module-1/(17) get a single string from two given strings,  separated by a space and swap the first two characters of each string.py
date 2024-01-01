str1=input("enter your string: ")
str2=input("enter your string: ")

print("swap before string")

print("str1 = ",str1)
print("str2 = ",str2)

a=str1[:2]
b=str2[:2]
print("a = ",a)
print("b = ",b)

print("swap after string")

print(str1.replace(a,b))
print(str2.replace(b,a))


