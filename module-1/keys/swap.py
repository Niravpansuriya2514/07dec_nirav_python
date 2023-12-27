a=20
b=10
print("a = ",a)
print("b = ",b)

print("value swap using third variable")
c=a #20
a=b #10
b=c #20
print("a = ",a)
print("b = ",b)
print("value swap without third variable use +- logic")
a=a+b
b=a-b
a=a-b
print("a = ",a)
print("b = ",b)
print("value swap without third variable without logic")
a,b=b,a
print("a = ",a)
print("b = ",b)
