tuple1=('java','python','android','c++','c++')

for i in tuple1:
    if tuple1.count(i)>1:
        print("your repeted item is: ",i)
        print("How many times in repeat: ",tuple1.count(i))
        break

