dic={'leptop':50000,'mobile':15000,'mouse':200,'headphon':1000,'bag':2000}
list1=[]
list1=sorted(list(dic.values()))
print("your highest 3 value in dictionary")
print(list1[:-4:-1])