# Sample string: 'w3resource'
# Expected output:
# {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

a='w3resource'
print("your string")
print(a)

dic1={}

for i in a:
     dic1[i]=a.count(i)
print(dic1)