str=input("enter your string: ")

str1=str.index('not')
str2=str.index('poor')
str3=str[str1:str2+4]
if str1<str2:
    print(str.replace(str3,'good'))
else:
    print("invalid input")