str=input("enter your string: ")
len=(len(str))

if str.endswith('ing') or len>3:
    print(str,end='ly')
elif len>3:
    print(str,end="ing")
else:
    print("invalid input")