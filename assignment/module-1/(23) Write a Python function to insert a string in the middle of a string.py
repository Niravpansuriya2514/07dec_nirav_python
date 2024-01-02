str=input("enter your string: ")
len=len(str)

a=0
b=0
if len%2==0:
    a=len/2
    a1=int(a)
    substr=input("enter your sub string: ")
    joinstr=str[:a1]+substr+str[a1:]
    print("your join string: ",joinstr)
else:
    len-1
    b=len/2
    b+1
    b1=int(b)
    substr=input("enter your sub string: ")
    joinstr2=str[:b1]+substr+str[b1:]
    print("your join string: ",joinstr2)