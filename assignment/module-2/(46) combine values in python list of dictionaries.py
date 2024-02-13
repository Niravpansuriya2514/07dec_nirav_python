# Sample data: [{'item': 'item1', 'amount': 400},
#               {'item': 'item2', 'amount':300},
#               {'item': 'item1', 'amount': 750}]
# Expected Output:
# Counter ({'item1': 1150, 'item2': 300})


list1=[{'item': 'item1', 'amount': 400},
       {'item': 'item2', 'amount':300},            
       {'item': 'item1', 'amount': 750}]
import collections 

a=collections.Counter()

for i in list1:
    a[i['item']]+=i['amount']

print(a)