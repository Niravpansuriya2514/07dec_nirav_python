str=input("enter your string: ")
len=len(str)

if len>2:
    first2=str[:2]
    last2=str[-2:]
    print("your string is: ",first2+last2)
else:
    print("invalid input")