# Sample data: {'1': ['a','b'], '2': ['c','d']}
# Expected Output:
# ac ad bc bd


dic={1:['a','b'],2:['c','d']}
a=[]
for i,j in dic.items():
    a+=j
print(a[0]+a[2])
print(a[0]+a[3])
print(a[1]+a[2])
print(a[1]+a[3])

    